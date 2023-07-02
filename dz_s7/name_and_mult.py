# Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

import typing

__all__ = ['func', ]


def read_per_line(file_obj: typing.TextIO):
    line = file_obj.readline()
    if line == '':
        file_obj.seek(0)
        line = file_obj.readline()
    return line[:-1]


def func(names, numbers, results):
    with(
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(results, 'w', encoding='utf-8') as f_results
    ):
        len1 = sum(True for _ in f_numbers)
        len2 = sum(True for _ in f_names)

        for _ in range(max(len1, len2)):
            names = read_per_line(f_names)
            nums = read_per_line(f_numbers)
            res_sum = int(nums.split("|")[0]) * float(nums.split("|")[1])
            if res_sum > 0:
                f_results.write(f'{str(names.lower())}, {int(res_sum)}\n')
            else:
                f_results.write(f'{str(names.title())}, {str(res_sum)}\n')


if __name__ == '__main__':
    func('names.txt', 'text.txt', 'new_file.txt')
