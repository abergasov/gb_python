from cars.car import Car

class SportCar(Car):

    def __init__(self, color: str, vendor: str):
        super(SportCar, self).__init__(color, vendor, False)
