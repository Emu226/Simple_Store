import tkinter as tk
from tkinter import ttk, messagebox
import models.database as database
from datetime import datetime
import models.article as article

class ArticleListWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Simply Store - Artikel Liste")
        self.root.geometry("800x600")
        
        # Erstelle Treeview für Artikel-Liste
        self.tree = ttk.Treeview(root, columns=("Code", "Name", "Description", "Price", "Quantity", "Category", "Storage", "Created"), show="headings")
        
        # Definiere Spalten
        columns = {
            "Code": 100,
            "Name": 150,
            "Description": 200,
            "Price": 80,
            "Quantity": 80,
            "Category": 100,
            "Storage": 80,
            "Created": 150
        }
        
        for col, width in columns.items():
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Layout
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button Frame
        button_frame = ttk.Frame(root)
        button_frame.pack(side="bottom", fill="x", padx=5, pady=5)
        
        # Buttons
        ttk.Button(button_frame, text="Aktualisieren", command=self.refresh_data).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Neuer Artikel", command=self.show_add_dialog).pack(side="left", padx=5)
        
        # Initial Daten laden
        self.refresh_data()
    
    def refresh_data(self):
        try:
            # Lösche bestehende Einträge
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Lade und zeige Artikel
            articles = database.get_all_articles()
            for art in articles:
                self.tree.insert("", "end", values=art)
        except Exception as e:
            messagebox.showerror("Datenbankfehler", f"Fehler beim Laden der Artikel: {str(e)}")
    
    def validate_inputs(self, code, name, price, quantity):
        if not code or not name:
            raise ValueError("Code und Name sind Pflichtfelder!")
        if not price:
            raise ValueError("Bitte geben Sie einen gultigen Preis ein!")
        if not quantity:
            raise ValueError("Bitte geben Sie eine gultige Menge ein!")
    
    def show_add_dialog(self):
        dialog = tk.Toplevel(self.root)
        dialog.title("Neuer Artikel")
        dialog.geometry("400x500")
        
        # Eingabefelder
        fields = {}
        
        ttk.Label(dialog, text="Artikel Code:*").pack(pady=5)
        fields['code'] = ttk.Entry(dialog)
        fields['code'].pack(pady=5)
        
        ttk.Label(dialog, text="Artikel Name:*").pack(pady=5)
        fields['name'] = ttk.Entry(dialog)
        fields['name'].pack(pady=5)
        
        ttk.Label(dialog, text="Beschreibung:").pack(pady=5)
        fields['desc'] = ttk.Entry(dialog)
        fields['desc'].pack(pady=5)
        
        ttk.Label(dialog, text="Preis:*").pack(pady=5)
        fields['price'] = ttk.Entry(dialog)
        fields['price'].pack(pady=5)
        
        ttk.Label(dialog, text="Menge:*").pack(pady=5)
        fields['quantity'] = ttk.Entry(dialog)
        fields['quantity'].pack(pady=5)
        
        ttk.Label(dialog, text="Kategorie:").pack(pady=5)
        fields['category'] = ttk.Entry(dialog)
        fields['category'].pack(pady=5)
        
        ttk.Label(dialog, text="Lager ID:").pack(pady=5)
        fields['storage'] = ttk.Entry(dialog)
        fields['storage'].pack(pady=5)
        
        def save_article():
            try:
                # Validierung
                self.validate_inputs(
                    fields['code'].get(),
                    fields['name'].get(),
                    fields['price'].get(),
                    fields['quantity'].get()
                )
                
                new_article = article.Article(
                    fields['code'].get(),
                    fields['name'].get(),
                    fields['desc'].get(),
                    float(fields['price'].get()),
                    int(fields['quantity'].get()),
                    fields['category'].get(),
                    fields['storage'].get(),
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
                article.Article.create(new_article)
                self.refresh_data()
                dialog.destroy()
            except ValueError as e:
                messagebox.showerror("Eingabefehler", str(e))
            except Exception as e:
                messagebox.showerror("Fehler", f"Fehler beim Speichern: {str(e)}")
        
        # Buttons
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=20)
        
        ttk.Button(button_frame, text="Speichern", command=save_article).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Abbrechen", command=dialog.destroy).pack(side="left", padx=5)

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = ArticleListWindow(root)
    root.mainloop()