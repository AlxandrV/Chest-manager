import json
from prettytable import PrettyTable

from model.player import Player as p
from view.playerView import PlayerView as pv
from controller.databaseManager import DatabaseManager as dm

class PlayerManager:

    def __init__(self) -> None:
        self.player_view = pv()
        self.database_manager = dm()
        self.TABLE_NAME = "player"

    def new_player(self) -> object:
        """Create a new model player"""
        specifications_new_player = self.player_view.new_player()
        player =  p(specifications_new_player)
        self.database_manager.insert_into_db(self.TABLE_NAME, player)

    def add_player(self) -> object:
        """Create a new player or get a player in Database"""
        statut_player = self.player_view.add_player()

        if statut_player == 1:
            return self.new_player()

        elif statut_player == 2:
            list_players = self.database_manager.search_multiple(self.TABLE_NAME, 0)
            table_list_players = PrettyTable(["ID", "Prénom", "Nom", "Date de naissance"])
        
            for element in list_players:
                player = self.hydrate_object_with_json(element)
                table_list_players.add_row([
                    player._id, 
                    player._name,
                    player._last_name,
                    player._birthday])

            self.player_view.except_value(table_list_players)
            id_player = self.player_view.select_player()
            player_to_add = self.hydrate_object_with_json(self.database_manager.search_single("player", id_player))
            self.player_view.except_value(f"{player_to_add._name} {player_to_add._last_name} ajouté au tournoi !\n")
            return player_to_add

    def list_players(self, number_to_range):
        """Return a list players object"""
        list_id_players = []
        for player in range(number_to_range):
            new_player = self.player_manager.add_player()
            list_id_players.append(new_player)
        return list_id_players


    def sorted_players(self, list_players) -> list:
        """Sorted list of players by ranking"""
        # for player in list_players:
        #     print(player._name)
        return sorted(list_players, key=lambda player: player._ranking)

    def hydrate_object_with_json(self, json_to_hydrate):
        return json.loads(json_to_hydrate, object_hook=p)

    def hydrate_object_by_id(self, id_player):
        json_player = self.database_manager.search_single(self.TABLE_NAME, id_player)
        return self.hydrate_object_with_json(json_player)
