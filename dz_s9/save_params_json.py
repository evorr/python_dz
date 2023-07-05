# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции
# и результат, который она возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться. Каждый ключевой параметр сохраните
# как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные,
# так и ключевые аргументы. Имя файла должно совпадать с именем декорируемой
# функции.
import json
import os
from functools import wraps
__all__ = ['get_any', 'deco', ]

def deco(func):
    @wraps(func)
    def wrapper(num, *args, **kwargs):
        print('wrap json')
        filename = 'params.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                list_file = json.load(file)
        else:
            list_file = []
        result = func(num, *args, **kwargs)
        print(result)
        list_file.append({
            'args': (num, args, kwargs),
            'result': result
        })
        print(list_file)
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(list_file, file, indent=1)
        return result

    return wrapper


@deco
def get_any(num, *args, **kwargs):
    return num


if __name__ == '__main__':
    my_dict = {1: 1, 2: 2}
    get_any(1, 11, 22, 33, my_dict, hex=7)
