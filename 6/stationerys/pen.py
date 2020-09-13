from stationerys.stationery import Stationery


class Pen(Stationery):
    __title = 'pen... piter pen'

    def draw(self):
        print(f"{self.__title} is drawing")

