# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

# usage: python 4/1.py 33 2 3
from sys import argv

_, w_hours, p_hour, prem = argv


def calculate_pay(work_hours, per_hour, premium):
    return int(work_hours) * int(per_hour) + int(premium)


try:
    sum_v = calculate_pay(w_hours, p_hour, prem)
    print(f"Реккомендуемая заработная плата сотрудника: {sum_v}")
except (ValueError,) as err:
    print(f"Допускаются только числа, {err.args[0]}")
