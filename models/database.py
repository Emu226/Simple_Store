import sqlite3
from venv import create
from datetime import datetime
from services.data_service import get_database_connection # Importieren der Datenbankverbindung "conn"
from models import article
from models import storage

def get_database_connection():
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect("C:/1code/Simple_Store/Simple_Store/models/simplystore.db")
    return conn

def create_storages_table():
    #StoragesID, StorageName, StorageDescription, LastModified
    conn = get_database_connection()
    cursor = conn.cursor()
    try:
        # Tabelle erstellen, falls sie nicht existiert
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Storages (
                       "Id" INTEGER NOT NULL CONSTRAINT "PK_Storages" PRIMARY KEY AUTOINCREMENT,
                       "Code" TEXT NOT NULL,
                       "Name" TEXT NOT NULL,
                       "Description" TEXT NOT NULL,
                       "LastModified" TEXT NOT NULL
                        )
        ''')
        conn.commit()
    finally:
        # Verbindung immer schließen
        conn.close()


def create_articles_table():
    conn = get_database_connection()
    cursor = conn.cursor()
    
    try:
        # Tabelle erstellen, falls sie nicht existiert
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Articles (
                       "Id" INTEGER NOT NULL CONSTRAINT "PK_Articles" PRIMARY KEY AUTOINCREMENT,
                       "Code" TEXT NOT NULL,
                       "Name" TEXT NOT NULL,
                       "Description" TEXT NOT NULL,
                       "Price" TEXT NOT NULL,
                       "Quantity" INTEGER NOT NULL,
                       "Category" TEXT NOT NULL,
                       "Storage_where" TEXT NOT NULL,
                       "LastModified" TEXT NOT NULL,
                       --Fremdschlüssel-Beziehung: Verknüpft Artikel mit ihrem Lagerort. 
                       --Wenn ein Lagerort gelöscht wird, werden alle zugehörigen Artikel automatisch gelöscht (CASCADE)
                       CONSTRAINT "FK_Articles_Storages_Storage_where" FOREIGN KEY ("Storage_where") REFERENCES "Storages" ("Code") ON DELETE CASCADE
                        )
        ''')
        conn.commit()
    finally:
        # Verbindung immer schließen
        conn.close()


def get_all_articles():
    conn = get_database_connection()
    cursor = conn.cursor()
    
    try:
        # Tabelle abfragen
        cursor.execute("SELECT * FROM Articles")
        rows = cursor.fetchall()
        return rows
    finally:
        # Verbindung immer schließen
        conn.close()

create_storages_table()
create_articles_table()

# Beispiel-Storage und Article erstellen
storage.Storage.create(storage.Storage("ST001", "Lager 1", "Hauptlager", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
article.Article.create(article.Article("AR001", "Artikel 1", "Beschreibung Artikel 1", "19.99", 100, "Kategorie A", 1, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

# Beispielaufruf
if __name__ == "__main__":
    articles = get_all_articles()
    for article in articles:
        print(article)