from cars.car import Car

class TownCar(Car):

    _max_speed = 60

    def __init__(self, color: str, vendor: str):
        super(TownCar, self).__init__(color, vendor, False)

    def show_speed(self):
        if self._max_speed > self._speed:
            return f"{self._speed}(превышение скорости! {self._max_speed} max)"
        return self._speed
