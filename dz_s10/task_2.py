# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.
class Rectangle:
    def __init__(self, length, width=0):
        if width == 0:
            width = length
        self.length = length
        self.width = width

    def length_rectangle(self):
        return 2 * self.length + 2 * self.width

    def area_rectangle(self):
        return self.length * self.width


r1 = Rectangle(3, 4)
print(f'{r1.length_rectangle() = }\n{r1.area_rectangle() = }')
r2 = Rectangle(3)
print(f'{r2.length_rectangle() = }\n{r2.area_rectangle() = }')
