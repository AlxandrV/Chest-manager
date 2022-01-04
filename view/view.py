class View:

    def list_choice(self) -> None:
        try:
            input_choice = int(input(
                "\nQue voulez-vous faire :\n"
                "1 : Joueurs\n"
                "2 : Tournois\n"
                "3 : Lancer le tour d'un tournoi\n"
                "4 : Terminer le tour d'un tournoi et rentrer les résultats\n"
                "\nChoix : "))
            return input_choice

        except ValueError as e:
            print("\nVeuillez rentrer un nombre parmis la liste, merci !\n")
            self.list_choice()

    def player_choice(self):
        return input(
            "\nQue voulez-vous faire :\n"
            "1 : Ajouter un nouveau joueur\n"
            "2 : Modifer le rang d'un joueur\n"
            "q : Retour au menu principale"
            "\nChoix : ")

    def tournament_choice(self):
        return input(
            "\nQue voulez-vous faire :\n"
            "1 : Créer un nouveau tournoi\n"
            "2 : Rapport de tournoi déjà joué\n"
            "q : Retour au menu principale"
            "\nChoix : ")
        
    def input(self, string_to_input) -> str:
        return input(string_to_input)

    def print_to_user(self, string_to_print) -> None:
        print(string_to_print)