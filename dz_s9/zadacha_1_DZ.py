# Напишите следующие функции:
# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json
import os.path
from random import randint
import csv

__all__ = ['create_csv', 'quadratic_equation', 'deco_save_param_result']


def deco_save_param_result(func):
    def wrapper(a, b, c):
        filename = 'results.json'
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                list_file = json.load(file)
        else:
            list_file = []
        result = func(a, b, c)
        list_file.append({' '.join(map(str, (a, b, c))): result})
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(list_file, file, indent=1)
        return result

    return wrapper


def deco_quadr_eq_from_csv(func):
    def wrapper():
        with open('numbers.csv', 'r', newline='', encoding='utf-8') as file:
            numbers = csv.reader(file)
            for line in numbers:
                func(*(map(int, line)))

    return wrapper


@deco_quadr_eq_from_csv
@deco_save_param_result
def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x_1 = (-b - discriminant ** 0.5) / (2 * a)
        x_2 = (-b + discriminant ** 0.5) / (2 * a)
        return x_1, x_2
    elif discriminant == 0:
        x = -(b / (2 * a))
        return x
    else:
        return 'no roots'


def create_csv():
    with open('numbers.csv', 'w', newline='', encoding='utf-8') as file:
        list_numbers = [[randint(1, 20), randint(1, 20), randint(1, 20)] for _ in range(100)]
        csv_write = csv.writer(file)
        csv_write.writerows(list_numbers)


if __name__ == '__main__':
    create_csv()
    quadratic_equation()
