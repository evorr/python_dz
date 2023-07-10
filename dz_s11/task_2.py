# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

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


a = Archive(12, 'test')
print(a)
print(a.list_numbers, a.list_strings)
b = Archive(13, 'test_2')
print(b)
print(b.list_numbers, b.list_strings)