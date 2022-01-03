class View:

    def list_choice(self) -> None:
        try:
            input_choice = int(input(
                "Que voulez-vous faire :\n"
                "1 : Créer un nouveau tournoi\n"
                "2 : Créer un nouveau joueur\n"
                "3 : Consulter la liste de tous les tournois\n"
                "4 : Consulter la liste des joueurs\n"
                "5 : Lancer le tour d'un tournoi\n"
                "6 : Terminer le tour d'un tournoi et rentrer les résultats\n"
                "\nChoix : "))
            self.choice = input_choice

        except ValueError as e:
            print("\nVeuillez rentrer un nombre parmis la liste, merci !\n")
            self.list_choice()
        
    def input(self, string_to_input) -> str:
        return input(string_to_input)

    def print_to_user(self, string_to_print) -> None:
        print(string_to_print)