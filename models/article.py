from models.database import get_database_connection

# This module defines the Article class, which represents an article/item in the store and provides methods for database operations.
# Classes:
#     Article: Represents an article with attributes such as code, name, description, price, quantity, category, storage location, last modified date, and optional ID.
# Methods:
#     __init__(self, code, name, description, price, quantity, category, storage_where, last_modified, id=None):
#         Initializes an Article instance with the provided attributes.
#     create(article):
#         Static method to insert a new article into the Articles table in the database.
#     get_by_id(article_id):
#         Static method to retrieve an article from the database by its ID. Returns an Article instance if found, otherwise None.
#     get_all():
#         Static method to retrieve all articles from the database. Yields Article instances for each row found.

class Article:
    # Represents an article in the Simple Store inventory system.
    def __init__(self, code, name, description, price, quantity, category, storage_where, last_modified, id=None):
        self.id = id
        self.code = code
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.category = category
        self.storage_where = storage_where
        self.last_modified = last_modified

    @staticmethod
    def create(article):
        # Creates a new article record in the Articles table of the database.
        # Raises:
        # Exception: If an error occurs during the database operation, the exception is printed and re-raised.
    
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Articles (Code, Name, Description, Price, Quantity, Category, Storage_where, LastModified)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (article.code, article.name, article.description, article.price, article.quantity, article.category, article.storage_where, article.last_modified))
            conn.commit()
        except Exception as e:
            print(f"Error occurred while creating article: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_by_id(article_id):
        # Retrieve an Article object from the database by its ID.
        # Args: article_id (int): The unique identifier of the article to retrieve.
        # Returns: Article: An Article object populated with data from the database if found, otherwise None.
        # Raises: Exception: If an error occurs while fetching the article from the database.
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT ID, Code, Name, Description, Price, Quantity, Category, Storage_where, LastModified
                FROM Articles 
                WHERE ID = ?
            ''', (article_id,))
            row = cursor.fetchone()
            if row:
                return Article(
                    code=row[1],
                    name=row[2],
                    description=row[3],
                    price=row[4],
                    quantity=row[5],
                    category=row[6],
                    storage_where=row[7],
                    last_modified=row[8],
                    id=row[0]
                )
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all():
        # Retrieve all articles from the database.
        # Yields Article objects for each article found in the database.
        # This is a generator method that yields Article objects one by one.
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT ID, Code, Name, Description, Price, Quantity, Category, Storage_where, LastModified
                FROM Articles
            ''')
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                yield Article(
                    code=row[1],
                    name=row[2],
                    description=row[3],
                    price=row[4],
                    quantity=row[5],
                    category=row[6],
                    storage_where=row[7],
                    last_modified=row[8],
                    id=row[0]
                )
        finally:
            conn.close()

    @staticmethod
    def update(article):
        # Aktualisiert einen bestehenden Artikel in der Datenbank.
        # Args:article (Article): Das Article-Objekt mit den aktualisierten Daten.
        # Raises:Exception: Wenn ein Fehler während der Datenbankoperation auftritt.
        # Returns: bool: True wenn erfolgreich aktualisiert, False wenn der Artikel nicht gefunden wurde.
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE Articles 
                SET Code = ?, 
                    Name = ?, 
                    Description = ?, 
                    Price = ?, 
                    Quantity = ?, 
                    Category = ?, 
                    Storage_where = ?, 
                    LastModified = ?
                WHERE ID = ?
            ''', (article.code, article.name, article.description, article.price, 
                  article.quantity, article.category, article.storage_where, 
                  article.last_modified, article.id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Fehler beim Aktualisieren des Artikels: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def delete(article_id):
        # Löscht einen Artikel aus der Datenbank anhand seiner ID.
        # Args: article_id: Die ID des zu löschenden Artikels.
        # Raises: Exception: Wenn ein Fehler während der Datenbankoperation auftritt.
        # Returns: bool: True wenn erfolgreich gelöscht, False wenn der Artikel nicht gefunden wurde.
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM Articles WHERE ID = ?', (article_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Fehler beim Löschen des Artikels: {e}")
            raise
        finally:
            conn.close()