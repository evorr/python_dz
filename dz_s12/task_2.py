# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.
import json


class Factorial:
    def __init__(self):
        self.history = []

    def __call__(self, value, k):
        res = 1
        for i in range(1, value + 1):
            res *= i
            if value - k < i:
                self.history.append({i: res})
        return self.history

    def __enter__(self):
        return self.history

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial.json', 'w', encoding='utf-8') as file:
            json.dump(self.history, file)


factorial = Factorial()
with factorial as f:
    factorial(6, 4)

