from model.tournament import Tournament as t
from view.tournamentView import TournamentView as tv
from controller.playerManager import PlayerManager as pm

class TournamentManager:

    def __init__(self) -> None:
        self.tournament_view = tv()
        self.player_manager = pm()
    
    def new_tournament(self) -> None:
        """Creat a new tournament"""
        new_tournament = self.tournament_view.new_tournament()

        list_players = []

        for player in range(new_tournament['number_players']):
            list_players.append(self.player_manager.add_player())

        sorted_list_players = self.player_manager.sorted_players(list_players)

        list_match = []
        
        print(sorted_list_players[0].get_ranking())
