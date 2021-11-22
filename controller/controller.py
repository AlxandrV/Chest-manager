from view.view import View as v
from controller.tournamentManager import TournamentManager as tm
from controller.playerManager import PlayerManager as pm

def main():
    # view = v()
    # switch_choice(view)

    # player = pm()
    # create_player(player)

    tournament = tm()

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

def create_tournament():
    """Create a new tournament"""
    new_tournament = t()

def create_player(player_manager):
    player_manager.new_player()
