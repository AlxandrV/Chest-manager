import json

from model.database import Database as db

class DatabaseManager:

    def __init__(self) -> None:
        self._db = db()

    def insert_into_db(self, table, to_insert):
        """Insert in database"""
        serialize_to_insert = self.serialize_to_json(to_insert)
        self._db.insert(table, serialize_to_insert)

    def serialize_to_json(self, model):
        """"Serialize an object in JSON"""
        return json.loads(json.dumps(model, default=lambda o: o.__dict__))

    def last_insert(self, table):
        """Return id of the last insert in table"""
        return self._db.last_insert(table)

    def search_multiple(self, table_name, index_start):
        data_table = self._db.search_table(table_name)
        
        return self._db.search_more(data_table, index_start)