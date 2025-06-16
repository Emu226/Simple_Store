from tkinter import messagebox
from datetime import datetime
from models.storage import Storage
from views.storage_dialog import StorageDialog

class StorageListController:
    def __init__(self):
        self.view = None
    
    def set_view(self, view):
        self.view = view
        self.refresh_data()
    
    def refresh_data(self):
        """Lädt die Lagerort-Daten und aktualisiert die View"""
        try:
            storages = Storage.get_all()
            self.view.update_storage_list(storages)
        except Exception as e:
            messagebox.showerror("Datenbankfehler", 
                               f"Fehler beim Laden der Lagerorte: {str(e)}")
    
    def show_add_dialog(self):
        """Zeigt den Dialog zum Hinzufügen eines neuen Lagerorts"""
        dialog = StorageDialog(self.view.root, self.save_storage)
    
    def save_storage(self, storage_data):
        """Speichert einen neuen Lagerort"""
        try:
            new_storage = Storage(
                code=storage_data['code'],
                name=storage_data['name'],
                description=storage_data['desc'],
                last_modified=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            Storage.create(new_storage)
            self.refresh_data()
            return True
        except ValueError as e:
            messagebox.showerror("Eingabefehler", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Speichern: {str(e)}")
        return False