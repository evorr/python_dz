# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции
from random import randint, uniform

__all__ = ['fill_file', ]

MIN = -1000
MAX = 1000


def fill_file(count_str, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(count_str + 1):
            f.write(f'{randint(MIN, MAX)}|{round(uniform(MIN, MAX), 2)}\n')


if __name__ == '__main__':
    fill_file(5, 'text.txt')