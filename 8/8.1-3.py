# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год»
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class CustomDate:

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"set data is {self.day} - {self.month} - {self.year}"

    @classmethod
    def get_int_from_str(cls, usr_str: str):
        data = [int(s) for s in usr_str.split('-')]
        if len(data) == 3 and cls.validate(data[0], data[1], data[2]):
            return cls(data[0], data[1], data[2])
        return None

    @staticmethod
    def validate(day: int, month: int, year: int) -> bool:
        valid = 0 < day <= 31 and 0 < month <= 12 and 2020 <= year <= 3000
        if valid is not True:
            return False
        if month == 2 and day > 30:
            return False
        return True


def get_user_date(usr_input: str):
    try:
        dataQ = CustomDate.get_int_from_str(usr_input)
        if dataQ is not None:
            print(dataQ)
        else:
            print("неверная дата")
    except Exception:
        print("допустимый формат даты: 22-09-2020")


get_user_date("10-02-2022")
get_user_date("10-22-2022")
get_user_date("44-22-2022")
get_user_date("abs-22-2022")


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class BadMathematica(Exception):

    def __init__(self, user_input, message="введите число больше 0"):
        self.input = user_input
        self.message = f"{message}. вы ввели: {self.input}"
        super().__init__(self.message)


try:
    ui = input("введите число, на которое разделить 10: ")
    if int(ui) == 0:
        raise BadMathematica(ui)
    print(10 / int(ui))
except BadMathematica as b:
    print(b.message)
except ValueError:
    print("вводите числа только")


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class BadNumber(Exception):

    def __init__(self, user_input, message="только числ допускаются"):
        self.input = user_input
        self.message = f"{message}. вы ввели: {self.input}"
        super().__init__(self.message)


def validate_input(usr_str: str):
    try:
        if usr_str.isnumeric():
            return int(usr_str)
        raise BadNumber(usr_str)
    except BadNumber as bn:
        print(bn.message)
        return None


usr_list = []
while True:
    usr = input("Введите число (q для выхода) ")
    if usr == "q":
        print(f"итоговый список: {usr_list}")
        break
    data = validate_input(usr)
    if data is not None:
        usr_list.append(data)
