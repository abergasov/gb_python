class Worker:
    _name = ''
    _surname = ''
    _position = ''
    __income = None

    def __init__(self, wage: int, bonus: int, position: str):
        self.__income = {
            "wage": wage,
            "bonus": bonus,
        }
        self._position = position

    def _set_name(self, name: str):
        self._name = name

    def _set_sur_name(self, sur_name: str):
        self._surname = sur_name

    def get_incoming(self):
        return self.__income['wage'] + self.__income['bonus']
