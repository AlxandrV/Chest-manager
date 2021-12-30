import json

from prettytable import PrettyTable

from model.tournament import Tournament as t
from controller.databaseManager import DatabaseManager as dbm
from view.tournamentView import TournamentView as tv
from controller.playerManager import PlayerManager as pm

class TournamentManager:

    def __init__(self) -> None:
        self.tournament_view = tv()
        self.player_manager = pm()
        self.database_manager = dbm()
    
    def new_tournament(self) -> None:
        """Creat a new tournament"""
        specifications_new_tournament = self.tournament_view.new_tournament()

        create_players = self.tournament_view.create_players()

        if create_players == 1:
            list_id_players = []

            for player in range(specifications_new_tournament['number_players']):
                new_player = self.player_manager.add_player()
                list_id_players.append(self.database_manager.last_insert('player'))

            specifications_new_tournament['_list_players'] = list_id_players

        new_tournament = t(specifications_new_tournament)
        self.database_manager.insert_into_db('tournament', new_tournament)
        # sorted_list_players = self.player_manager.sorted_players(list_players)
        
    def list_tournament(self) -> None:
        """List of tournaments"""
        list_tournament = self.database_manager.search_multiple('tournament', 0)

        table_list_tournament = PrettyTable(["ID", "Nom", "Lieu", "Date début", "Date fin"])
        
        for element in list_tournament:
            tournament = self.hydrate_object_with_json(element)
            table_list_tournament.add_row([tournament._id, tournament._name, tournament._place, tournament._date_start, tournament._date_end])

        self.tournament_view.get_tournament(table_list_tournament)

    def launch_tournament(self) -> None:
        id_tournament_to_launch = self.tournament_view.launch_tournament()
        tournament = self.database_manager.search_single("tournament", id_tournament_to_launch)

        if tournament == None:
            self.tournament_view.except_value("\nID incorrect !\n")
            return False

        tournament_object = self.hydrate_object_with_json(tournament)

        if self.has_attribute(tournament_object, '_list_players') == False:
            print('pas de joueurs')

    def hydrate_object_with_json(self, json_to_hydrate):
        return json.loads(json_to_hydrate, object_hook=t)

    def has_attribute(self, object_with_attr, nam_attr):
        if hasattr(object_with_attr, nam_attr):
            return True
        else:
            return False