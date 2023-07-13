# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Range:
    def __init__(self, min_value: int = None):
        self.min_value = min_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if value.istitle():
          setattr(instance, self.param_name, value)

    def validate(self, value):
        if not isinstance(value, int):
            raise TypeError(f'Value {value} should be celoe chislo')
        if self.min_value is not None and value <= self.min_value:
            raise ValueError(f'Value {value} должно быть болььше{self.min_value}')


class Rectangle:
    length = Range(0)
    width = Range(0)

    def __init__(self, length, width=0):
        if width == 0:
            width = length
        self.length = length
        self.width = width

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


if __name__ == '__main__':
    r1 = Rectangle(4, 10)
    print(f'{r1 = }')
    r1.width = 7
    print(f'{r1 = }')
    r1.width = 0
    print(f'{r1 = }')
    r1.width = -3
    print(f'{r1 = }')

