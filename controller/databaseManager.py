import json

from model.database import Database as db

class DatabaseManager:

    def __init__(self) -> None:
        self._db = db()

    def add_tournament(self, new_tournament):
        self._db.insert(0, new_tournament)

    def serialize_to_json(self, model):
        return json.loads(json.dumps(model, default=lambda o: o.__dict__))