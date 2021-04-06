#  Реализовать проект «Операции с комплексными числами».
#  Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
#  Проверьте работу проекта, создав экземпляры класса (комплексные числа)
#  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class complex_number:

    def __init__(self, a, b, i):
        self.a = a
        self.b = b
        self.i = i

    def x (self):
        return self.a + self.b * self.i

    def __add__(self, other):
        return complex_number(self.number + other.number)

    def __mul__(self, other):
        return complex_number(self.number * other.number)

x_1 = complex_number(int(input('a = ')), int(input('b = ')), int(input('i = ')))
x_1 = complex_number.x(x_1)
print('x_1 =', x_1)
x_2 = complex_number(int(input('a = ')), int(input('b = ')), int(input('i = ')))
x_2 = complex_number.x(x_2)
print('x_2 =', x_2)
print("x_1 + x_2 = ", x_1 + x_2)
print("x_1 * x_2 =", x_1 * x_2)