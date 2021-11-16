class View:

    def list_choice(self) -> None:
        try:
            input_choice = int(input("Que voulez-vous faire :\n"
                "1 : Créer un nouveau tournoi\n"
                "2 : Consulter la liste des tournois déjà joués\n"
                "3 : Consulter la liste des joueurs\n"
                "\nChoix : "))
            self.choice = input_choice

        except ValueError as e:
            print("\nVeuillez rentrer un nombre parmis la liste, merci !\n")
            self.list_choice()
        
