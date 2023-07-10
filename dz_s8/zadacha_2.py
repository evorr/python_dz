# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle

__all__ = ['print_pickle_str', ]


def print_pickle_str(file_csv):
    with open(file_csv, 'r', encoding='utf-8') as fc:
        read_file = list(csv.reader(fc))
        print(pickle.dumps(read_file))


if __name__ == '__main__':
    print_pickle_str('users.csv')
