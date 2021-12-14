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

            specifications_new_tournament['list_players'] = list_id_players

        new_tournament = t(specifications_new_tournament)
        self.database_manager.insert_into_db('tournament', new_tournament)
        # sorted_list_players = self.player_manager.sorted_players(list_players)
        
    def list_tournament(self) -> None:
        """List of tournaments"""
        list_tournament = self.database_manager.search_multiple('tournament', 0)
        