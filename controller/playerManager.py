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
        self.player_view.except_value(f"Joueur {player._name} {player._last_name} créé !\n")

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
    
    def list_players(self):
        list_players = self.database_manager.search_multiple(self.TABLE_NAME, 0)
        list_players_object = [self.hydrate_object_with_json(player) for player in list_players]
        self.player_view.print_list_players(list_players_object)
    
    def update_ranking(self):
        list_players = self.database_manager.search_multiple(self.TABLE_NAME, 0)
        list_players_object = [self.hydrate_object_with_json(player) for player in list_players]
        id_player = self.player_view.select_player()
        for player in list_players_object:
            if player._id == id_player:

                new_ranking = self.player_view.update_ranking(player)
                player._ranking = new_ranking
                self.update_player_db(player, player._id)
                self.player_view.except_value(f"{player._name} {player._last_name} mis à jour !\n")
                break

    def get_players(self, number_to_range):
        """Return a list players object"""
        list_id_players = []
        for player in range(number_to_range):
            new_player = self.add_player()
            list_id_players.append(new_player)
        return list_id_players

    def get_players_in_stage(self, list_id_players):
        list_players = []
        for id_player in list_id_players:
            list_players.append(self.hydrate_object_by_id(id_player))
        return list_players

    def generate_pairs(self, list_players) -> list:
        """Sorted list of players by ranking and generate a pair of players"""
        all_players_sorted = sorted(list_players, key=lambda player: player._ranking)
        lower_player = all_players_sorted[0:int(len(all_players_sorted)/2)]
        upper_players = all_players_sorted[int(len(all_players_sorted)/2):int(len(all_players_sorted))]

        list_pairs = []
        for i in range(int(len(lower_player)/2)):
            list_pairs.append([lower_player[0], lower_player[-1]])
            del lower_player[0], lower_player[-1]

        for i in range(int(len(upper_players)/2)):
            list_pairs.append([upper_players[0], upper_players[-1]])
            del upper_players[0], upper_players[-1]

        return list_pairs

    def hydrate_object_with_json(self, json_to_hydrate):
        """Hydrate an object with a JSON"""
        return json.loads(json_to_hydrate, object_hook=p)

    def hydrate_object_by_id(self, id_player):
        """Search player by id"""
        json_player = self.database_manager.search_single(self.TABLE_NAME, id_player)
        return self.hydrate_object_with_json(json_player)

    def update_player_db(self, object_to_update, id_to_object):
        """Update a player in database"""
        datas_serialize = self.database_manager.serialize_object_to_json(object_to_update)
        self.database_manager.update(self.TABLE_NAME, id_to_object, datas_serialize)

