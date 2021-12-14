from tinydb import TinyDB, Query, table
import os

class Database:

    def __init__(self) -> None:
        self._db = TinyDB('db.json')
        self._q = Query()

    def insert(self, table, to_insert):
        """Insert into table in database"""
        self._db.table(table).insert(to_insert)

    def search_table(self, table_name):
        """Search and retun a table in database"""
        return self._db.table(table_name)

    def search_single(self, table_name, id_value):
        """Search and return a single value by id"""
        return table_name.get(doc_id=id_value)

    def search_more(self, table_name, index_start, limit=10):
        return table_name.all()[index_start:limit]

    def delete(self):
        pass

    def update(self):
        pass

    def last_insert(self, table_name):
        """Return id of the last insert in table"""
        table_result = self._db.table(table_name)
        max_id = False
        for result in table_result:
            if result.doc_id > max_id:
                max_id = result.doc_id
        return max_id