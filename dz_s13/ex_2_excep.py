class HumanException(Exception):
    pass


class NameException(HumanException):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.name} содержит цифры или символы'


class AgeException(HumanException):
    def __init__(self, age):
        self.age = age

    def __str__(self):
            return f'Возраст не может быть меньше 0 и должен быть целым числом. Вы ввели {self.age}'
