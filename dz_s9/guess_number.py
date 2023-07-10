# Создайте функцию-замыкание, которая принимает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.
__all__ = ['two_nums', ]


def two_nums(num, attempt):
    def func():
        count = 0
        while count < attempt:
            number_user = int(input(f'Введите число от 1 до 100: '))
            if number_user == num:
                return f'угадали, загаданное чсило - {num}'
            elif number_user > num:
                count += 1
                print('меньше\nпопытка - ', count)
            elif number_user < num:
                count += 1
                print('больше\nпопыткак - ', count)
        if count == attempt:
            return f'загаданное чсило - - {num}'

    return func


if __name__ == '__main__':
    res = two_nums(10, 5)
    res()
