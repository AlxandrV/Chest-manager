from model.player import Player as p
from view.playerView import PlayerView as pv

class PlayerManager:

    def new_player(self):
        player = p()
        player_view = pv()
        specifications_new_player = player_view.new_player()

        print(specifications_new_player)