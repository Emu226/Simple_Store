import sqlite3

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
                       "Storage_where" INTEGER NOT NULL,
                       "LastModified" TEXT NOT NULL,
                       --Fremdschlüssel-Beziehung: Verknüpft Artikel mit ihrem Lagerort. 
                       --Wenn ein Lagerort gelöscht wird, werden alle zugehörigen Artikel automatisch gelöscht (CASCADE)
                       CONSTRAINT "FK_Articles_Storages_Storage_where" FOREIGN KEY ("Storage_where") REFERENCES "Storages" ("Id") ON DELETE CASCADE
                        )
        ''')
        conn.commit()
    finally:
        # Verbindung immer schließen
        conn.close()


def add_storage(code, name, description, last_modified):
    conn = get_database_connection()
    cursor = conn.cursor()
    
    try:
        # Lagerort in die Tabelle einfügen
        cursor.execute('''
            INSERT INTO Storages (Code, Name, Description, LastModified)
            VALUES (?, ?, ?, ?)
        ''', (code, name, description, last_modified))
        conn.commit()
    finally:
        # Verbindung immer schließen
        conn.close()


def add_article(code, name, description, price, quantity, category, storage_where, last_modified):
    conn = get_database_connection()
    cursor = conn.cursor()
    
    try:
        # Artikel in die Tabelle einfügen
        cursor.execute('''
            INSERT INTO Articles (Code, Name, Description, Price, Quantity, Category, Storage_where, LastModified)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (code, name, description, price, quantity, category, storage_where, last_modified))
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
# Demo data insert:
add_storage("ST001", "Lager 1", "Hauptlager für Artikel", "2023-10-01 12:00:00")
add_storage("ST002", "Lager 2", "Zweites Lager für spezielle Artikel", "2023-10-01 12:00:00")
add_article("AR001", "Artikel 1", "Beschreibung von Artikel 1", "19.99", 100, "Kategorie A", 1, "2023-10-01 12:00:00")
add_article("AR002", "Artikel 2", "Beschreibung von Artikel 2", "29.99", 50, "Kategorie B", 2, "2023-10-01 12:00:00")


# Beispielaufruf
if __name__ == "__main__":
    articles = get_all_articles()
    for article in articles:
        print(article)