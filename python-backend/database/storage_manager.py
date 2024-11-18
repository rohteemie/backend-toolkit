# storage/storage_manager.py
class StorageManager:
    def __init__(self, backend="SQL"):
        if backend == "SQL":
            from database.sql_db_storage import DBStorage
            self.storage = DBStorage()
        elif backend == "NoSQL":
            from database.nosql_db_storage import NoSQLDBStorage
            self.storage = NoSQLDBStorage()
        elif backend == "File":
            from database.file_storage import FileStorage
            self.storage = FileStorage()
        else:
            raise ValueError("Unsupported storage backend")

    def all(self, cls=None):
        return self.storage.all(cls)

    def new(self, obj):
        self.storage.new(obj)

    def save(self):
        self.storage.save()

    def delete(self, obj):
        self.storage.delete(obj)

    def get(self, cls, id):
        return self.storage.get(cls, id)

    def count(self, cls=None):
        return self.storage.count(cls)
