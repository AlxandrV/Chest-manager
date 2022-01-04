class Stage:

    def __init__(self, specifications) -> None:
        if '_id' in specifications:
            self._id = specifications['_id']
        self._number = specifications['_number']
        self._id_tournament = specifications['_id_tournament']
        if '_id_match' in specifications:
            self._id_match = specifications['_id_match']
        if '_status' in specifications:
            self._status = specifications['_status']
        else:
            self._status = 0
        if '_datetime_start' in specifications:
            self._datetime_start = specifications['_datetime_start']
        if '_datetime_end' in specifications:
            self._datetime_end = specifications['_datetime_end']