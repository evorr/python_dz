# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц
from random import randint


class Matrix:
    def __init__(self, array=None, rows=None, col=None, high=None):
        if not array:
            self.matrix = [[randint(1, high) for _ in range(0, col)] for _ in range(0, rows)]
        else:
            self.matrix = array

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
            new_matrix = [[i_s + i_o for i_s, i_o in zip(r_s, r_o)] for r_s, r_o in zip(self.matrix, other.matrix)]
            return Matrix(array=new_matrix)
        return 'количество столбцов и/или строк матриц не совпадает'

    def __mul__(self, other):
        new_matrix = [[0 for _ in range(0, len(self.matrix))] for _ in range(0, len(self.matrix))]
        for i in range(0, len(new_matrix)):
            for j in range(0, len(new_matrix)):
                for k in range(0, len(self.matrix[i])):
                    new_matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return Matrix(array=new_matrix)

    def __str__(self):
        res = ''
        for row in self.matrix:
            res += f'{row}\n'
        return res


a = Matrix(rows=3, col=4, high=2)
b = Matrix(rows=4, col=3, high=4)
print(a)
print()
print(b)
print(a.__eq__(b))
print(a.__gt__(b))
c = a.__add__(b)
print(c)
d = a.__mul__(b)
print(d)
