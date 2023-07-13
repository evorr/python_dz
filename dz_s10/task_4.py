# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь
from Human import Human
from random import randint


class Employee(Human):
    accsess_div = 7

    def __init__(self, id, *args, **kwargs):
        self.id = id # randint(100000, 999999)
        self.__access = sum(list(map(int, str(self.id)))) % self.accsess_div
        super().__init__(*args, **kwargs)

    def get_access(self):
        return self.__access

    def check_id(self):
        if self.id < 100000 or self.id > 999999:
            self.id = randint(100000, 999999)
        return self.id


if __name__ == '__main__':
    e1 = Employee('Ivanov', 'Maxim', 'Fedorovich', 34)
    print(e1.full_name(), e1.get_age())
    print(e1.id)
    print(e1.get_access())
    e1.birthday()
    print(e1.get_age())
