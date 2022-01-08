class Tournament:

    def __init__(self, specifications) -> None:
        if '_id' in specifications:
            self._id = specifications['_id']
        self._name = specifications['_name']
        self._place = specifications['_place']
        self._date_start = specifications['_date_start']
        self._date_end = specifications['_date_end']
        if '_id_stage' in specifications:
            self._id_stage = specifications['_id_stage']
        self._time_control = specifications['_time_control']
        self._description = specifications['_description']
        self._number_players = specifications['_number_players']
        if '_list_players' in specifications:
            self._list_players = specifications['_list_players']
        if '_status' in specifications:
            self._status = specifications['_status']
        else:
            self._status = 0
        if '_stage_in_progress' in specifications:
            self._stage_in_progress = specifications['_stage_in_progress']
        else:
            self._stage_in_progress = False
