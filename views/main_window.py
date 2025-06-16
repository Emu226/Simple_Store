import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Simply Store")
        self.root.geometry("400x300")
        
        # Configure the main grid
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        
        # Create menubar
        self.create_menubar()
        
        # Create main content
        self.create_main_content()
        
        # Style configuration
        self.configure_styles()
        
        # Initialize controller
        from controllers.article_list_controller import ArticleListController
        self.article_list_controller = ArticleListController()

    def configure_styles(self):
        style = ttk.Style()
        # Configure scan button style
        style.configure(
            "Scan.TButton",
            font=("Helvetica", 14, "bold"),
            padding=20
        )

    def create_menubar(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Create File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Menu", menu=file_menu)
        
        file_menu.add_command(label="📋 All Articles", command=self.show_articles)
        file_menu.add_command(label="🏪 Storage", command=self.show_storage)
        file_menu.add_command(label="📊 Dashboard", command=self.show_dashboard)
        file_menu.add_separator()
        file_menu.add_command(label="⚙️ Settings", command=self.show_settings)
        file_menu.add_separator()
        file_menu.add_command(label="🎮 Load Demo", command=self.load_demo)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

    def create_main_content(self):
        # Create and pack the header label
        header_label = ttk.Label(
            self.root,
            text="Simply Store",
            font=("Helvetica", 24)
        )
        header_label.grid(row=0, column=0, pady=20)

        # Create frame for scan elements
        scan_frame = ttk.Frame(self.root)
        scan_frame.grid(row=1, column=0, pady=10)

        # Create entry field
        self.scan_entry = ttk.Entry(
            scan_frame,
            width=20,
            font=("Helvetica", 12)
        )
        self.scan_entry.pack(pady=5)
        
        # Set focus to entry field
        self.scan_entry.focus()

        # Bind Enter key to scan function
        self.scan_entry.bind('<Return>', lambda e: self.open_scan_window())

        # Create and pack the scan button
        scan_button = ttk.Button(
            scan_frame,
            text="📱 SCAN ARTICLE",
            style="Scan.TButton",
            command=self.open_scan_window
        )
        scan_button.pack(pady=5)
        
        # Create version label
        version_label = ttk.Label(
            self.root,
            text="v1.0",
            font=("Helvetica", 8)
        )
        version_label.grid(row=2, column=0, pady=10)

    # Placeholder methods for menu actions
    def open_scan_window(self):
        scanned_value = self.scan_entry.get()
        if not scanned_value:
            print("Please enter an article ID")
            return
            
        # Clear entry field
        self.scan_entry.delete(0, tk.END)
        
        # Show scan type selection window
        from views.scan_window import show_scan_window
        result = show_scan_window(self.root, scanned_value)
        
        if result:
            # Handle the result
            if result["type"] == "article":
                from views.article_dialog import ArticleDialog
                from models.article import Article
                import datetime
                
                def create_article(data):
                    try:
                        # Erstelle neues Article-Objekt
                        article = Article(
                            code=data['code'],
                            name=data['name'],
                            description=data.get('desc', ''),
                            price=float(data.get('price', 0)),
                            quantity=int(data.get('quantity', 0)),
                            category=data.get('category', ''),
                            storage_where=data.get('storage', None),
                            last_modified=datetime.datetime.now()
                        )
                        # Speichere in Datenbank
                        Article.create(article)
                        return True
                    except Exception as e:
                        print(f"Fehler beim Erstellen des Artikels: {e}")
                        return False

                # Öffne Article Dialog
                dialog = ArticleDialog(self.root, create_article)
                # Setze den gescannten Code
                dialog.fields['code'].insert(0, result['code'])
                # Mache Code-Feld schreibgeschützt
                dialog.fields['code'].configure(state='readonly')
                
                # Warte bis der Dialog geschlossen wird
                self.root.wait_window(dialog.dialog)
                
                # Wenn der Artikel erfolgreich erstellt wurde, öffne die Artikel-Liste
                if dialog.dialog.winfo_exists() == 0:  # Dialog wurde geschlossen
                    self.open_article_list()
                
            else:  # storage
                from views.storage_dialog import StorageDialog
                from models.storage import Storage
                import datetime
                
                def create_storage(data):
                    try:
                        # Erstelle neues Storage-Objekt
                        storage = Storage(
                            code=data['code'],
                            name=data['name'],
                            description=data.get('desc', ''),
                            last_modified=datetime.datetime.now()
                        )
                        # Speichere in Datenbank
                        Storage.create(storage)
                        return True
                    except Exception as e:
                        print(f"Fehler beim Erstellen des Lagerorts: {e}")
                        return False

                # Öffne Storage Dialog
                dialog = StorageDialog(self.root, create_storage)
                # Setze den gescannten Code
                dialog.fields['code'].insert(0, result['code'])
                # Mache Code-Feld schreibgeschützt
                dialog.fields['code'].configure(state='readonly')
                
                # Warte bis der Dialog geschlossen wird
                self.root.wait_window(dialog.dialog)
                
                # Wenn der Lagerort erfolgreich erstellt wurde, öffne die Artikel-Liste
                if dialog.dialog.winfo_exists() == 0:  # Dialog wurde geschlossen
                    self.open_article_list()

    def open_article_list(self):
        """Öffnet das ArticleListWindow in einem neuen Fenster"""
        list_window = tk.Toplevel(self.root)
        from views.article_list_window import ArticleListWindow
        article_list_window = ArticleListWindow(list_window, self.article_list_controller)
        # Wichtig: Setze zuerst die View im Controller
        self.article_list_controller.set_view(article_list_window)

    def show_articles(self):
        print("Showing articles...")

    def show_storage(self):
        print("Showing storage...")

    def show_dashboard(self):
        print("Showing dashboard...")

    def show_settings(self):
        print("Showing settings...")

    def load_demo(self):
        print("Loading demo...")

def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()