from stationerys.stationery import Stationery


class Handle(Stationery):
    __title = 'handle'

    def draw(self):
        print(f"{self.__title} is drawing")

