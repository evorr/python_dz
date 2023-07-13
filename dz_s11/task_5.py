# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    """A class for arithmetic operations with a rectangle. Allows to calculate
    the perimeter and area of a rectangle, add and subtract the perimeters of rectangles """

    def __init__(self, length, width=0):
        """Sets the width and length of the rectangle"""
        if width == 0:
            width = length
        self.length = length
        self.width = width

    def length_rectangle(self):
        """Calculate the perimeter of a rectangle"""
        return 2 * self.length + 2 * self.width

    def area_rectangle(self):
        """Calculate the area of a rectangle"""
        return self.length * self.width

    def __add__(self, other):
        """Gets a rectangle whose perimeter is equal to the sum of the rectangles' perimeter."""
        res = self.length_rectangle() + other.length_rectangle()
        sum_sides = res / 2
        new_width, new_length = sum_sides * 0.4, sum_sides * 0.6
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        """Gets a rectangle whose perimeter is equal to the difference of the rectangles' perimeter."""
        res = abs(self.length_rectangle() - other.length_rectangle())
        sum_sides = res / 2
        new_width, new_length = sum_sides * 0.4, sum_sides * 0.6
        return Rectangle(new_length, new_width)

    def __str__(self):
        if self.width == self.length:
            return f'Square with side {self.length}'
        return f'Rectangle with sides {self.length} and {self.width}'

    def __repr__(self):
        return f'Rectangle({self.length},{self.width})'


r1 = Rectangle(3, 4)
print(r1)
print(r1.length_rectangle())
r2 = Rectangle(3)
print(repr(r2))
print(r2)
print(r2.length_rectangle())

r3 = r1.__add__(r2)
print(r3.length, r3.width, r3.length_rectangle())
r4 = r1.__sub__(r2)
print(r4.length, r4.width, r4.length_rectangle())
