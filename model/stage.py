class Stage:

    def __init__(self, specifications) -> None:
        if '_id' in specifications:
            self._id = specifications['_id']
        self._number = specifications['_number']
        if '_id_match' in specifications:
            self._id_match = specifications['_id_match']
        if '_status' in specifications:
            self._status = specifications['_status']
        else:
            self.status = False