# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

data = 'C:Users\Лена\Desktop\prorgamm567k.txt'


def func(text):
    *path, file = text.split("\\")
    name, extension = file.split('.')
    return path, name, extension


a = func(data)
print(a)
