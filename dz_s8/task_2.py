# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# в пределах одного уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.
import json
import os

__all__ = ['func', ]


def func(file_json):
    if os.path.isfile(file_json):
        with open(file_json, 'r', encoding='utf-8') as f:
            dct = json.load(f)
    else:
        dct = {str(i): {} for i in range(1, 8)}

    while True:
        data = input('Enter the name, ID, and access level separated by a space: ')
        if data == '':
            break
        else:
            user_input, id, access = data.split()
            # if id not in dct[access] and dct[access][id] == user_input:
            if id not in dct[access]:
                dct.setdefault(access, {id: user_input})[id] = user_input
                print(dct)
    with open(file_json, 'w', encoding='utf-8') as fs:
        json.dump(dct, fs, ensure_ascii=False)


if __name__ == '__main__':
    func('text.json')
