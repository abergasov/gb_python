from cars.car import Car

class WorkCar(Car):

    _max_speed = 60

    def __init__(self, vendor: str):
        super(WorkCar, self).__init__('dark_grey', vendor, False)

    def show_speed(self):
        if self._max_speed > self._speed:
            return f"{self._speed}(превышение скорости! {self._max_speed} max)"
        return self._speed
