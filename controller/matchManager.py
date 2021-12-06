from model.match import Match as m

class MatchManager:

    def create_match(self, stage_number, match_number, list_two_players, player_winner=None):
        return m(stage_number, match_number, list_two_players, player_winner)