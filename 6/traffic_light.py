import time


class TrafficLight:
    __color = None
    __c_before = None

    def running(self):
        i = 1
        while i < 3:
            for color, t_delay in {'red': 7, 'orange': 2, 'green': 12}.items():
                self.__color = color
                print(self.dispatch(color, i, t_delay))
                self.__check_color(color)
                time.sleep(t_delay)
            i += 1

    def get_color(self):
        return self.__color

    def dispatch(self, color, iteration, delay):
        method_name = f"_generate_{str(color)}_str"
        method = getattr(self, method_name, None)
        if method is None:
            return f"invalid color {color}"
        return method(iteration, color, delay)

    def _generate_red_str(self, i, text, delay):
        return f"\033[91m{i} - {text} ({delay}s wait)"

    def _generate_green_str(self, i, text, delay):
        return f"\033[92m{i} - {text} ({delay}s wait)"

    def _generate_orange_str(self, i, text, delay):
        return f"\033[93m{i} - {text} ({delay}s wait)"

    def __check_color(self, color: str):
        if self.__c_before is None:
            self.__c_before = color
            return
        if self.__c_before == "red" and color != "orange":
            raise RuntimeError('после красного должен идти оранжевый')
        elif self.__c_before == "orange" and color != "green":
            raise RuntimeError('после оранжевого должен идти зеленый')
        elif self.__c_before == "green" and color != "red":
            raise RuntimeError('после зеленого должен идти красный')

        self.__c_before = color
