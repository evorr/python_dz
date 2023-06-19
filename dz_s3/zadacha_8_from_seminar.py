# Три друга взяли вещи в поход. Сформируйте словарь,
# где ключ - имя друга, а значение - кортеж вещей.
# Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей, кроме одного и имя того,
# у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей
#
dict_items = {'Ivan': ('рюкзак', 'карта', 'компас', 'палатка', 'вода', 'палка'),
          'Petr': ('рюкзак', 'хлеб', 'пластырь', 'палатка', 'вода', 'спальник'),
          'Vasya': ('рюкзак', 'хлеб', 'пластырь', 'вода', 'фонарик', 'нож')}
some_list = []
for name in dict_items:
    some_list.append(set(dict_items[name]))
every_has = set.intersection(*some_list)
print(f'вещи взяли все {every_has}')


for name in dict_items:
    some_list.remove(set(dict_items[name]))
    uniq = set(dict_items[name]).difference(*some_list)
    doesnt_have = set.intersection(*some_list).difference(set(dict_items[name]))
    some_list.append(set(dict_items[name]))
    print(f'Есть только у {name} {uniq}')
    print(f'Нет только у {name} {doesnt_have}')