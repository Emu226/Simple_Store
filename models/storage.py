from models.database import get_database_connection
from services.data_service import get_database_connection # Importieren der Datenbankverbindung "conn"

class Storage:
    def __init__(self, code, name, description, last_modified, id=None):
        self.id = id
        self.code = code
        self.name = name
        self.description = description
        self.last_modified = last_modified

    @staticmethod
    def create(storage):
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Storages (Code, Name, Description, LastModified)
                VALUES (?, ?, ?, ?)
            ''', (storage.code, storage.name, storage.description, storage.last_modified))
            conn.commit()
        finally:
            conn.close()

