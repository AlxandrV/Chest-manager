from prettytable import PrettyTable
from model.player import Player

from view.view import View as v

class MatchView:

    def __init__(self) -> None:
        self.view = v()

    def play_match(self, match, list_player):
        """Print detail of a match"""
        self.view.print_to_user(f"\nMatch n°{match._number}, renseigner l'ID du gagnant(e), si égalité rentrer \"nulle\"")
        match_descr = PrettyTable(["ID", "Prénom", "Nom"])
        list_id = []
        for player in list_player:
            list_id.append(player._id)
            match_descr.add_row([player._id, player._name, player._last_name])
        self.view.print_to_user(match_descr)
        winner = self.view.input("\nGagnant(e) : ")
        
        if winner in str(list_id):
            return winner
        elif winner == "nulle":
            return winner
        else:
            self.view.print_to_user("\nRenseigner un ID dans la liste ou \"nulle\" si égalité")
            return self.play_match(match, list_player)

    def except_value(self, string_to_except):
        self.view.print_to_user(string_to_except)
