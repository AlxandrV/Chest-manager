from datetime import datetime

class Player:
    
    def __init__(self) -> None:
        # self._set_name()
        # self._set_last_name()
        # self._set_birthday()
        # self._set_ranking()
        print("coucou")

    def _set_name(self, name) -> None:
        self._name = str(name)

    def get_name(self) -> str:
        return self._name

    def _set_last_name(self, last_name) -> None:
        self._last_name = str(last_name)

    def get_name(self) -> str:
        return self._last_name

    def _set_birthday(self, birthday) -> None:
        date_format = "%d/%m/%Y"

        try:
            res = bool(datetime.strptime(birthday, date_format))
            self._birthday = birthday
        except ValueError as e:
            print("Format de date incorrect !\n")
            self._set_birthday()

    def get_name(self) -> str:
        return self._birthday

    def _set_gender(self, gender) -> None:
        try:
            self._gender = int(gender)
        except ValueError as e:
            print

    def get_gender(self) -> int:
        return self._gender

    def _set_ranking(self, ranking) -> None:
        self._ranking = int(ranking)

    def get_ranking(self) -> int:
        return self._ranking
