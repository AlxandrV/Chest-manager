from tinydb import TinyDB, Query, table
import os

class Database:

    def __init__(self) -> None:
        self._db = TinyDB('db.json')
        self._q = Query()

    def insert(self, table, to_insert):
        """Insert into table in database"""
        self._db.table(table).insert(to_insert)

    def search(self, table_name, id_value):
        table_result = self._db.table(table_name)
        return table_result.get(doc_id=id_value)

    def delete(self):
        pass

    def update(self):
        pass