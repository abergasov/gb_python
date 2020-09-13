from cars.car import Car

class PoliceCar(Car):

    def __init__(self):
        super(PoliceCar, self).__init__("grey", "lada", True)
