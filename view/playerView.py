from datetime import datetime

from view.view import View as v

class PlayerView:

    def __init__(self) -> None:
        self.view = v()
    
    def new_player(self) -> dict:
        """Create specification of a new player"""
        specifications = {}

        name = self.name()
        specifications['_name'] = name

        lastname = self.lastname()
        specifications['_last_name'] = lastname

        birthday = self.birthday()
        specifications['_birthday'] = birthday

        gender = self.gender()
        specifications['_gender'] = gender

        specifications['_ranking'] = 0

        return specifications

    def add_player(self) -> int:
        """Choice for create a new player or get a player in database"""
        try:
            choice = int(self.view.input(
                "1 : Créer un nouveau joueur\n"
                "2 : Joueur déjà existant\n"
                "Choix : "))
            
            if choice >= 1 and choice <= 2:
                return choice
            
            else:
                print("\nChoissisez un nombre dans la liste !")
                return self.add_player()
        
        except ValueError as e:
            print("\nSaisissez un nombre !")
            return self.add_player()

    def name(self, string_to_input="Prénom : "):
        """Set a name of a player"""
        return self.view.input(string_to_input)

    def lastname(self, string_to_input="Nom : "):
        """Set a lastname of a player"""
        return self.view.input(string_to_input)

    def birthday(self, string_to_input="Date de naissance (jj/mm/aaaa) : "):
        """Set a birthday of a player"""
        birthday = self.view.input(string_to_input)
        date_format = "%d/%m/%Y"

        try:
            res = bool(datetime.strptime(birthday, date_format))
            return birthday
        except ValueError as e:
            print("Format de date incorrect !\n")
            return self.birthday()


    def gender(self, string_to_input="Sexe\n1 : M\n2 : F\n3 : Autre\nSaisir un nombre : ", choice=3):
        """Set a gender of a player"""
        gender = self.view.input(string_to_input)

        try:
            gender = int(gender)

            if gender > choice or gender <= 0:
                print(f"Veuillez choisir un nombre dans la liste !")
                return self.gender()
            else:
                return gender

        except ValueError as e:
            print(f"Veuillez choisir un nombre dans la liste !")
            return self.gender()

    def select_player(self, string_to_input="ID du joueur : "):
        try:
            return int(self.view.input(string_to_input))
        except ValueError as e:
            self.view.print_to_user("Saisissez un nombre !")
            return self.select_player()

    def except_value(self, string_to_except):
        self.view.print_to_user(string_to_except)
