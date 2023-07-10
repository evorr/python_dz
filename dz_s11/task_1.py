# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)
import time


class MyStr(str):
    """This class stores the name of the author of the string and the creation time."""

    def __new__(cls, value, name):
        """Added name and time parameters."""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time_cr = time.time()
        return instance

    def __str__(self):
        return f'author of the string: {self.name}\ncreation time: {self.time_cr}'

    def __repr__(self):
        return f'MyStr({super().__str__()}, {self.name})'


a = MyStr('test', 'author')
print(a)
print(repr(a))
print(a.upper())
print(a.time_cr)
print(a.name)
#help(MyStr)
