# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def func(**kwargs):
    param_dict = {}
    for key, value in kwargs.items():
        if type(value) in [list, set, bytearray, dict]:
            value = str(value)
        param_dict[value] = key
    print(param_dict)


func(math=5, mause='razer', numbers=[1, 2, 3], more_numbers=(4, 5, 7))