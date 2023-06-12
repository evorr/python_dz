## Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
## Используйте правило для проверки: "Число является простым, если делится нацело только на единицу
## и на себя". Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def get_number():
    number_user = int(input('Введите число от 1 до 100 000: '))
    if number_user > 100000 or number_user < 0:
        return get_number()
    else:
        return number_user


def check(number_from):
    number_of_divisors = 1
    divisor = 2
    for i in range(divisor, number_from + 1):
        if number_from % i == 0:
            number_of_divisors += 1
    if number_of_divisors > 2:
        print('Составное число')
    else:
        print('Простое число')


number = get_number()
check(number)
