from view.view import View as v
from controller.tournamentManager import TournamentManager as tm
from controller.playerManager import PlayerManager as pm

class Controller:

    def run(self):
        self.main()

    def main(self):
        # view = v()
        # switch_choice(view)

        player = pm()
        self.create_player(player)

        # tournament = tm()
        # self.create_tournament(tournament)

    def switch_choice(self,view_object):
        """List of interactions choices"""
        view_object.list_choice()
        choice = view_object.choice

        if choice == 1:
            self.create_tournament()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        else:
            print("\nCe choix n'est pas dans la iste !\n")
            self.switch_choice(view_object)

    def create_tournament(self,tournament_manager):
        """Create a new tournament"""
        tournament_manager.new_tournament()

    def create_player(self, player_manager):
        """Create a new player"""
        player_manager.new_player()
