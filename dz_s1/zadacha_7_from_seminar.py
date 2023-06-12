# Пользователь вводит число от 1 до 999. Используя операции с числами сообщите, что введено:
# цифра, двузначное число или трехзначное число
# Для цифры верните ее квадрат, например 5 - 25
# Для двузначного числа - произведение цифр, например 30 - 0
# Для трехзначного числа его трехначное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических числе
# В коде должны быть один input и один print


def get_number():
    number_user = int(input('Введите число от 1 до 999: '))
    if number_user > 999 or number_user < 0:
        return get_number()
    else:
        return number_user


number = get_number()
print(number)
number_2 = 0


def find_count(number):
    count = 0
    while number > 0:
        number = (number / 10) - (number % 10 / 10)
        count += 1
    return count

def find_type_result(number, number_2):
    count = find_count(number)
    if count == 1:
        number_t = 'цифра'
        number_2 = number * number
    elif count == 2:
        number_t = 'двузначное число'
        number_2 = ((number / 10) - (number % 10 / 10)) * (number % 10)
    else:
        number_t = 'трехзначное число'
        num_for_count = number
        while num_for_count > 0:
            btw_res = num_for_count % 10
            if btw_res == 0:
                number_2 = number_2 * 10
            else:
                number_2 = (number_2 * 10) + num_for_count % 10
            num_for_count = (num_for_count / 10) - (num_for_count % 10 / 10)
    print(number_t, number, ' - ', number_2)


find_type_result(number, number_2)
