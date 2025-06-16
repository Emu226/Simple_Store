from tkinter import messagebox
from datetime import datetime
from models.article import Article
from views.article_dialog import ArticleDialog

class ArticleListController:
    def __init__(self):
        self.view = None
    
    def set_view(self, view):
        self.view = view
        self.refresh_data()  # Jetzt können wir die Daten laden
    
    def refresh_data(self):
        """Lädt die Artikel-Daten und aktualisiert die View"""
        try:
            articles = Article.get_all()
            self.view.update_article_list(articles)
        except Exception as e:
            messagebox.showerror("Datenbankfehler", f"Fehler beim Laden der Artikel: {str(e)}")
    
    def show_add_dialog(self):
        """Zeigt den Dialog zum Hinzufügen eines neuen Artikels"""
        dialog = ArticleDialog(self.view.root, self.save_article)
    
    def save_article(self, article_data):
        """Speichert einen neuen Artikel"""
        try:
            new_article = Article(
                code=article_data['code'],
                name=article_data['name'],
                description=article_data['desc'],
                price=float(article_data['price']),
                quantity=int(article_data['quantity']),
                category=article_data['category'],
                storage_where=article_data['storage'],
                last_modified=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            )
            Article.create(new_article)
            self.refresh_data()
            return True
        except ValueError as e:
            messagebox.showerror("Eingabefehler", str(e))
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Speichern: {str(e)}")
        return False