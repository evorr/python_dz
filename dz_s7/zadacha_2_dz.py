# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# * При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
import os
from random import choice
from pathlib import Path

__all__ = ['rename_file', ]


def rename_file(new_names, old_ext=None, new_ext=None, dir=os.getcwd()):
    os.chdir(Path.cwd() / dir)
    count = 1
    for file in os.listdir():
        if file[-(len(old_ext)):] == old_ext and file[:-(len(old_ext))] not in new_names:
            Path(file).rename(file[:-(len(old_ext) + 1)] + '_' + choice(new_names) + '_' + str(count) + '.' + new_ext)
            count += 1


if __name__ == '__main__':
    rename_file(['AA', 'BB', 'CC'], old_ext='md', new_ext='csv')
