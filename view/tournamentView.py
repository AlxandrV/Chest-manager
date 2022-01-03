from datetime import datetime
from prettytable import PrettyTable


from view.view import View as v

class TournamentView:
    
    def __init__(self) -> None:
        self.view = v()
    
    def new_tournament(self) -> dict:
        self.view.print_to_user("Création d'un nouveau tournoi !")
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
        return self.view.input("Nom : ")

    def place(self) -> str:
        return self.view.input("Lieu : ")

    def date_start(self) -> str:
        date_start = self.view.input("Date de début (jj/mm/aaaa) : ")
        date_format = "%d/%m/%Y"

        try:
            res = bool(datetime.strptime(date_start, date_format))
            return date_start
            
        except ValueError as e:
            self.view.print_to_user("Format de date incorrect !\n")
            return self.date_start()


    def date_end(self) -> str:
        date_end = self.view.input("Date de fin (jj/mm/aaaa) : ")
        date_format = "%d/%m/%Y"

        try:
            res = bool(datetime.strptime(date_end, date_format))
            return date_end

        except ValueError as e:
            self.view.print_to_user("Format de date incorrect !\n")
            return self.date_end()

    
    def stage(self, number_stage=4) -> int:
        stage = self.view.input("Nombre de tours (par défaut 4) : ")

        if not stage:
            return number_stage

        else:
            try:
                if number_stage < 1:
                    self.view.print_to_user("Le nombre de tours minimum est de 1 !")
                    return self.stage()
                
                else:
                    return int(stage)

            except ValueError as e:
                self.view.print_to_user("Rentrer un nombre !\n")
                return self.stage()

    def time_control(self) -> int:
        time_control = self.view.input("Type de contrôle du temps :\n"
            "1 : Bullet\n"
            "2 : Blitz\n"
            "3 : Coup rapide\n"
            "\nChoix : ")
        
        try:
            time_control = int(time_control)
            if time_control >= 1 and time_control <= 3:
                return time_control

            else:
                self.view.print_to_user("Rentrer un nombre dans liste !")
                return self.time_control()

        except ValueError as e:
                self.view.print_to_user("Rentrer un nombre !")
                return self.time_control()

    def description(self) -> str:
        return self.view.input("Description : ")

    def number_players(self, number_players=8) -> int:
        players = self.view.input("Nombres de joueurs (par défaut 8) : ")

        if not players:
            return number_players

        else:
            try:
                players = int(players)

                if players < 2:
                    self.view.print_to_user("Le tournoi doit comporter au moins 2 joueurs !")
                    return self.number_players()

                elif players >= 0 and (players % 2) != 0 :
                    self.view.print_to_user("Le nombre de joueurs doit être paire !")
                    return self.number_players()

                else:
                    return players

            except ValueError as e:
                self.view.print_to_user("Renseigner un nombre !")
                return self.number_players()

    def create_players(self) -> int:
        create_or_not = self.view.input("Voulez-vous ajouter les joueurs maintenant ?\n"
            "1 : Oui\n"
            "2 : Non\n"
            "\nChoix : ")

        try:
            create_or_not = int(create_or_not)
            if create_or_not == 1 or create_or_not == 2:
                return create_or_not

            else:
                self.view.print_to_user("Veuillez choisir un nombre dans la liste !")
                return self.create_players()

        except ValueError as e:
                self.view.print_to_user("Veuillez choisir un nombre dans la liste !")
                return self.create_players()

    def launch_stage_tournament(self) -> None:
        id_tournament = self.view.input("Renseigner l'ID du tournoi à lancer : ")

        try:
            return int(id_tournament)
    
        except ValueError as e:
            self.view.print_to_user("Rentrer un nombre !")
            return self.launch_stage_tournament()

    def print_list_tournament(self, list_tournament):
        table_list_tournament = PrettyTable(["ID", "Nom", "Lieu", "Date début", "Date fin", "Contrôle du temps", "Status"])
        
        for element in list_tournament:
            if element._time_control == 1:
                time_control = "Bullet"
            elif element._time_control == 2:
                time_control = "Blitz"
            elif element._time_control == 3:
                time_control == "Coup rapide"
            else:
                time_control = "Error"

            if element._status == 0:
                status = "Non joué"
            elif element._status == 1:
                status = "En cours"
            else:
                status = "Déjà joué"

            table_list_tournament.add_row([
                element._id, 
                element._name, 
                element._place, 
                element._date_start, 
                element._date_end,
                time_control,
                status])

        self.except_value(table_list_tournament)   

    def except_value(self, string_to_except):
        self.view.print_to_user(string_to_except)
        