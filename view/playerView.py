from datetime import datetime

from view.view import View as v


class PlayerView:

    def __init__(self) -> None:
        self.view = v()

    def new_player(self) -> dict:
        specifications = {}

        name = self.name()
        specifications['name'] = name

        lastname = self.lastname()
        specifications['lastname'] = lastname

        birthday = self.birthday()
        specifications['birthday'] = birthday

        gender = self.gender()
        specifications['gender'] = gender

        return specifications

    def name(self, string_to_input="Prénom : "):
        return self.view.input(string_to_input)

    def lastname(self, string_to_input="Nom : "):
        return self.view.input(string_to_input)

    def birthday(self, string_to_input="Date de naissance (jj/mm/aaaa) : "):
        birthday = self.view.input(string_to_input)
        date_format = "%d/%m/%Y"

        try:
            bool(datetime.strptime(birthday, date_format))
            return birthday
        except ValueError:
            print("Format de date incorrect !\n")
            return self.birthday()

    def gender(self, choice=3):
        gender = self.view.input(
            "Sexe\n1 : M\n2 : F\n3 : Autre\nSaisir un nombre : "
            )
        try:
            gender = int(gender)
            if gender > choice or gender <= 0:
                print("Veuillez choisir un nombre dans la liste !")
                return self.gender()
            else:
                return gender
        except ValueError:
            print("Veuillez choisir un nombre dans la liste !")
            return self.gender()
