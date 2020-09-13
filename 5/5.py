import random
import json
import functools

# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
f = open('5_1', 'w', encoding='utf-8')
while True:
    user_text = input('Введите строку для файла (пустая строка для выхода)')
    f.write(user_text + "\n")
    if len(user_text) == 0:
        break

f.close()

# 2. Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
f = open('5_2', 'r', encoding='utf-8')
total_rows = 0
total_words = 0
for i in f:
    total_rows += 1
    words = i.split()
    total_words += len(words)

    print(f"Строка {total_rows}, слов: {len(words)}")

f.close()
print(f"Всего строк: {total_rows}, всего слов: {total_words}")

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
f = open('5_3', 'r', encoding='utf-8')
user_salary_sum = 0
user_count = 0
for i in f:
    data = i.split()
    if len(data) != 2:
        continue

    try:
        salary = int(data[1])
        user_count += 1
        user_salary_sum += salary
        if salary < 20000:
            print(f"сотрудник {data[0]} имеет оклад меньше 20000 (оклад {data[1]})")
    except:
        print('неверный формат файла')
        continue

medium = "{:10.2f}".format(user_salary_sum / user_count)
print(f'всего сотрудников: {user_count}, средняя зп: {medium}')
f.close()

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
word_map = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
f = open('5_4', 'r', encoding='utf-8')
fr = open('5_4_r', 'w', encoding='utf-8')

for i in f:
    data = i.split()
    ru_word = word_map.get(data[0], False)
    ru_text = f"Неизвестное число %{data[0]}%" if ru_word is False else ru_word
    data[0] = ru_text

    fr.write(" ".join(data) + "\n")

f.close()
fr.close()

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
f = open("5_5", 'w+', encoding="utf-8")

nums = [str(random.randint(10, 100)) for _ in range(1, 100)]
f.write(" ".join(nums))

f.seek(0)
random_nums = f.readline()

total_sum = functools.reduce(lambda a, b: int(a)+int(b), random_nums.split())
print(f"Общая сумма: {total_sum}")

f.close()

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def get_digits_from_str(line):
    res = []
    for i in line.split():
        num = ''
        for j in i:
            if j.isnumeric() is not True:
                continue
            num += j
        if len(num) > 0:
            res.append(int(num))
    return res


f = open("5_6", 'r', encoding="utf-8")
result = {}
for i in f:
    data = i.split(":")
    if len(data) != 2:
        print("ошибка формата расписания")
        continue

    result[data[0]] = functools.reduce(lambda a, b: a + b, get_digits_from_str(data[1]))

f.close()
print(f"по часам предметов:{result}")

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

def parse_firm_info(line):
    company_info = line.split()
    profit = int(company_info[2])
    debt = int(company_info[3])
    return [company_info[0], profit - debt]


calculation_result = []
with open("5_7", "r", encoding='utf-8') as f:
    c_params = {}
    sum_total = 0
    count = 0
    for i in f:
        company_name, res_amount = parse_firm_info(i)
        c_params[company_name] = res_amount
        if res_amount > 0:
            sum_total += res_amount
            count += 1

    avg = sum_total / count if count > 0 else 0
    calculation_result.append(c_params)
    calculation_result.append({'average_profit': avg})

print(calculation_result)
with open("5_7_j", "w", encoding='utf-8') as f:
    json.dump(calculation_result, f)
