# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json
__all__ = ['func', ]


def func(file):
    dict_res = {}
    with (
        open(file, 'r', encoding='utf-8') as f1,
        open('new_file.json', 'w') as f2
    ):
        for line in f1:
            name, number = line.split()
            dict_res[name.capitalize()] = number
        json.dump(dict_res, f2, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    func('new_file.txt')