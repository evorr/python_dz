# Пользователь вводит строку текста.
# Вывести каждое слово с новой строки
# Строки нумеруются начиная с единицы
# Слова выводятся отсортированными согласно кодировке Unicode
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки


data = input(': ')

data_list = data.split(' ')
indent = len(max(data_list, key=len))
for num, item in enumerate(sorted(data_list), start=1):
    print(f'{num} {item:>{indent}}')