# Объедините функции из прошлых задач.
# Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.
from save_params_json import deco as save_params
from guess_number_with_check import deco as check_val
from multiple_run_func import count
__all__ = ['game', ]

@count(2)
#@save_params
#@check_val
def game(num, attempt):
    count = 0
    while count < attempt:
        number_user = int(input(f'Введите число от 1 до 100: '))
        if number_user == num:
            print(f'угадали, загаданное чсило - {num}')
            return 1
        elif number_user > num:
            count += 1
            print('меньше\nпопытка - ', count)
        elif number_user < num:
            count += 1
            print('больше\nпопытка - ', count)
    if count == attempt:
        print(f'загаданное чсило - - {num}')
        return 0


if __name__ == '__main__':
    game(43, 6)

