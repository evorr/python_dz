# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from sys import argv


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
    _, params = argv
    print(func(params))

# python .\zadacha_dz_1.py 29.02.2023