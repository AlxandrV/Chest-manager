from view.view import View as v
from controller.tournamentManager import TournamentManager as tm
from controller.playerManager import PlayerManager as pm

def main():
    # view = v()
    # switch_choice(view)

    # player = pm()
    # create_player(player)

    tournament = tm()
    create_tournament(tournament)

def switch_choice(view_object):
    """List of interactions choices"""
    view_object.list_choice()
    choice = view_object.choice

    if choice == 1:
        create_tournament()
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    else:
        print("\nCe choix n'est pas dans la iste !\n")
        switch_choice(view_object)

def create_tournament(tournament_manager):
    """Create a new tournament"""
    tournament_manager.new_tournament()

def create_player(player_manager):
    """Create a new player"""
    player_manager.new_player()
