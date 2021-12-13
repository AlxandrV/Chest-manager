from model.database import Database as db

class DatabaseManager:

    def __init__(self) -> None:
        self._db = db()

    def add_tournament(self, new_tournament):
        self._db.insert(0, new_tournament)