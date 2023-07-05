# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать декорированную функцию со случайными числами
# из диапазонов.
from random import randint
from functools import wraps

__all__ = ['game', 'deco', ]


def deco(func):
    @wraps(func)
    def wrapper(num, attempt):
        if num < 1 or num > 100:
            num = randint(1, 100)
        if attempt < 1 or attempt > 10:
            attempt = randint(1, 10)
        func(num, attempt)

    return wrapper


@deco # или в if __name__== '__main__': game = deco(func) game(108, 11)
def game(num, attempt):
    count = 0
    while count < attempt:
        number_user = int(input(f'Введите число от 1 до 100: '))
        if number_user == num:
            print(f'угадали, загаданное чсило - {num}')
        elif number_user > num:
            count += 1
            print('меньше\nпопытка - ', count)
        elif number_user < num:
            count += 1
            print('больше\nпопытка - ', count)
    if count == attempt:
        print(f'загаданное чсило - - {num}')


if __name__ == '__main__':
    game(108, 13)
    print(f'{game.__name__ = }')
