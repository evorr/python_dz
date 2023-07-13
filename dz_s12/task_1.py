# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k рассчитанных факториалов.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.
from math import factorial


class Factorial:
    def __init__(self, k):
        self._k = k
        self._history = []

    def __call__(self, num):
        m = 1
        for n in range(1, num):
            m *= n
        self._history.append({num: m})
        if len(self._history) > self._k:
            self._history = self._history[-self._k]
        return m

    def get_history(self):
        return self._history



# МОЕ РЕШЕНИЕ !!!!:

#class Factorial:
    #def __init__(self):
        #self.history = []

    #def __call__(self, value, k):
        #res = 1
        #for i in range(1, value + 1):
            #res *= i
            #if value - k < i:
                #self.history.append(res)
        #return self.history
        # аналог:
        #for i in range(1, value + 1):
         #   self.history.append(factorial(i))
        #return self.history[-k:]


#f = Factorial()
#print(f(6, 4))
