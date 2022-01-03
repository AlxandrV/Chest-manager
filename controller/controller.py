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
        self._view.list_choice()
        choice = self._view.choice

        if choice == 1:
            self.create_tournament()
        elif choice == 2:
            print("Ajout de joueur à venir...")
        elif choice == 3:
            self.list_tournament()
        elif choice == 4:
            print("Liste des joueurs à venir...")
        elif choice == 5:
            self.launch_tournament()
        elif choice == 6:
            self.close_stage()
        else:
            print("\nCe choix n'est pas dans la iste !\n")
            self.switch_choice()
        self.switch_choice()

    def create_tournament(self):
        """Create a new tournament"""
        self.tournament_manager.new_tournament()
        self.switch_choice()

    def create_player(self, player_manager):
        """Create a new player"""
        player_manager.new_player()

    def list_tournament(self):
        """List of tournaments"""
        self.tournament_manager.list_tournament()
    
    def launch_tournament(self):
        """Launch a tournament"""
        bool_result = self.tournament_manager.launch_tournament()
        if bool_result == False:
            self.main()

    def close_stage(self):
        self.tournament_manager.close_stage_of_tournament()