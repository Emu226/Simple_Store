import tkinter as tk
from tkinter import ttk, messagebox
import models.database as database
from datetime import datetime
from models.article import Article
from models.storage import Storage
from views.article_list_window import ArticleListWindow
from controllers.article_list_controller import ArticleListController
from views.scan_window import ScanWindow
from views.main_window import MainWindow

def main():
    #start MainWindow
    root = tk.Tk()
    main_window = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()