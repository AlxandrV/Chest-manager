from tinydb import TinyDB, Query
import os

class Database:

    def __init__(self) -> None:
        self._db = TinyDB('db.json')
        self._table_tournament = self._db.table('tournament')

    def insert(self, table, to_insert):
        if table == 0:
            self._table_tournament.insert(to_insert)

    def search(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass