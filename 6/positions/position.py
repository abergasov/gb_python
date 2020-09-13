from positions.worker import Worker


class Position(Worker):

    def __init__(self, position_name: str, salary: int, bonus: int):
        super().__init__(salary, bonus, position_name)

    def get_full_name(self):
        return f"{self._name} {self._surname}"

    def set_fio(self, name: str, sur_name: str):
        self._set_name(name)
        self._set_sur_name(sur_name)
        return self

    def get_total_income(self):
        return self.get_incoming()

    def get_position(self):
        return self._position
