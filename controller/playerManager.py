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

    def add_player(self, player_to_except=None) -> object:
        """Create a new player or get a player in Database"""
        statut_player = self.player_view.add_player()
        if statut_player == 1:
            return self.new_player()

        elif statut_player == 2:
            list_players = self.database_manager.search_multiple(self.TABLE_NAME, 0)
            list_players_object = []   
            for element in list_players:
                list_players_object.append(self.hydrate_object_with_json(element))

            list_to_print = []
            for player in list_players_object:
                if player._id in player_to_except or player._temp_rank != False:
                    pass
                else:
                    list_to_print.append(player)

            self.player_view.print_list_players(list_to_print)
            player = self.player_view.select_player(list_to_print)
            self.player_view.except_value(f"{player._name} {player._last_name} ajouté au tournoi !\n")
            return player
    
    def list_players(self, sorted_status):
        """List and sort players"""
        list_players = self.database_manager.search_multiple(self.TABLE_NAME, 0)
        list_players_object = [self.hydrate_object_with_json(player) for player in list_players]
        if sorted_status == 1:
            list_players_object = sorted(list_players_object, key=lambda player: player._last_name)
        elif sorted_status == 2:
            list_players_object = sorted(list_players_object, key=lambda player: player._ranking)

        self.player_view.print_list_players(list_players_object)
    
    def update_ranking(self):
        list_players = self.database_manager.search_multiple(self.TABLE_NAME, 0)
        list_players_object = [self.hydrate_object_with_json(player) for player in list_players]
        id_player = self.player_view.select_player(list_players_object)
        for player in list_players_object:
            if player._id == id_player:

                new_ranking = self.player_view.update_ranking(player)
                player._ranking = new_ranking
                self.update_player_db(player, player._id)
                self.player_view.except_value(f"{player._name} {player._last_name} mis à jour !\n")
                break

    def get_players(self, number_to_range):
        """Return a list players object"""
        list_players = []
        list_players_id = []
        for i in range(number_to_range):
            player_to_add = self.add_player(list_players_id)
            list_players.append(player_to_add)
            list_players_id.append(player_to_add._id)
        return list_players

    def get_players_from_list_id(self, list_id_players):
        """Return a list players object create from a list id"""
        list_players = []
        for id_player in list_id_players:
            list_players.append(self.hydrate_object_by_id(id_player))
        return list_players

    def generate_pairs_first_stage(self, list_players) -> list:
        """Sorted list of players by ranking and generate a pair of players"""
        p_sorted = sorted(list_players, key=lambda player: player._ranking)
        return self.generate_pairs(p_sorted)
    
    def generate_pairs_more_stage(self, list_players):
        """Sorted list of player by temp rank"""
        p_sorted = sorted(list_players, key=lambda player: player._temp_rank)
    
        for i in range(0, len(p_sorted)-1):
            if p_sorted[i]._temp_rank == p_sorted[i+1]._temp_rank and p_sorted[i]._ranking > p_sorted[i+1]._ranking:
                p_sorted[i], p_sorted[i+1] = p_sorted[i+1], p_sorted[i]
        return self.generate_pairs(p_sorted)

    def generate_pairs(self, list_players):
        lower_players = list_players[0:int(len(list_players)/2)]
        upper_players = list_players[int(len(list_players)/2):int(len(list_players))]

        list_pairs = []
        for i in range(len(lower_players)):
            list_pairs.append([lower_players[0], upper_players[0]])
            del lower_players[0], upper_players[0]

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

