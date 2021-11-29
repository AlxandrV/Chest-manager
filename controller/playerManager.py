from model.player import Player as p
from view.playerView import PlayerView as pv

class PlayerManager:

    def __init__(self) -> None:
        self.player_view = pv()

    def new_player(self) -> object:
        """Create a new model player"""
        specifications_new_player = self.player_view.new_player()
        specifications_new_player['ranking'] = 0
        return p(specifications_new_player)

    def add_player(self) -> object:
        """Create a new player or get a player in Database"""
        statut_player = self.player_view.add_player()

        if statut_player == 1:
            return self.new_player()

        elif statut_player == 2:
            print("pas de joueur en bdd pour le moment")
