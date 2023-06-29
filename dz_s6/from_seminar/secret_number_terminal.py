# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение
__all__ = ['func']
from random import randint
from sys import argv


def func(lower_limit, upper_limit, attempts):
    secret_number = randint(lower_limit, upper_limit)
    while attempts:
        number_user = int(input(f'Введите число от {lower_limit} до {upper_limit}: '))
        if number_user == secret_number:
            print('угадали, загаданное чсило - ', secret_number)
            break
        elif number_user > secret_number:
            attempts -= 1
            print('меньше\nосталось попыток - ', attempts)
        elif number_user < secret_number:
            attempts -= 1
            print('больше\nосталось попыток - ', attempts)
    else:
        print('загаданное чсило - ', secret_number)


if __name__ == '__main__':
    _, *params = argv
    func(*map(int, params))