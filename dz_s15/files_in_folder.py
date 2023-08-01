# Напишите код, который запускается из командной строки и получает
# на вход путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import argparse
import os
from collections import namedtuple
import logging

parser = argparse.ArgumentParser(prog='Work with data')
parser.add_argument('-path', metavar='path', type=str, default=os.getcwd())

Obj = namedtuple('Obj', ['name', 'parent_folder', 'file_ext', 'flag_folder'], defaults=[None, 'FILE'])

logging.basicConfig(filename='objects.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def func(path):
    data = []
    for line in os.walk(path):
        *parent_path, parent_folder = line[0].split("\\")
        for file in line[2]:
            file_name, extension = file, None
            if '.' in file:
                file_name, extension = file.rsplit('.', 1)
            o = Obj(file_name, parent_folder, extension)
            logger.info(f'{o.parent_folder} / {o.name}  {o.file_ext}  {o.flag_folder} ')
            data.append(o)
        for dir in line[1]:
            o = Obj(dir, parent_folder, flag_folder='FOLDER')
            logger.info(f'{o.parent_folder} / {o.name}  {o.file_ext}  {o.flag_folder} ')
            data.append(o)


if __name__ == '__main__':
    args = parser.parse_args()
    func(args.path)


r"""
launching in terminsl:
python .\files_in_folder.py -path C:\Users\Лена\Desktop\Python_les\python_dz
python .\files_in_folder.py
"""
