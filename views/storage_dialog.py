import tkinter as tk
from tkinter import ttk, messagebox

class StorageDialog:
    """
    Dialog-Fenster zur Erstellung und Bearbeitung von Lagerorten.
    
    Diese Klasse erstellt ein modales Dialogfenster mit Eingabefeldern für alle
    relevanten Lagerort-Daten. Das Fenster kommuniziert über einen Callback mit dem
    Controller, der die eigentliche Datenspeicherung übernimmt.

    Attributes:
        dialog (tk.Toplevel): Das Dialogfenster
        callback (callable): Funktion die aufgerufen wird wenn der Benutzer auf Speichern klickt
        fields (dict): Dictionary mit allen Eingabefeldern, key ist die field_id
    """

    def __init__(self, parent, callback):
        """
        Initialisiert das Dialogfenster.

        Args:
            parent (tk.Widget): Das übergeordnete Fenster
            callback (callable): Funktion die die eingegebenen Daten verarbeitet.
                               Erwartet ein Dictionary mit den Lagerort-Daten und
                               gibt Boolean zurück (True = Erfolg)
        """
        self.dialog = tk.Toplevel(parent)
        self.callback = callback
        self.setup_ui()
    
    def setup_ui(self):
        """
        Erstellt und konfiguriert alle UI-Elemente des Dialogs.
        
        Erzeugt ein Formular mit Eingabefeldern für alle Lagerort-Attribute.
        Pflichtfelder sind mit einem * gekennzeichnet.
        """
        self.dialog.title("Neuer Lagerort")
        self.dialog.geometry("400x300")
        
        # Dictionary für die Eingabefelder
        self.fields = {}
        
        # Konfiguration der Eingabefelder
        field_configs = [
            ("code", "Lagerort Code:*"),    # Eindeutiger Identifikator
            ("name", "Bezeichnung:*"),       # Name des Lagerorts
            ("desc", "Beschreibung:")        # Optional: Detaillierte Beschreibung
        ]
        
        # Erstelle Eingabefelder gemäß Konfiguration
        for field_id, label_text in field_configs:
            ttk.Label(self.dialog, text=label_text).pack(pady=5)
            self.fields[field_id] = ttk.Entry(self.dialog)
            self.fields[field_id].pack(pady=5)
        
        # Button-Frame am unteren Rand
        button_frame = ttk.Frame(self.dialog)
        button_frame.pack(pady=20)
        
        # Speichern- und Abbrechen-Buttons
        ttk.Button(button_frame, text="Speichern", 
                  command=self.save).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Abbrechen", 
                  command=self.dialog.destroy).pack(side="left", padx=5)
    
    def save(self):
        """
        Sammelt alle Eingabedaten und übergibt sie an den Controller.
        
        Sammelt die Werte aller Eingabefelder in ein Dictionary und übergibt
        dieses an die Callback-Funktion. Wenn der Callback True zurückgibt
        (erfolgreiches Speichern), wird der Dialog geschlossen.
        """
        data = {field: widget.get() for field, widget in self.fields.items()}
        
        if self.callback(data):
            self.dialog.destroy()