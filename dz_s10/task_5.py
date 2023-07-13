# Создайте три (или более) отдельных классов животных.
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства,
# например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Birds:

    def __init__(self, name, color, wingspan):
        self.name = name
        self.color = color
        self.wingspan = wingspan

    def specific(self):
        return self.wingspan


class Fish:
    def __init__(self, name, color, fin):
        self.name = name
        self.color = color
        self.fin = fin

    def specific(self):
        return self.fin


class Mammal:
    def __init__(self, name, color, hibernate):
        self.name = name
        self.color = color
        self.hibernate = hibernate

    def specific(self):
        return self.hibernate
