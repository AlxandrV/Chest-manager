class Match:

    def __init__(self, specifications) -> None:
        if '_id' in specifications:
            self._id = specifications['_id']
        self._number = specifications['_number']
        self._id_stage = specifications['_id_stage']
        self._id_players = specifications['_id_players']
        if '_id_winner' in specifications:
            self._id_winner = specifications['_id_winner']
