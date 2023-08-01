# Возьмите 1-3 задачи из тех, что были на прошлых семинарах
# или в домашних заданиях. Напишите к ним классы исключения
# с выводом подробной информации. Поднимайте исключения внутри
# основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра
from ex_1_excep import IsDigitException


class Archive:
    """This class stores a couple of properties."""

    list_numbers = []
    list_strings = []

    def __init__(self, number, string):
        """Added number and string parameters.
        Parameter values are passed to lists."""
        if not isinstance(number, (int, float)):
            raise IsDigitException(number)
        else:
            self.number = number
            self.string = string
            self.list_numbers.append(self.number)
            self.list_strings.append(self.string)


if __name__ == '__main__':
    a = Archive(12, 'test')
    print(a.list_numbers, a.list_strings)
    b = Archive('twelve', 'test_2')
    print(b.list_numbers, b.list_strings)
