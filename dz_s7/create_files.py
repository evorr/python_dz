# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.
import os
import string
from random import randint, choices

__all__ = ['create_files', ]


def create_files(ext, min_len=6, max_len=30, min_b=256, max_b=4096, quant=42):
    for _ in range(quant):
        name_length = randint(min_len, max_len)
        file_name = ''.join(choices(string.ascii_letters + string.digits, k=name_length)) + '.' + ext
        file_size = randint(min_b, max_b)
        random_bytes = os.urandom(file_size)
        with open(file_name, 'wb') as file:
            file.write(random_bytes)


if __name__ == '__main__':
    create_files(ext='txt', quant=2)
