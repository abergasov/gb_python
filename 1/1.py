# задание 1.1 Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
a = 2
b = 3
print(f"умножение: {a * b}")
print(f"деление: {a / b}")
print(f"целочисленное деление: {a // b}")
print(f"целочисленное деление: {a % b}")
user_input = input("введите число:")
print(f"введено число: {user_input}")
print(f"умножение: {int(user_input) * a * b}")


# задание 1.2 Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
user_seconds = input("введите число секунд:")
print(f"ковертируем секунды: {user_seconds}")

user_seconds = int(user_seconds)

# узнаем сколько полных часов в указанных сек
hours = user_seconds // 3600
# вычитаем часы из общего числ секунд и узнаем полное число минут
minutes = (user_seconds - (hours * 3600)) // 60
# все что остается после вычета часов и минут - просто пихаем в секунды
seconds = user_seconds - (hours * 3600) - (minutes * 60)
print(f"{hours}:{minutes}:{seconds}")


# 1.3 Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
user_num = input("введите число:")
sumFromString = int(user_num) + int(user_num + user_num) + int(user_num + user_num + user_num)
user_num = int(user_num)
sumFromInt = user_num + 11 * user_num + 111 * user_num
print(f"сумма чисел через объединение строк n + nn + nnn: {sumFromString}")
print(f"сумма чисел через умножение n + nn + nnn: {sumFromInt}")


# 1.4 Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_num = input("введите положительное число:")
user_num = int(user_num)
if user_num > 0:
    maxD = -1
    while user_num > 10:
        d = user_num % 10
        user_num //= 10
        if d > maxD:
            maxD = d

    print(f"максимальная цифра: {maxD}")


# 1.5 Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
company_proceeds = input("введите выручку:")
company_cost = input("введите издержки:")

company_proceeds = int(company_proceeds)
company_cost = int(company_cost)
if company_proceeds > company_cost:
    print("компания работает в +")
    company_profit = company_proceeds - company_cost
    print(f"прибыль: {company_profit}")
    print(f"рентабельность: {company_profit/company_proceeds}")
    company_employees = input("введите число сотрудников:")
    company_employees = int(company_employees)
    if company_employees > 0:
        print(f"прибыль с сотрудника: {company_profit/company_employees}")
else:
    print("компания работает в -")


# 1.6 Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
user_distance = input("сколько километров пробежали:")
user_target = input("сколько километров хотите пробежать:")
user_distance = int(user_distance)
user_target = int(user_target)
if user_target > 0 and user_distance > 0:
    tD = 1
    while True:
        user_distance = (user_distance / 100) * 110
        if user_distance >= user_target:
            print(f"цель достигните на день {tD}")
            break
        tD += 1
