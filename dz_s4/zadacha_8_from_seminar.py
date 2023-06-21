# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

names = 'ivan'
cities = 'samara'
numbers = 34
purchase = [23, 56, -3]
toolbox = ('hammer', 'side cutters')
s = {'a': 1, 'b': 2}


def replace_value():
    dict_words = {}
    for k, v in globals().items():
        if not k.startswith('_') and k != 'replace_value':
            dict_words[k] = v
    print(dict_words)
    new_dict = {}
    for key in dict_words:
        if key.endswith('s') and key != 's':
            new_dict[key.rstrip('s')] = dict_words[key]
            dict_words[key] = None
    print(dict_words)
    print(new_dict)


replace_value()