# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv

__all__ = ['from_pickle_to_csv', ]


def from_pickle_to_csv(file_pickle, file_csv):
    with(
        open(file_pickle, 'rb') as fp,
        open(file_csv, 'w', newline='', encoding='utf-8') as fc
    ):
        list_of_dict = pickle.load(fp)
        all_keys = list_of_dict[0].keys()
        writer = csv.DictWriter(fc, fieldnames=all_keys, delimiter=' ')
        writer.writeheader()
        writer.writerows(list_of_dict)


if __name__ == '__main__':
    from_pickle_to_csv('users.pickle', 'users.csv')
