# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.
from traffic_light import TrafficLight

t = TrafficLight()
t.running()

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
import random

from road import Road

road = Road(5000, 20)
asphaltHeight = 5
need = road.calculate_asphalt(asphaltHeight)
print(f"для толщины в {asphaltHeight}cm необходимо асфальта: {need}")

# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, positions (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
from positions import Position


def create_position(position_name: str, salary: int, bonus: int, name: str, sur_name: str):
    p = Position(position_name, salary, bonus)
    p.set_fio(name, sur_name)
    return p


for i in [
    Position('developer', 100, 5).set_fio('Ivan', 'Ivanoff'),
    create_position('analytic', 80, 5, 'Petr', 'Petroff'),
    create_position('tester', 50, 0, 'Semen', 'Semenoff'),
    create_position('project_manager', 120, 15, 'Anton', 'Antonoff'),
]:
    print(f'сотрудник: {i.get_full_name()}, должность: {i.get_position()}, суммарый доход {i.get_incoming()}')

# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

from cars import Car, PoliceCar, TownCar, SportCar, WorkCar, Directions


def watch_car(car_obj: Car):
    speed = car_obj.go(random.randint(40, 100))
    rand_direction = [Directions.FORWARD, Directions.BACK, Directions.LEFT, Directions.RIGHT][random.randint(0, 3)]
    direction = car_obj.turn(rand_direction)
    ride_stop = random.randint(1, 10)
    if ride_stop > 9:
        speed = car_obj.go(0)

    speed_text = f"едет со скоростью {car_obj.show_speed()}" if speed > 0 else "остановилась"
    car_details = f"{car_obj.get_car_desc()}"
    print(f'{car_obj.__class__.__name__}({car_details}) {speed_text}, {direction}')
    if speed == 0:
        return False
    return True


for car in [PoliceCar(), TownCar('black', 'kia'), SportCar('red', 'bmw'), WorkCar('kama2')]:
    while watch_car(car):
        pass

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
from stationerys import Pen, Pencil, Handle

Handle().draw()
Pencil().draw()
Pen().draw()
