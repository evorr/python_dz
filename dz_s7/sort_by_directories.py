# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

import os

__all__ = ['sort_file', ]

DCT = {'Video': ('avi', 'mp4', 'mkv'),
       'Images': ('gif', 'jpg', 'tiff'),
       'Text': ('txt', 'rtf')}


def sort_file(dir_start):
    os.chdir(dir_start)
    files = [file for file in os.listdir() if os.path.isfile(file)]
    for fold, ext in DCT.items():
        if fold not in os.listdir():
            os.mkdir(fold)
        for file in files:
            if file.split('.')[1] in ext:
                os.replace(file, os.path.join(os.getcwd(), fold, file))


if __name__ == '__main__':
    sort_file('C:\\Users\Лена\Downloads')
