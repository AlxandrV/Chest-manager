from view.view import View as v

class PlayerView:

    def __init__(self) -> None:
        self.view = v()
    
    def new_player(self):
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

    def name(self, string_to_input="Nom : "):
        return self.view.input(string_to_input)

    def lastname(self, string_to_input="Prénom : "):
        return self.view.input(string_to_input)

    def birthday(self, string_to_input="Date de naissance (jj/mm/aaaa) : "):
        return self.view.input(string_to_input)

    def gender(self, string_to_input="Sexe\n1 : M\n2 : F\n3 : Autre\nSaisir un nombre : "):
        return self.view.input(string_to_input)
