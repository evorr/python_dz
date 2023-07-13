# Возьмите любую из задач с прошлых семинаров
# (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства.
# Задачи должны решаться через вызов методов экземпляра.

# Задача с семинара 6.
# Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
from random import randint


class DataInYear:
    def __init__(self, data):
        self.day = int(data.split('.')[0])
        self.month = int(data.split('.')[1])
        self.year = int(data.split('.')[2])

    def check_year(self):
        if self.year < 1 or self.year > 9999:
            return False
        return True

    def check_visokos(self):
        if self.year % 400 == 0 or self.year % 100 != 0 and self.year % 4 == 0:
            return True
        return False

    def check_month(self):
        if self.month < 1 or self.month > 12:
            return False
        return True

    def check_day(self):
        if self.day < 1 or self.day <= 31:
            if self.day == 31 and self.month in [4, 6, 7, 9, 11]:
                return True
            elif self.month == 2:
                if self.day > 29:
                    return False
                if self.day == 29:
                    return self.check_visokos()
            return True
        return False

    def check_data(self):
        if self.check_year() and self.check_month() and self.check_day():
            return True
        return False


data = DataInYear('29.00.2500')
print(data.check_year())
print(data.check_month())
print(data.check_day())
print(data.check_data())
