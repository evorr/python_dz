# Создайте модуль и напишите в нём функцию, которая получает на вход дату в виде строки вида DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
__all__ = ['func']


def func(data):
    day, month, year = map(int, data.split('.'))
    if 0 < year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31:
        if day == 31 and month in [4, 6, 7, 9, 11]:
            return False
        if month == 2:
            if day > 29:
                return False
            if day == 29:
                return check(year)
        return True
    return False


def check(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    return False


if __name__ == '__main__':
    print(func('31.04.2024'))