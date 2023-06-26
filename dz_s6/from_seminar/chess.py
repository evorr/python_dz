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
                print(f'{coord_tuple[i]} and {coord_tuple[s_i]} in straight line')
                return False
            if coord_tuple[s_i] in set_diagonal:
                print(f'{coord_tuple[i]} and {coord_tuple[s_i]} in diagonal line')
                return False
    return True


if __name__ == '__main__':
    coordinates = ((3, 5), (4, 4), (7, 4), (6, 1), (8, 7), (1, 6), (2, 2), (5, 3))
    result = func(coordinates)
    print(result)
