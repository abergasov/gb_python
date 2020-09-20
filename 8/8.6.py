# 8. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class MyComplex:

    def __init__(self, num: int, num2: int = 1):
        self.num = num
        self.num2 = num2

    def __repr__(self):
        sign = "+" if self.num2 > 0 else ""
        return f"complex is ({self.num} {sign} {self.num2}i)"

    def __add__(self, other):
        a = self.num
        ai = self.num2
        b = other.num
        bi = other.num2
        return MyComplex(a + b, ai + bi)

    def __mul__(self, other):
        a = self.num
        ai = self.num2
        b = other.num
        bi = other.num2
        s = a * b + ai * bi * -1
        i = a*bi + ai * b
        return MyComplex(s, i)


c1 = MyComplex(3, 1)
c2 = MyComplex(2, -3)
c3 = MyComplex(4, -4)
c4 = MyComplex(1, 4)
c5 = MyComplex(1, 4)

print(c1)
print(c2)
print(c1 * c2)
print(c1 + c2)

print(c3)
print(c1 * c3)

print(c4)
print(c5)
print(c4 * c5)
print(c4 + c5)