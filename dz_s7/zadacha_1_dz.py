# Дорабатываем функции из предыдущих задач.
# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
import string
from pathlib import Path
from random import randint, choices

__all__ = ['create_dif_files', ]


def create_files(ext, min_len=6, max_len=30, min_b=256, max_b=4096, quant=42, dir=None):
    if Path.cwd() != dir:
        os.chdir(dir)
    for _ in range(quant):
        name_length = randint(min_len, max_len)
        file_name = ''.join(choices(string.ascii_letters + string.digits, k=name_length)) + '.' + ext
        if Path(file_name).exists():
            file_name = file_name[:-(len(ext) + 1)] + '_2' + file_name[-(len(ext) + 1):]
        file_size = randint(min_b, max_b)
        random_bytes = os.urandom(file_size)
        with open(file_name, 'wb') as file:
            file.write(random_bytes)


def create_dif_files(folder, **kwargs):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    path_fold = Path.cwd() / folder
    for ext, num in kwargs.items():
        create_files(ext, quant=num, dir=path_fold)


if __name__ == '__main__':
    create_dif_files('test', txt=2, bin=1)
