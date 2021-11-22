from datetime import datetime

class Tournament:
    
    def __init__(self) -> None:
        # self._set_name()
        # self._set_place()
        # self._set_date_start()
        # self._set_date_end()
        # self._set_turn()
        self._set_time_control()
        self._set_description()

    def _set_name(self) -> None:
        self._name = str(input("Nom du tournoi : "))

    def get_name(self) -> str:
        return self._name

    def _set_place(self) -> str:
        self._place = str(input("Lieu du tournoi : "))

    def get_place(self) -> str:
        return self._place

    def _set_date_start(self) -> str:
        date_format = "%d/%m/%Y"

        try:
            date_start = str(input("Date de début (jj/mm/aaaa) : "))
            res = bool(datetime.strptime(date_start, date_format))
            self._date_start = date_start
        except ValueError as e:
            print("Format de date incorrect !\n")
            self._set_date_start()

    def get_date_start(self) -> str:
        return self._date_start

    def _set_date_end(self) -> str:
        date_format = "%d/%m/%Y"
        date_end = str(input("Date de fin (jj/mm/aaaa) : "))

        if not date_end:
            self._date_end = False

        else:
            try:
                res = bool(datetime.strptime(date_end, date_format))
                self._date_end = date_end
            except ValueError as e:
                print("Format de date incorrect !\n")
                self._set_date_end()
    
    def get_date_end(self) -> str:
        return self._date_end

    def _set_turn(self) -> None:
        turn = input("Nombre de tours (par défaut 4) : ")
        if not turn:
            self._turn = 4
        else:
            try:
                self._turn = int(turn)
            except ValueError as e:
                print("Rentrer un nombre !\n")
                self._set_turn()

    def get_turn(self) -> int:
        return self._turn

    def _set_instance(self) -> None:
        self._instance = False
    
    def get_instance(self) -> bool:
        return self._instance

    def _set_players(self) -> None:
        self._players = []
    
    def get_players(self) -> list:
        return self._players

    def _set_time_control(self) -> None:
        try:
            time_control = int(input("Choix du contrôle du temps\n"
                "1 : Bullet\n"
                "2 : Blitz\n"
                "3 : Coup rapide\n"
                "\nChoix : "))
            
            if time_control > 3:
                print("Rentrer un nombre dans la liste !\n")
                self._set_time_control()

            else:
                self._time_control = time_control

        except ValueError as e:
            print("Rentrer un nombre !\n")
            self._set_time_control()
    
    def get_time_control(self) -> int:
        return self._time_control

    def _set_description(self) -> None:
        self._description = str(input("Description :\n"))
    
    def get_description(self) -> str:
        return self._description
