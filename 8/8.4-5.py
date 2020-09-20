import random
from abc import ABC, abstractmethod
import json


class InventoryItem(ABC):
    _vendor = ""
    _year = 0
    _type = ""
    _model = ""

    def populate(self, vendor: int, model: int, year: int):
        self._type = self.get_type()
        self._year = year
        if model > len(self.get_model_list()):
            raise RuntimeError("Model invalid")

        self._model = self.get_model_list()[model]

        if vendor > len(self.get_vendor_list()):
            raise RuntimeError("Vendor invalid")

        self._vendor = self.get_vendor_list()[vendor]
        return self

    @abstractmethod
    def get_type(self) -> str:
        pass

    @abstractmethod
    def get_model_list(self) -> list:
        pass

    @abstractmethod
    def get_vendor_list(self) -> list:
        pass

    def __repr__(self):
        return self.get_type()

    @staticmethod
    def _generate_inventory() -> int:
        return random.randint(10000, 100000)

    def get_item(self) -> dict:
        return {
            "type": self._type,
            "vendor": self._vendor,
            "model": self._model,
            "year": self._year,
            "inventory_number": InventoryItem._generate_inventory(),
        }


class Printer(InventoryItem):

    def get_type(self) -> str:
        return "printer"

    def get_model_list(self) -> list:
        return ["abc-x2", "cdf-j3", "yuz2000"]

    def get_vendor_list(self) -> list:
        return ["pr_1", "pr_2", "pr_3"]


class Scanner(InventoryItem):

    def get_type(self) -> str:
        return "scanner"

    def get_model_list(self) -> list:
        return ["sc_1", "sc_2", "sc_3"]

    def get_vendor_list(self) -> list:
        return ["sc_vendor_1", "sc_vendor_2"]


class Xerox(InventoryItem):
    def get_type(self) -> str:
        return "xeroxx"

    def get_model_list(self) -> list:
        return ["xe_1", "xe_2", "xe_3"]

    def get_vendor_list(self) -> list:
        return ["xe_vendor_1", "xe_vendor_2", "xe_vendor_3"]


class Storage:
    _departments = ['it', 'sysops', 'accounting']
    _items_map = {}

    def __init__(self):
        for i in self._departments:
            self._items_map[i] = []

    def get_dep_map(self) -> dict:
        result = {}
        i = 0
        for d in self._departments:
            result[i] = d
            i += 1
        return result

    def add_item(self, item: InventoryItem, count: int, dep: int) -> bool:
        if dep in self.get_dep_map():
            for i in range(count):
                data = item.get_item()
                self._items_map[self.get_dep_map()[dep]].append(data)
            return True
        return False

    def print_result(self) -> dict:
        return self._items_map


storage = Storage()


type_list = {
    1: Printer(),
    2: Scanner(),
    3: Xerox(),
}


# проверяем что юзер ввел что нужно
def validate_input(user_input: str, av_list=None) -> bool:
    if user_input == "q":
        raise RuntimeError("exit here")

    if user_input.isnumeric() is not True:
        print("только цифры")
        return False
    if av_list is not None:
        user_input = int(user_input)
        if user_input not in av_list:
            print("нет такого типа")
            return False
    return True

def convert_to_dict(items: list) -> dict:
    j = 0
    result = {}
    for i in items:
        result[j] = i
        j += 1
    return result

try:
    dep_map = storage.get_dep_map()
    while True:
        dep = input(f"укажите отдел {dep_map} (q для выхода)")
        if validate_input(dep, dep_map) is not True:
            continue

        t = input(f"укажите тип устройства {type_list} (q для выхода)")
        if validate_input(t, type_list) is not True:
            continue

        t = type_list[int(t)]

        v_list = convert_to_dict(t.get_vendor_list())
        v = input(f"укажите производителя устройства {v_list} (q для выхода)")
        if validate_input(v, v_list) is not True:
            continue

        m_list = convert_to_dict(t.get_model_list())
        m = input(f"укажите модель {m_list} (q для выхода)")
        if validate_input(m, m_list) is not True:
            continue

        y = input(f"укажите год")
        if validate_input(y) is not True:
            continue

        c = input(f"укажите количество предметов")
        if validate_input(c) is not True:
            continue

        item = t.populate(int(v), int(m), int(y))
        if storage.add_item(item, int(c), int(dep)):
            print("добавлено")
        else:
            print("ошибка добавления")
except Exception as e:
    a = 2
    print(e)
finally:
    print(storage.print_result())
