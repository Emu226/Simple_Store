from models.database import get_database_connection

class Storage:
    def __init__(self, code, name, description, last_modified, id=None):
        self.id = id
        self.code = code
        self.name = name
        self.description = description
        self.last_modified = last_modified

    @staticmethod
    def create(storage):
        # Erstellt einen neuen Lagerort in der Datenbank
        # Args: storage (Storage): Das Storage-Objekt, das erstellt werden soll
        # Raises: Exception: Wenn ein Fehler während der Datenbankoperation auftritt
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO Storages (Code, Name, Description, LastModified)
                VALUES (?, ?, ?, ?)
            ''', (storage.code, storage.name, storage.description, storage.last_modified))
            conn.commit()
        except Exception as e:
            print(f"Fehler beim Erstellen des Lagerorts: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def get_by_id(storage_id):
        # Holt einen Lagerort aus der Datenbank anhand seiner ID
        # Args: storage_id (int): Die ID des zu holenden Lagerorts
        # Returns: Storage: Ein Storage-Objekt wenn gefunden, sonst None
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT ID, Code, Name, Description, LastModified
                FROM Storages 
                WHERE ID = ?
            ''', (storage_id,))
            row = cursor.fetchone()
            if row:
                return Storage(
                    code=row[1],
                    name=row[2],
                    description=row[3],
                    last_modified=row[4],
                    id=row[0]
                )
            return None
        finally:
            conn.close()

    @staticmethod
    def get_all():
        # Holt alle Lagerorte aus der Datenbank
        # Yields: Storage-Objekte für jeden gefundenen Lagerort
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                SELECT ID, Code, Name, Description, LastModified
                FROM Storages
            ''')
            while True:
                row = cursor.fetchone()
                if row is None:
                    break
                yield Storage(
                    code=row[1],
                    name=row[2],
                    description=row[3],
                    last_modified=row[4],
                    id=row[0]
                )
        finally:
            conn.close()

    @staticmethod
    def update(storage):
        # Aktualisiert einen bestehenden Lagerort in der Datenbank
        # Args: storage (Storage): Das Storage-Objekt mit den aktualisierten Daten
        # Returns: bool: True wenn erfolgreich aktualisiert, False wenn nicht gefunden
        # Raises: Exception: Wenn ein Fehler während der Datenbankoperation auftritt
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('''
                UPDATE Storages 
                SET Code = ?, 
                    Name = ?, 
                    Description = ?, 
                    LastModified = ?
                WHERE ID = ?
            ''', (storage.code, storage.name, storage.description, 
                  storage.last_modified, storage.id))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Fehler beim Aktualisieren des Lagerorts: {e}")
            raise
        finally:
            conn.close()

    @staticmethod
    def delete(storage_id):
        # Löscht einen Lagerort aus der Datenbank anhand seiner ID
        # Args: storage_id (int): Die ID des zu löschenden Lagerorts
        # Returns: bool: True wenn erfolgreich gelöscht, False wenn nicht gefunden
        # Raises: Exception: Wenn ein Fehler während der Datenbankoperation auftritt
        conn = get_database_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM Storages WHERE ID = ?', (storage_id,))
            conn.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Fehler beim Loschen des Lagerorts: {e}")
            raise
        finally:
            conn.close()

