# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


dev = 16
dict_hex = '0123456789abcdef'

numer = int(input('Число: '))


def num_to_hex(num):
    res = ''
    while num > 0:
        if num in dict_hex:
            res = dict_hex[num] + res
        elif num % dev in dict_hex:
            res = dict_hex[num % dev] + res
        else:
            res = str(num % dev) + res
        num = num // dev
    print(res)


num_to_hex(numer)
print(hex(numer))
