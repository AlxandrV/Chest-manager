class Match:

    def __init__(self, specifications) -> None:
        if '_id' in specifications:
            self._id = specifications['_id']
        self._number = specifications['_number']
        self._id_stage = specifications['_id_stage']
        self._id_players = specifications['_id_players']
        if '_id_winner' in specifications:
            self._id_winner = specifications['_id_winner']

    def set_player_winner(self, player_winner):
        self.player_winner = player_winner

    def get_player_winner(self) -> object:
        return self.player_winner

    def _set_stage_number(self, stage_number):
        try:
            int(stage_number)
            self.stage_number = stage_number

        except ValueError as e:
            print("Le numéro du tours doit être un entier !")

    def get_stage_number(self) -> int:
        return self.stage_number

    def _set_match_number(self, match_number):
        try:
            int(match_number)
            self.match_number = match_number

        except ValueError as e:
            print("Le numéro du match doit être un entier !")


    def get_match_number(self) -> int:
        return self.match_number

    def _set_palyers(self, list_two_players):
        if isinstance(list_two_players, list):
            self.players = list_two_players
        else:
            print("Les joueurs doit être une liste !")

    def get_players(self) -> list:
        return self.players