from model.player import Player as p
from view.playerView import PlayerView as pv

class PlayerManager:

    def new_player(self) -> object:
        player_view = pv()
        specifications_new_player = player_view.new_player()
        specifications_new_player['ranking'] = 0
        return p(specifications_new_player)
