class Road:
    _length = 0
    _width = 0
    __weight_per_square = 25

    def __init__(self, length, width):
        self._width = int(width)
        self._length = int(length)

    def calculate_asphalt(self, asphalt_height: int):
        return (self._width * self._length * self.__weight_per_square * asphalt_height) / 1000
