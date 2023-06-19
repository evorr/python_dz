# Напишите функцию для транспонирования матрицы


def transposition(old_matrix):
    new_matrix = zip(*old_matrix)
    for line in new_matrix:
        print(line)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
transposition(matrix)