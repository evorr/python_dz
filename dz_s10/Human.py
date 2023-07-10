# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.


class Human:
    def __init__(self, surname, name, patronym, age):
        self.surname = surname
        self.name = name
        self.patronym = patronym
        self.__age = age

    def birthday(self):
        self.__age += 1

    def full_name(self):
        return f'{self.surname} {self.name} {self.patronym}'

    def get_age(self):
        return self.__age

if __name__ == '__main__':
    h1 = Human('Petorv', 'Andrei', 'Andreevich', 16)
    print(h1.full_name())
    print(h1.get_age())
    h1.birthday()
    print(h1.get_age())
    h1.__age = 20
    print(h1.__age)
    print(h1.get_age())
