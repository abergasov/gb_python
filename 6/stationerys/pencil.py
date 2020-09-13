from stationerys.stationery import Stationery


class Pencil(Stationery):
    __title = 'pencil'

    def draw(self):
        print(f"{self.__title} is drawing")

