# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции.

import csv
import json

__all__ = ['func', ]


def func(csv_file, json_file):
    with(
        open(csv_file, 'r', encoding='utf-8') as csv_f,
        open(json_file, 'w', encoding='utf-8') as json_f
    ):
        file = [*csv.reader(csv_f)]
        header_id, header_name, header_access = file[0]
        lst = []
        for id, access, name in file[1:]:
            lst.append({'id': id, 'name': name, 'access': access, 'hash': hash(name + id)})
            # lst.append({header_id: id, header_name: name, header_access: access, 'hash': hash(name + id)})
        json.dump(lst, json_f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    func('new_csv.csv', 'users.json')

# def from_cvs_to_json(file_csv, file_json):
# with(
# open(file_csv, 'r', newline='', encoding='utf-8') as file_c,
# open(file_json, 'w', encoding='utf-8') as file_j
# ):
# csv_file = csv.reader(file_c)
# for line in csv_file:
# id = int(line[0]) + randint(1000000000, 9999999989)
# name = line[2].capitalize()
# hash_obj = hash((name, id))
# dct = {line[1]: {id: name}}
# print(dct)
# json.dump(dct, file_j, indent=1)
