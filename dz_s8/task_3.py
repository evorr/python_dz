# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.
import csv
import json

__all__ = ['save_csv', ]


def save_csv(file_json):
    with(
        open(file_json, 'r', encoding='utf-8') as fj,
        open('new_csv.csv', 'w', newline='', encoding='utf-8') as fc
    ):
        dict_json = json.load(fj)
        rows = []
        for level, in_dict in dict_json.items():
            for id, name in in_dict.items():
                rows.append({'id': id, 'level': int(level), 'name': name})
        print(rows)
        csv_write = csv.DictWriter(fc, fieldnames=['id', 'level', 'name'])
        csv_write.writerows(rows)


if __name__ == '__main__':
    save_csv('text.json')
