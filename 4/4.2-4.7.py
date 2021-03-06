import itertools
from functools import reduce
# 2. Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def is_el_valid(list_el):
    b = None
    for i in list_el:
        if b is None:
            b = i
            continue
        if i > b:
            yield i
        b = i


print([el for el in is_el_valid(my_list)])


# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.
res_list = [el for el in range(20, 240) if (el % 20 == 0) or (el % 21 == 0)]
print(res_list)


def gen():
    for el in range(20, 240):
        valid = (el % 20 == 0) or (el % 21 == 0)
        if valid is not True:
            continue
        yield el


res_list = [i for i in gen()]
print(res_list)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
src_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def check_duplicates(list_data):
    for i in list_data:
        if list_data.count(i) == 1:
            yield i


print([el for el in check_duplicates(src_list)])


# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
def generate_list():
    for i in range(99, 1001):
        if i % 2 == 0:
            yield i


custom_list = [el for el in generate_list()]
data = reduce(lambda a, b: a+b, custom_list)
data_from_iterate = reduce(lambda a, b: a+b, generate_list())
print(f"Сумма через промедуточный список: {data}, напрямки: {data_from_iterate}")


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

# а) итератор, генерирующий целые числа, начиная с указанного,
limit = input('Введите длину списка: ')
user_num = input('Введите начальное число: ')


def generate_user_list(start_num, max_count):
    j = 0
    for i in itertools.count(int(start_num), 1):
        j += 1
        yield i
        if j > int(max_count):
            break


try:
    print([el for el in generate_user_list(user_num, limit)])
except:
    print("Что-то не так. Вводите только числа")


# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
sample_list = [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210, 220, 231]


def duplicate_sample_list(list_to_copy):
    counter = 0
    for i in itertools.cycle(list_to_copy):
        counter += 1
        if counter > len(list_to_copy):
            break
        yield i


copy_list = [el for el in duplicate_sample_list(sample_list)]
print(f"Исходный список: {sample_list}")
print(f"Копия списка: {copy_list}")


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
        yield i, res


for i in fact(6):
    key, val = i
    print(f"факториал числа {key}: {val}")