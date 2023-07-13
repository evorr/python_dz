# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length_circle(self):
        return 2 * math.pi * self.radius

    def square_circle(self):
        return math.pi * (self.radius ** 2)


c1 = Circle(3)
c2 = Circle(1)
print(f'{c1.length_circle() = }\n{c1.square_circle() = }')
print(f'{c2.length_circle() = }\n{c2.square_circle() = }')