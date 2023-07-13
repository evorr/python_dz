# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам
# для каждого предмета и по оценкам всех предметов вместе взятых.
import csv
from random import randint


class Check:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return self.name

    def __set__(self, instance, value):
        self.validate(value)
        self.name = value

    def validate(self, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError(f'В {value} должно быть только буквы, первая - заглавная')


class Student:
    last_name = Check()
    first_name = Check()
    patronymic = Check()

    def __init__(self, last_name, first_name, patronymic):
        self.__courses = self.get_courses()
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    def get_courses(self):
        with open('test_pred.csv', 'r', encoding='utf-8', newline='') as file:
            csv_reader = csv.reader(file)
            res = {}
            for line in csv_reader:
                course, *value = line
                grades_c = list(map(int, value[:value.index('tests')]))
                grades_t = list(map(int, value[value.index('tests') + 1:]))
                grades_c.append({'tests': grades_t})
                res[course] = grades_c
            return res

    def aver_test_score_subj(self):
        res_str = ''
        for subj, grades in self.__courses.items():
            aver_tests = sum(grades[-1]['tests']) / len(grades[-1]['tests'])
            res_str += f'{subj} test average score: {round(aver_tests, 1)} \n'
        return res_str

    def aver_score_all_subj(self):
        all_grades = [nums for grades in self.__courses.values() for nums in grades[:-1]]
        aver_subj = sum(all_grades) / len(all_grades)
        return f'средний балл по оценкам всех предметов вместе взятых {aver_subj}'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}\n{self.__courses}'




def create_grades():
    courses = ['math', 'geography', 'chemistry', 'literature']
    with open('test_pred.csv', 'w', encoding='utf-8', newline='') as file:
        csv_write = csv.writer(file)
        for item in courses:
            line = [item, *[randint(2, 5) for _ in range(5)], 'tests', *[randint(0, 100) for _ in range(3)]]
            csv_write.writerow(line)


create_grades()
s1 = Student('Smit', 'Will', 'Jhonov')
print(s1)
print(s1.aver_test_score_subj())
print(s1.aver_score_all_subj())
#s2 = Student('Smit', 'jhon', 'Ivanov1ch')
#print(s2)
#s1.__courses['math'] = [5, 5, 5, 5, 5, {'tests': [90, 92, 96]}]
#print(s1)
