# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions


def reduce_fract(numerator, denominator):
    cut = 1
    for i in range(2, denominator):
        if denominator % i == 0 and numerator% i == 0:
            cut = i
    return cut


def prog(str_1, str_2):
    str_x1, str_x2 = str_1.split('/')
    str_y1, str_y2 = str_2.split('/')
    x1 = int(str_x1)
    x2 = int(str_x2)
    y1 = int(str_y1)
    y2 = int(str_y2)
    numerator_mult = x1 * y1
    denominator_mult = x2 * y2
    cut = reduce_fract(numerator_mult, denominator_mult)
    mult_str = str(int(numerator_mult / cut)) + '/' + str(int(denominator_mult / cut))
    nok = 1
    for i in range(x2, x2 * y2 + 1):
        if i % x2 == 0 and i % y2 == 0:
            nok = i
    numerator_sum = x1 * (nok / x2) + y1 * (nok / y2)
    cut = reduce_fract(numerator_sum, nok)
    sum_str = str(int(numerator_sum / cut)) + '/' + str(int(nok / cut))
    return mult_str, sum_str

aa = '2/6'
bb = '3/4'

mult_fract, sum_fract = prog(aa, bb)

print(f'{aa} + {bb} = {sum_fract}')
print(f'{aa} * {bb} = {mult_fract}')

res_sum = fractions.Fraction(aa) + fractions.Fraction(bb)
res_mult = fractions.Fraction(aa) * fractions.Fraction(bb)
print(res_sum, res_mult)
