import math
from abc import ABC, abstractmethod
# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Maxtrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        res = ""
        for i in self.matrix:
            res += (' '.join(str(j) for j in i)) + '\n'
        return res

    def __add__(self, other):
        res = []
        matrix_len = len(self.matrix)
        if matrix_len != len(other.matrix):
            raise RuntimeError("матрицы должны совпадать по размерам")

        for i in range(matrix_len):
            row_len = len(self.matrix[i])
            if row_len != len(other.matrix[i]):
                raise RuntimeError("матрицы должны совпадать по размерам!")
            tmp = []
            for j in range(row_len):
                tmp.append(self.matrix[i][j] + other.matrix[i][j])
            res.append(tmp)

        return Maxtrix(res)


matrix_1 = Maxtrix([[31, 22, 8], [37, 43, 1], [51, 86, 55]])
matrix_2 = Maxtrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
matrix_3 = Maxtrix([[3, 5, 8, 3], [8, 3, 7, 1]])

try:
    print(matrix_1)
    print(matrix_2)
    print('сумму этих матриц:')
    print(matrix_1 + matrix_2)

    print()
    print()
    print()

    print(matrix_2)
    print(matrix_3)
    print('сумму этих матриц:')
    print(matrix_2 + matrix_3)
except RuntimeError as t:
    print(f"ошибка: {t}")

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


class Wear(ABC):
    @abstractmethod
    def calculate(self):
        pass


class Coat(Wear):
    def __init__(self, v):
        self.v = v

    @property
    def calculate(self):
        return "{:.2f}".format((self.v / 6.5) + 0.5)


class Suit(Wear):
    def __init__(self, h):
        self.h = h

    @property
    def calculate(self):
        return "{:.2f}".format((self.h * 2) + 0.3)


print(f"Костюм длиной 2 потребует {Suit(2).calculate} ткани")
print(f"Костюм длиной 1.5 потребует {Suit(1.5).calculate} ткани")
print(f"Костюм длиной 1 потребует {Suit(1).calculate} ткани")

print(f"Пальто длиной 1 потребует {Coat(1).calculate} ткани")
print(f"Пальто длиной 1.5 потребует {Coat(1.5).calculate} ткани")
print(f"Пальто длиной 2 потребует {Coat(2).calculate} ткани")


# 3. Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки.
# Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell > other.cell:
            return Cell(self.cell - other.cell)
        raise RuntimeError("разность количества ячеек двух клеток больше нуля")

    def __truediv__(self, other):
        return Cell(math.ceil(self.cell / other.cell))

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def make_order(self, rows):
        res = ""
        for i in range(self.cell):
            if i % rows == 0:
                res += "\n"
            res += '*'
        return res


cell_1 = Cell(13)
cell_2 = Cell(4)

try:
    print(f"клетка 1: {cell_1}, 2:{cell_2}")
    print(f"сумма: {cell_1 + cell_2}")
    print(f"умножение: {cell_1 * cell_2}")
    print(f"разница: {cell_1 - cell_2}")
    print(f"деление: {cell_1 / cell_2}")

    print(cell_1.make_order(4))
    print(cell_2.make_order(4))
    print(cell_2 - cell_1)
except RuntimeError as t:
    print(f"ошибка: {t}")
