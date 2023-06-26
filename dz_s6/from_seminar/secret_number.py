# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.
__all__ = ['func']
from random import randint


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
    func(1, 1000, 10)