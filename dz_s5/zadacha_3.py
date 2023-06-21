# Создайте функцию генератор чисел Фибоначчи
# https://ru.wikipedia.org/
# wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8

def fib_gen(n):
    x = 0
    y = 1
    for i in range(0, n):
        yield x
        x, y = y, x + y


a = fib_gen(15)
print(*a)