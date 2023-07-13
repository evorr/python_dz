# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

class Archive:
    """This class stores a couple of properties."""
    list_numbers = []
    list_strings = []

    def __init__(self, number, string):
        """Added number and string parameters.
        Parameter values are passed to lists."""
        self.number = number
        self.string = string
        self.list_numbers.append(self.number)
        self.list_strings.append(self.string)

    def __str__(self):
        """String representation of an object when printing an instance."""
        return f'Number: {self.number}, String: {self.string}'

    def __repr__(self):
        """A string representation of an object that can be used to recreate this object."""
        return f'Archive({self.number}, {self.string})'


a = Archive(12, 'test')
print(a)
print(f'{a = }')
