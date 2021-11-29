from model.tournament import Tournament as t
from view.tournamentView import TournamentView as tv

class TournamentManager:
    
    def new_tournament(self) -> None:
        tournament_view = tv()
        new_tournament = tournament_view.new_tournament()