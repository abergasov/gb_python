# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = [1, "2", False, [1, 2, 3], {1, 2, 3}]

for i in my_list:
    print(f"содержимое:{i}, тип: {type(i)}")

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
user_list = "1 2 3 4 5 6 7 111 8 9 10 11"
iterable_list = user_list.split()
i = 0
while i < len(iterable_list):
    if i + 1 >= len(iterable_list):
        break
    if i % 2 == 0:
        a = iterable_list[i]
        b = iterable_list[i + 1]

        iterable_list[i] = b
        iterable_list[i + 1] = a
    i += 1

result = ' '.join(iterable_list)
print(f"оригинальная последовательность: {user_list}")
print(f"итог перестановок: {result}")

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

user_month = input("Введите номер месяца")
# user_month = 9
user_month = int(user_month)
if 0 < user_month <= 12:
    month_data = {"Зима": [1, 2, 12], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
    for group in month_data:
        for month_num in month_data[group]:
            if month_num != user_month:
                continue
            print(f"Месяц {user_month} относится к {group}")

else:
    print("Неверный месяц")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
user_text = input("Введите нескольких слов, разделённых пробелами")
# user_text = "Пользователь вводит строку из нескольких слов Строки необходимо пронумероватьпронумеровать."
user_text_words = user_text.split()
for i in range(len(user_text_words)):
    word = user_text_words[i]
    word_length = len(word)
    word = word[:10] + '...' if word_length > 10 else word
    print(f"{i} - {word}")

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
# после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
print(f"Текущий рейтинг: {my_list}")
while True:
    new_ratio = input("Введите новый рейтинг или наберите -1 что бы выйти")
    if new_ratio == "-1":
        break
    if not new_ratio.isnumeric():
        print("Только числа")
        continue

    new_ratio = int(new_ratio)
    # если в списке нет этого числа - берем индекс для вставки 0, иначе - индекс первого совпадения
    new_position = 0 if not new_ratio in my_list else my_list.index(new_ratio)
    my_list.insert(new_position, new_ratio)
    print(f"Новый рейтинг: {my_list}")

print(f"Итоговый рейтинг: {my_list}")

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }