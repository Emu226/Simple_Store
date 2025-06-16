import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from models.article import Article

class ArticleListWindow:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.setup_ui()
    
    def setup_ui(self):
        self.root.title("Simply Store - Artikel Liste")
        self.root.geometry("800x600")
        
        # Erstelle Treeview für Artikel-Liste
        self.tree = ttk.Treeview(self.root, 
            columns=("Code", "Name", "Description", "Price", "Quantity", "Category", "Storage", "Created"), 
            show="headings")
        
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
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Layout
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Button Frame
        button_frame = ttk.Frame(self.root)
        button_frame.pack(side="bottom", fill="x", padx=5, pady=5)
        
        # Buttons
        ttk.Button(button_frame, text="Aktualisieren", 
                  command=self.controller.refresh_data).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Neuer Artikel", 
                  command=self.controller.show_add_dialog).pack(side="left", padx=5)
    
    def update_article_list(self, articles):
        """Aktualisiert die Artikel-Liste in der TreeView"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for art in articles:
            self.tree.insert("", "end", values=(
                art.code, art.name, art.description, art.price,
                art.quantity, art.category, art.storage_where, art.last_modified
            ))