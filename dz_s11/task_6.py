# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

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

    def __eq__(self, other):
        """Checks whether the area of this rectangle is equal to the area of another rectangle."""
        return self.area_rectangle() == other.area_rectangle()

    def __ne__(self, other):
        """Checks that the area of this rectangle is not equal to the area of another rectangle."""
        return self.area_rectangle() != other.area_rectangle()

    def __gt__(self, other):
        """Checks that the area of this rectangle is larger than the area of another rectangle."""
        return self.area_rectangle() > other.area_rectangle()

    def __ge__(self, other):
        """Checks that the area of this rectangle is less than or equal to the area of another rectangle."""
        return self.area_rectangle() <= other.area_rectangle()

    def __lt__(self, other):
        """Checks that the area of this rectangle is smaller than the area of another rectangle."""
        return self.area_rectangle() < other.area_rectangle()

    def __le__(self, other):
        """Checks that the area of this rectangle is greater than or equal to the area of another rectangle."""
        return self.area_rectangle() >= other.area_rectangle()

    def __str__(self):
        if self.width == self.length:
            return f'Square with side {self.length}'
        return f'Rectangle with sides {self.length} and {self.width}'

    def __repr__(self):
        return f'Rectangle({self.length},{self.width})'


r1 = Rectangle(3, 4)
# print(r1.length_rectangle())
r2 = Rectangle(3)
r3 = Rectangle(3, 4)
# print(r2.length_rectangle())
print(r1.__gt__(r2))
print(r1.__gt__(r3))
