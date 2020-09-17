class Directions:
    FORWARD = "ALGA!!!"
    BACK = "налево алга, еще раз налево алга"
    LEFT = "налево и алга"
    RIGHT = "навраво и алга"


class Car:
    _speed = 0
    _color = None
    _name = None
    _is_police = False
    _direction = ''

    def __init__(self, color: str, name: str, police: bool):
        self._color = color
        self._name = name
        self._is_police = police

    def turn(self, direction: str):
        self._direction = direction
        return self._direction

    def stop(self):
        self._speed = 0
        return self._speed

    def go(self, speed: int):
        self._speed = speed
        return self._speed

    def show_speed(self):
        return self._speed

    def get_car_desc(self):
        return f'{self._name} {self._color}'
