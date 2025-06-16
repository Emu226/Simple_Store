import tkinter as tk
from tkinter import ttk, messagebox
from models.storage import Storage  # Import der Storage-Klasse für die Lagerorte

class ArticleDialog:
    """
    Dialog-Fenster zur Erstellung und Bearbeitung von Artikeln.
    
    Diese Klasse erstellt ein modales Dialogfenster mit Eingabefeldern für alle
    relevanten Artikeldaten. Das Fenster kommuniziert über einen Callback mit dem
    Controller, der die eigentliche Datenspeicherung übernimmt.

    Attributes:
        dialog (tk.Toplevel): Das Dialogfenster
        callback (callable): Funktion die aufgerufen wird wenn der Benutzer auf Speichern klickt
        fields (dict): Dictionary mit allen Eingabefeldern, key ist die field_id
        storage_mapping (dict): Dictionary zur Zuordnung von Lagerort-Display-Strings zu Codes
    """

    def __init__(self, parent, callback):
        """
        Initialisiert das Dialogfenster.

        Args:
            parent (tk.Widget): Das übergeordnete Fenster
            callback (callable): Funktion die die eingegebenen Daten verarbeitet.
                               Erwartet ein Dictionary mit den Artikeldaten und
                               gibt Boolean zurück (True = Erfolg)
        """
        self.dialog = tk.Toplevel(parent)
        self.callback = callback
        self.setup_ui()
    
    def setup_ui(self):
        """
        Erstellt und konfiguriert alle UI-Elemente des Dialogs.
        
        Erzeugt ein Formular mit Eingabefeldern für alle Artikel-Attribute.
        Pflichtfelder sind mit einem * gekennzeichnet.
        """
        self.dialog.title("Neuer Artikel")
        self.dialog.geometry("400x550")
        
        # Dictionary für die Eingabefelder
        self.fields = {}
        
        # Konfiguration der Eingabefelder
        # Tupel aus: (field_id, label_text)
        # field_id wird als Key im fields Dictionary verwendet
        # * am Ende des label_text kennzeichnet Pflichtfelder
        field_configs = [
            ("code", "Artikel Code:*"),      # Eindeutiger Identifikator
            ("name", "Artikel Name:*"),      # Bezeichnung des Artikels
            ("desc", "Beschreibung:"),       # Optional: Detaillierte Beschreibung
            ("price", "Preis:*"),           # Preis in EUR
            ("quantity", "Menge:*"),        # Verfügbare Stückzahl
            ("category", "Kategorie:")       # Optional: Gruppierung
        ]
        
        # Erstelle Eingabefelder gemäß Konfiguration
        for field_id, label_text in field_configs:
            ttk.Label(self.dialog, text=label_text).pack(pady=5)
            self.fields[field_id] = ttk.Entry(self.dialog)
            self.fields[field_id].pack(pady=5)

        # Lagerorte laden
        storage_locations = list(Storage.get_all())
        
        # Storage Dropdown erstellen
        ttk.Label(self.dialog, text="Lagerort:*").pack(pady=5)
        self.fields['storage'] = ttk.Combobox(self.dialog, state='readonly')
        self.fields['storage'].pack(pady=5)
        
        # Combobox mit Werten füllen
        storage_values = [(s.code, f"{s.code} - {s.name}") for s in storage_locations]
        self.fields['storage']['values'] = [f"{code} - {name}" for code, name in storage_values]
        self.storage_mapping = {f"{code} - {name}": code for code, name in storage_values}
        
        # Wenn keine Lagerorte vorhanden sind
        if not storage_locations:
            messagebox.showwarning(
                "Kein Lagerort",
                "Es sind keine Lagerorte verfügbar. Bitte erst einen Lagerort erstellen."
            )
            self.dialog.destroy()
            return
        
        # Button-Frame am unteren Rand
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(pady=20)
        
        # Speichern- und Abbrechen-Buttons
        ttk.Button(button_frame, text="Speichern", 
                  command=self.save).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Abbrechen", 
                  command=self.dialog.destroy).pack(side="left", padx=5)

    def get_selected_storage(self):
        """
        Gibt den Code des ausgewählten Lagerorts zurück.
        
        Returns:
            str: Der Code des ausgewählten Lagerorts oder ein leerer String.
        """
        selected = self.fields['storage'].get()
        return self.storage_mapping.get(selected, '')

    def save(self):
        """
        Sammelt alle Eingabedaten und übergibt sie an den Controller.
        
        Sammelt die Werte aller Eingabefelder in ein Dictionary und übergibt
        dieses an die Callback-Funktion. Wenn der Callback True zurückgibt
        (erfolgreiches Speichern), wird der Dialog geschlossen.
        
        Returns:
            None
        """
        # Überprüfe ob ein Lagerort ausgewählt wurde
        if not self.fields['storage'].get():
            messagebox.showerror("Fehler", "Bitte wählen Sie einen Lagerort aus.")
            return
            
        # Erstelle Dictionary mit allen Eingabewerten
        data = {field: widget.get() for field, widget in self.fields.items()}
        
        # Ersetze den Display-String mit dem tatsächlichen Storage-Code
        data['storage'] = self.get_selected_storage()
        
        # Validiere Pflichtfelder
        required_fields = ['code', 'name', 'price', 'quantity', 'storage']
        for field in required_fields:
            if not data[field]:
                messagebox.showerror(
                    "Fehler",
                    f"Bitte füllen Sie alle Pflichtfelder aus. ({field})"
                )
                return
        
        # Übergebe Daten an Controller und schließe bei Erfolg
        if self.callback(data):
            self.dialog.destroy()