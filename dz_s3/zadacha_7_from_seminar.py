# Пользователь вводит строку текста
# Подсчитайте сколько раз встречается каждая буква в строке
# без использования метода count() и с ним
# Результат сохраните в словаре, где ключ - символ,
# а значение - частота встречи символа в строке
# Обратите внимание на порядок ключей. Объясните, почему
# они совпадают или не совпадают в ваших решениях

data = input(': ')

symbols_dict = {}
for symbol in data.replace(' ', '').replace(',', '').replace('.', '').replace('-', ''):
    symbols_dict[symbol] = symbols_dict.get(symbol, 0) + 1

symbols_dict_2 = {}
for symbol in data.replace(' ', '').replace(',', '').replace('.', '').replace('-', ''):
    if symbol not in symbols_dict_2:
        symbols_dict_2[symbol] = data.count(symbol)


print(symbols_dict)
print(symbols_dict_2)

#for key, value in symbols_dict.items():
#    print(key, '-', value)