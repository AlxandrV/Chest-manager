from datetime import datetime

class Player:
    
    def __init__(self, specifications) -> None:
        if '_id' in specifications:
            self._id = specifications['_id']
        self._name = specifications['_name']
        self._last_name = specifications['_last_name']
        self._gender = specifications['_gender']
        self._birthday = specifications['_birthday']
        self._ranking = specifications['_ranking']
        if '_temp_rank' in specifications:
            self._temp_rank = specifications['_temp_rank']
        else:
            self._temp_rank = 0
