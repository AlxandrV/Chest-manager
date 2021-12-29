from tinydb import TinyDB, Query, table
import os

from tinydb.utils import T

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

    def search_single(self, datas_table, id_value):
        """Search and return a single value by id"""
        return datas_table.get(doc_id=id_value)

    def search_more(self, datas_table, index_start, limit=10):
        return datas_table.all()[index_start:limit]

    def delete(self):
        pass

    def update(self, datas_table, id_index, data_to_update):
        """Update an item in table"""
        datas_table.update(data_to_update, doc_ids=[id_index])

    def last_insert(self, table_name):
        """Return id of the last insert in table"""
        table_result = self._db.table(table_name)
        max_id = False
        for result in table_result:
            if result.doc_id > max_id:
                max_id = result.doc_id
        return max_id