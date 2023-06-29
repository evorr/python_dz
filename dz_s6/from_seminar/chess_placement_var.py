# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки
# ферзей в задаче выше. Проверяйте различные случайные варианты
# и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок
from random import randint
__all__ = ['create_coordinates', 'func', 'turn_ninety', 'check']

def create_coordinates():
    random_coord = set()
    while len(random_coord) != 8:
        random_coord.add((randint(1, 8), randint(1, 8)))
    return tuple(random_coord)


def func(coord_tuple):
    for i in range(len(coord_tuple) - 1):
        x, y = coord_tuple[i]
        set_diagonal = set()
        while x <= 8 and y <= 8:
            set_diagonal.add((x, y))
            x += 1
            y += 1
        x, y = coord_tuple[i]
        while x >= 1 and y >= 1:
            set_diagonal.add((x, y))
            x -= 1
            y -= 1
        x, y = coord_tuple[i]
        while x >= 1 and y <= 8:
            set_diagonal.add((x, y))
            x -= 1
            y += 1
        x, y = coord_tuple[i]
        while x <= 8 and y >= 1:
            set_diagonal.add((x, y))
            x += 1
            y -= 1
        for s_i in range(i + 1, len(coord_tuple)):
            if coord_tuple[i][0] == coord_tuple[s_i][0] or coord_tuple[i][1] == coord_tuple[s_i][1]:
                return False
            if coord_tuple[s_i] in set_diagonal:
                return False
    return True


def turn_ninety(coords):
    new_coords = set()
    for i in range(len(coords)):
        new_coords.add((coords[i][1], 9 - coords[i][0]))
    return tuple(new_coords)


def check():
    attempt = 0
    res = False
    while not res:
        coord = create_coordinates()
        if func(coord):
            print(attempt, coord, 'НЕ ПЕРЕСЕКАЮТСЯ ')
            new_2 = turn_ninety(coord)
            new_3 = turn_ninety(new_2)
            new_4 = turn_ninety(new_3)
            print(f'{new_2}\n{new_3}\n{new_4}')
            print(*map(func, (new_2, new_3, new_4)))
            res = True
        attempt += 1

if __name__ == '__main__':
    check()
