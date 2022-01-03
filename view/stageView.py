from view.view import View as v

class StageView:

    def __init__(self) -> None:
        self.view = v()

    def except_value(self, string_to_except):
        self.view.print_to_user(string_to_except)