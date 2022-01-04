from prettytable import PrettyTable

from view.view import View as v

class StageView:

    def __init__(self) -> None:
        self.view = v()

    def print_list_stage(self, list_stage):
        table_list_stage = PrettyTable(["ID", "Round n°", "Date et heure de début", "Date et heure de fin"])
        
        for element in list_stage:
            if hasattr(element, '_datetime_start'):
                datetime_start = element._datetime_start
            else:
                datetime_start = ""
            if hasattr(element, '_datetime_end'):
                datetime_end = element._datetime_end
            else:
                datetime_end = ""

            table_list_stage.add_row([
                element._id, 
                element._number, 
                datetime_start, 
                datetime_end])

        self.except_value(table_list_stage)

    def select_stage(self):
        return self.view.input(
            "\nRenseigner l'ID d'un tour pour voir les match ou \"q\" pour revenir à la liste des tournois :\n"
            "Choix : ")

    def except_value(self, string_to_except):
        self.view.print_to_user(string_to_except)