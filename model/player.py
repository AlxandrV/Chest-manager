from datetime import datetime

class Player:
    
    def __init__(self, specification) -> None:
        self._set_name(specification['name'])
        self._set_last_name(specification['lastname'])
        # self._set_birthday(specification['birthday'])
        self._set_ranking(specification['ranking'])

    def _set_name(self, name) -> None:
        """Setter name"""
        self._name = str(name)

    def get_name(self) -> str:
        """Getter name"""
        return self._name

    def _set_last_name(self, last_name) -> None:
        """Setter lastname"""
        self._last_name = str(last_name)

    def get_name(self) -> str:
        """Getter lastname"""
        return self._last_name

    def _set_birthday(self, birthday) -> None:
        """Setter birthday"""
        date_format = "%d/%m/%Y"

        try:
            res = bool(datetime.strptime(birthday, date_format))
            self._birthday = birthday
        except ValueError as e:
            print("Format de date incorrect !\n")

    def get_birthday(self) -> str:
        """Getter birthday"""
        return self._birthday

    def _set_gender(self, gender) -> None:
        """Setter gender"""
        try:
            self._gender = int(gender)
        except ValueError as e:
            print("Valeur incorrect !\n")

    def get_gender(self) -> int:
        """Getter gender"""
        return self._gender

    def _set_ranking(self, ranking) -> None:
        """Setter ranking"""
        self._ranking = int(ranking)

    def get_ranking(self) -> int:
        """Getter ranking"""
        return self._ranking
