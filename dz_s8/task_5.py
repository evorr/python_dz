# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде
# одноимённых pickle файлов.
import json
import os
import pickle

__all__ = ['func', ]


def func(folder):
    for file in os.listdir(folder):
        if file[-4:] == 'json':
            with (open(file, 'r', encoding='utf-8') as f,
                  open(file[:-4] + 'pickle', 'wb') as fp):
                res = json.load(f)
                pickle.dump(res, fp)


if __name__ == '__main__':
    func(os.getcwd())
    with open('users.pickle', 'rb') as file:
        print(pickle.load(file))
