# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс
# Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name):
        self.name = name


class Birds(Animal):
    prop = {
        1: 'fly',
        2: 'not fly'
    }

    def __init__(self, name, specific):
        super().__init__(name)
        self.specific = self.prop[specific]

    def get_specific(self):
        return self.specific


class Fish(Animal):
    prop = {
        1: 'presnovod',
        2: 'sea'
    }

    def __init__(self, name, specific):
        super().__init__(name)
        self.specific = self.prop[specific]

    def get_specific(self):
        return self.specific


class Mammal(Animal):
    prop = {
        1: 'smoke',
        2: 'dont smoke'
    }

    def __init__(self, name, specific):
        super().__init__(name)
        self.specific = self.prop[specific]

    def get_specific(self):
        return self.specific


if __name__ == '__main__':
    a1 = Fish('karas', 1)
    print(a1.get_specific())
