import sqlite3

def get_database_connection():
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect("C:/1code/Simple_Store/Simple_Store/models/simplystore.db")
    return conn