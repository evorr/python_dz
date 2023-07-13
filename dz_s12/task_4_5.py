# 4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.

# 5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.


class Rectangle:
    __slots__ = ('_length', '_width')

    def __init__(self, length, width=0):
        if width == 0:
            width = length
        self._length = length
        self._width = width

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._width

    @length.setter
    def length(self, value):
        if value > 0:
            self._length = value
        else:
            raise ValueError('Сторона не может быть ноль или меньше')

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError('Сторона не может быть ноль или меньше')

    def length_rectangle(self):
        return 2 * self.length + 2 * self.width

    def area_rectangle(self):
        return self.length * self.width

    def __add__(self, other):
        res = self.length_rectangle() + other.length_rectangle()
        sum_sides = res / 2
        new_width, new_length = sum_sides * 0.4, sum_sides * 0.6
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        res = abs(self.length_rectangle() - other.length_rectangle())
        sum_sides = res / 2
        new_width, new_length = sum_sides * 0.4, sum_sides * 0.6
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        return self.area_rectangle() == other.area_rectangle()

    def __ne__(self, other):
        return self.area_rectangle() != other.area_rectangle()

    def __gt__(self, other):
        return self.area_rectangle() > other.area_rectangle()

    def __ge__(self, other):
        return self.area_rectangle() <= other.area_rectangle()

    def __lt__(self, other):
        return self.area_rectangle() < other.area_rectangle()

    def __le__(self, other):
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
