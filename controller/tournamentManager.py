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

        new_tournament = t(specifications_new_tournament)

        self.database_manager.insert_into_db('tournament', new_tournament)

        # list_players = []

        # for player in range(new_tournament['number_players']):
        #     list_players.append(self.player_manager.add_player())

        # new_tournament['list_players'] = list_players
        # sorted_list_players = self.player_manager.sorted_players(list_players)

        # self.database_manager.add_tournament(new_tournament)
        