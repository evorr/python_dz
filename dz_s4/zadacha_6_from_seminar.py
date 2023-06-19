# Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def func(num_list, ind1, ind2):
    result = 0
    start_ind = 0
    end_ind = len(num_list)
    if 0 <= ind1 <= end_ind:
        start_ind = ind1
    if 0 <= ind2 <= end_ind:
        end_ind = ind2
    for i in range(start_ind, end_ind):
        result += num_list[i]
    return result


res_sum = func([1, 2, 3, 4, 6, 0], -2, 8)
print(res_sum)