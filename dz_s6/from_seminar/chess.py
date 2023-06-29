# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить
# 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
__all__ = ['func']


def func(coord_tuple):
    for item in coord_tuple:
        for next_item in coord_tuple[coord_tuple.index(item) + 1:]:
            if item[0] == next_item[0] \
                    or item[1] == next_item[1] \
                    or abs(item[0] - next_item[0]) == abs(item[1] - next_item[1]):
                print(f'{item} and {next_item} in line')
                return False
    return True


if __name__ == '__main__':
    coordinates = ((7, 1), (5, 2), (3, 3), (1, 4), (6, 5), (8, 6), (2, 7), (4, 8))
    result = func(coordinates)
    print(result)
