# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.
from functools import wraps

__all__ = ['nny_func', 'count', ]


def count(num):
    def deco(func):
        list_results = []

        @wraps(func)
        def wrapper(*args):
            result = None
            for _ in range(num):
                result = func(*args)
                list_results.append(result)
                print(list_results)
            return result

        return wrapper

    return deco


@count(3)
def nny_func(*args):
    return args


if __name__ == '__main__':
    nny_func('some', 'word', 5)
    nny_func('new')
