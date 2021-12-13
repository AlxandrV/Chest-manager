import json

from model.database import Database as db

class DatabaseManager:

    def __init__(self) -> None:
        self._db = db()

    def insert_into_db(self, table, serialize_to_insert):
        self._db.insert(table, serialize_to_insert)

    def serialize_to_json(self, model):
        return json.loads(json.dumps(model, default=lambda o: o.__dict__))