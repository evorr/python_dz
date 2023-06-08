## Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна
## подсказывать "больше" или "меньше" после каждой попытки. Для генерации случайного числа используйте
## код:
## from random import randint
## num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)
ATTEMPTS = 10
while ATTEMPTS > 0:
    number_user = int(input('Введите число от 1 до 100 000: '))
    if number_user == secret_number:
        print('угадали, загаданное чсило - ', secret_number)
        break
    elif number_user > secret_number:
        ATTEMPTS -= 1
        print('меньше\nосталось попыток - ', ATTEMPTS)
    elif number_user < secret_number:
        ATTEMPTS -= 1
        print('больше\nосталось попыток - ', ATTEMPTS)
if ATTEMPTS == 0:
    print('загаданное чсило - ', secret_number)
