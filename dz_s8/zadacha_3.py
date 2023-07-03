# Напишите функцию, которая получает на вход директорию
# и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом
# всех вложенных файлов и директорий.
import json
import os
import csv
import pickle

__all__ = ['size_folder', 'func', ]


def size_folder(folder):
    size = 0
    list_obj = os.walk(folder)
    for item in list_obj:
        for fold in item[1]:
            folder_size = size_folder(fold)
            size += folder_size
        for file in item[2]:
            file_size = os.path.getsize(os.path.join(item[0], file))
            size += file_size
    return size


def func(folder):
    dict_result = {}
    for line in os.walk(folder):
        parent = ''
        if line[0] != folder:
            *parent_path, parent = line[0].split("\\")
        for file in line[2]:
            file_size = os.stat(line[0] + "\\" + file).st_size
            dict_result[file] = {'type': 'file', 'size': file_size, 'parent': parent}
        for dir in line[1]:
            size_f = size_folder(os.path.join(line[0], dir))
            dict_result[dir] = {'type': 'folder', 'size': size_f, 'parent': parent}
    with(
        open('result.json', 'w', encoding='utf-8') as fj,
        open('result.csv', 'w', newline='', encoding='utf-8') as fc,
        open('result.pickle', 'wb') as fp
    ):
        json.dump(dict_result, fj, ensure_ascii=False, indent=1)
        rows_dict = []
        for key, value in dict_result.items():
            row = {'object': key}
            for sub_key, sub_value in value.items():
                row[sub_key] = sub_value
            rows_dict.append(row)
        writer = csv.DictWriter(fc, fieldnames=['object', 'type', 'size', 'parent'], restval=None, delimiter=' ')
        writer.writeheader()
        writer.writerows(rows_dict)
        pickle.dump(rows_dict, fp)


if __name__ == '__main__':
    func(r"C:\Users\Лена\Desktop\Python_les\python_dz\dz_s8")
    # func(r"C:\Users\Лена\Desktop\Python_les\python_dz")
    with open('result.pickle', 'rb') as file:
        print(pickle.load(file))
