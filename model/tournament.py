from datetime import datetime

class Tournament:
    
    def __init__(self, specifications) -> None:
        if '_id' in specifications:
            self._set_id(specifications['_id'])
        self._set_name(specifications['_name'])
        self._set_place(specifications['_place'])
        self._set_date_start(specifications['_date_start'])
        self._set_date_end(specifications['_date_end'])
        self._set_stage(specifications['_id_stage'])
        self._set_time_control(specifications['_time_control'])
        self._set_description(specifications['_description'])
        self._set_number_players(specifications['_number_players'])
        if '_list_players' in specifications:
            self._set_list_players(specifications['_list_players'])
        if '_status' in specifications:
            self._status = specifications['_status']
        else:
            self.status = False


    def _set_id(self, id) -> None:
        self._id = int(id)

    def get_id(self) -> str:
        return self._id

    def _set_name(self, name) -> None:
        self._name = str(name)

    def get_name(self) -> str:
        return self._name

    def _set_place(self, place) -> str:
        self._place = str(place)

    def get_place(self) -> str:
        return self._place

    def _set_date_start(self, date_start) -> str:
        date_format = "%d/%m/%Y"

        try:
            try_date_start = str(date_start)
            res = bool(datetime.strptime(try_date_start, date_format))
            self._date_start = try_date_start
        except ValueError as e:
            print("Format de date incorrect !\n")

    def get_date_start(self) -> str:
        return self._date_start

    def _set_date_end(self, date_end) -> str:
        date_format = "%d/%m/%Y"

        try:
            try_date_end = str(date_end)
            res = bool(datetime.strptime(date_end, date_format))
            self._date_end = try_date_end
        except ValueError as e:
            print("Format de date incorrect !\n")
    
    def get_date_end(self) -> str:
        return self._date_end

    def _set_stage(self, turn) -> None:
        try:
            self._id_stage = list(turn)
        except ValueError as e:
            print("Format des tours incorrect !\n")

    def get_stage(self) -> int:
        return self._id_stage

    # def _set_instance(self) -> None:
    #     self._instance = False
    
    # def get_instance(self) -> bool:
    #     return self._instance

    def _set_players(self, players_id) -> None:
        self._players_id = list(players_id)
    
    def get_players(self) -> list:
        return self._players_id

    def _set_time_control(self, time_control) -> None:
        self._time_control = time_control
    
    def get_time_control(self) -> int:
        return self._time_control

    def _set_description(self, description) -> None:
        self._description = str(description)
    
    def get_description(self) -> str:
        return self._description

    def _set_number_players(self, number_players) -> None:
        self._number_players = int(number_players)

    def _set_list_players(self, list_players):
        self._list_players = list(list_players)
