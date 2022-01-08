import json

from model.database import Database as db


class DatabaseManager:

    def __init__(self) -> None:
        self._db = db()

    def insert_into_db(self, table, to_insert):
        """Insert in database"""
        serialize_to_insert = self.serialize_object_to_json(to_insert)
        self._db.insert(table, serialize_to_insert)
        id_create = self.last_insert(table)
        self.update(table, id_create, {'_id': id_create})

    def serialize_object_to_json(self, model):
        """"Serialize an object in JSON"""
        return json.loads(json.dumps(model, default=lambda o: o.__dict__))

    def serialize_to_json(self, string_to_single_quote):
        """Convert JSON single quote to JSON double quote"""
        return json.dumps(string_to_single_quote)

    def last_insert(self, table):
        """Return id of the last insert in table"""
        return self._db.last_insert(table)

    def search_single(self, table_name, id_to_search):
        """Return a unique value"""
        datas_table = self._db.search_table(table_name)
        data = self._db.search_single(datas_table, id_to_search)
        return self.serialize_to_json(data)

    def search_multiple(self, table_name, index_start):
        """Return a list in table from an start index"""
        data_table = self._db.search_table(table_name)

        datas = self._db.search_more(data_table, index_start)
        return [self.serialize_to_json(data) for data in datas]

    def search_where(self, table_name, key, value):
        """Return a list of value search by condition"""
        data_table = self._db.search_table(table_name)
        datas = self._db.search_where(data_table, key, value)
        return [self.serialize_to_json(data) for data in datas]

    def update(self, table_name, id_index, data_to_update):
        """Update in database"""
        datas_table = self._db.search_table(table_name)
        self._db.update(datas_table, id_index, data_to_update)
