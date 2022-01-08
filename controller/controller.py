from view.view import View as v
from controller.tournamentManager import TournamentManager as tm
from controller.playerManager import PlayerManager as pm

class Controller:

    def __init__(self) -> None:
        self.tournament_manager = tm()
        self.player_manager = pm()
        self._view = v()

    def run(self):
        self.main()

    def main(self):
        self.switch_choice()

    def switch_choice(self):
        """List of interactions choices"""
        choice = self._view.list_choice()

        if choice == 1:
            self.player_choice(0)
        elif choice == 2:
            self.tournament_choice()
        elif choice == 3:
            self.launch_stage_tournament()
        elif choice == 4:
            self.close_stage()
        else:
            self._view.print_to_user("\nCe choix n'est pas dans la iste !\n")
            self.switch_choice()
        self.switch_choice()

    def player_choice(self, sorted_status):
        """List chooice for players interactions"""
        self.list_players(sorted_status)
        choice = self._view.player_choice()
        if choice == "1":
            self.create_player()
        elif choice == "2":
            self.update_ranking()
        elif choice == "3":
            self.player_choice(1)
        elif choice == "4":
            self.player_choice(2)
        elif choice == "q":
            self.switch_choice()
        else:
            self._view.print_to_user("\nCe choix n'est pas dans la iste !\n")
            self.player_choice(0)

    def list_players(self, sorted_status):
        self.player_manager.list_players(sorted_status)

    def update_ranking(self):
        self.player_manager.update_ranking()

    def create_player(self):
        """Create a new player"""
        self._view.print_to_user("\nCréation d'un nouveau joueur :\n")
        self.player_manager.new_player()

    def tournament_choice(self):
        """List of tournaments"""
        self.tournament_manager.list_tournament()
        choice = self._view.tournament_choice()
        if choice == "1":
            self.create_tournament()
        elif choice == "2":
            self.tournament_report()
        elif choice == "q":
            self.switch_choice()
        else:
            self._view.print_to_user("\nCe choix n'est pas dans la iste !\n")
            self.player_choice(0)

    def create_tournament(self):
        """Create a new tournament"""
        self.tournament_manager.new_tournament()
        self.switch_choice()

    def tournament_report(self):
        self.tournament_manager.tournament_report()
    
    def launch_stage_tournament(self):
        """Launch a tournament"""
        bool_result = self.tournament_manager.launch_stage_tournament()
        if bool_result == False:
            self.main()

    def close_stage(self):
        self.tournament_manager.close_stage_of_tournament()