from datetime import datetime
from prettytable import PrettyTable


from view.view import View as v

class TournamentView:
    
    def __init__(self) -> None:
        self.view = v()
    
    def new_tournament(self) -> dict:
        self.view.print_to_user("\nCréation d'un nouveau tournoi !")
        specifications = {}
        specifications['_name'] = self.name()
        specifications['_place'] = self.place()
        specifications['_date_start'] = self.date_start()
        specifications['_date_end'] = self.date_end()
        specifications['_stage'] = self.stage()
        specifications['_time_control'] = self.time_control()
        specifications['_description'] = self.description()
        specifications['_number_players'] = self.number_players()
        return specifications

    def name(self) -> str:
        return self.view.input("\nNom : ")

    def place(self) -> str:
        return self.view.input("\nLieu : ")

    def date_start(self) -> str:
        date_start = self.view.input("\nDate de début (jj/mm/aaaa) : ")
        date_format = "%d/%m/%Y"
        try:
            res = bool(datetime.strptime(date_start, date_format))
            return date_start
        except ValueError as e:
            self.view.print_to_user("\nFormat de date incorrect !\n")
            return self.date_start()

    def date_end(self) -> str:
        date_end = self.view.input("\nDate de fin (jj/mm/aaaa) : ")
        date_format = "%d/%m/%Y"
        try:
            res = bool(datetime.strptime(date_end, date_format))
            return date_end
        except ValueError as e:
            self.except_value("\nFormat de date incorrect !\n")
            return self.date_end()

    def stage(self, number_stage=4) -> int:
        stage = self.view.input("\nNombre de tours (par défaut 4) : ")

        if not stage:
            return number_stage
        else:
            try:
                if number_stage < 1:
                    self.except_value("\nLe nombre de tours minimum est de 1 !\n")
                    return self.stage()
                else:
                    return int(stage)
            except ValueError as e:
                self.except_value("\nRentrer un nombre !\n")
                return self.stage()

    def time_control(self) -> int:
        time_control = self.view.input("\nType de contrôle du temps :\n"
            "1 : Bullet\n"
            "2 : Blitz\n"
            "3 : Coup rapide\n"
            "\nChoix : ")
        try:
            time_control = int(time_control)
            if time_control >= 1 and time_control <= 3:
                return time_control
            else:
                self.except_value("\nRentrer un nombre dans liste !\n")
                return self.time_control()
        except ValueError as e:
                self.except_value("\nRentrer un nombre !\n")
                return self.time_control()

    def description(self) -> str:
        return self.view.input("\nDescription : ")

    def number_players(self, number_players=8) -> int:
        players = self.view.input("\nNombres de joueurs (par défaut 8) : ")
        if not players:
            return number_players
        else:
            try:
                players = int(players)
                if players < 2:
                    self.except_value("\nLe tournoi doit comporter au moins 2 joueurs !\n")
                    return self.number_players()
                elif players >= 0 and (players % 2) != 0 :
                    self.except_value("\nLe nombre de joueurs doit être paire !\n")
                    return self.number_players()
                else:
                    return players
            except ValueError as e:
                self.except_value("\nRenseigner un nombre !\n")
                return self.number_players()

    def create_players(self) -> int:
        create_or_not = self.view.input("\nVoulez-vous ajouter les joueurs maintenant ?\n"
            "1 : Oui\n"
            "2 : Non\n"
            "\nChoix : ")
        try:
            create_or_not = int(create_or_not)
            if create_or_not == 1 or create_or_not == 2:
                return create_or_not
            else:
                self.except_value("\nVeuillez choisir un nombre dans la liste !\n")
                return self.create_players()
        except ValueError as e:
                self.except_value("\nVeuillez choisir un nombre dans la liste !\n")
                return self.create_players()

    def launch_stage_tournament(self) -> None:
        return self.view.input("\nID du tournoi ou \"q\" pour revenir au menu principale : ")
        
    def print_list_tournament_in_progess(self, list_tournament):
        table_list_tournament = PrettyTable(["ID", "Nom", "Lieu", "Date début", "Date fin", "Contrôle du temps", "Status", "Round joué", "Description"])
        for element in list_tournament:
            if element._time_control == 1:
                time_control = "Bullet"
            elif element._time_control == 2:
                time_control = "Blitz"
            elif element._time_control == 3:
                time_control = "Coup rapide"
            else:
                time_control = "Error"

            if element._status == 0:
                status = "Non joué"
            elif element._status == 1:
                status = "En cours"
            else:
                status = "Terminé"

            table_list_tournament.add_row([
                element._id, 
                element._name, 
                element._place, 
                element._date_start, 
                element._date_end,
                time_control,
                status,
                element._stage_in_progress,
                element._description])
        self.except_value(table_list_tournament)   

    def except_value(self, string_to_except):
        self.view.print_to_user(string_to_except)
        