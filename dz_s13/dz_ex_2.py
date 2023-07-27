# Возьмите 1-3 задачи из тех, что были на прошлых семинарах
# или в домашних заданиях. Напишите к ним классы исключения
# с выводом подробной информации. Поднимайте исключения внутри
# основного кода.
# Например нельзя создавать прямоугольник со сторонами отрицательной длины.


# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

from ex_2_excep import AgeException, NameException


class Human:
    def __init__(self, surname, name, patronym, age):
        if not isinstance(age, int) or age < 0:
            raise AgeException(age)
        for elem in [surname, name, patronym]:
            if not elem.isalpha():
                raise NameException(elem)
        self.__age = age
        self.surname = surname
        self.name = name
        self.patronym = patronym

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age

    def full_name(self):
        return f'{self.surname} {self.name} {self.patronym}'


if __name__ == '__main__':
    h1 = Human('Petorv', 'Andrei', 'Andreevich', 16)
    print(h1.full_name())
    print(h1.get_age())
    h2 = Human('Cvetkov', 'Ivan', 'Alexandrovich', 16.4)
    print(h2.full_name())
    print(h2.get_age())
    h3 = Human('Ivanova', 'Anna5', 'Alexandrovna', 87)
    print(h3.full_name())
    print(h3.get_age())
