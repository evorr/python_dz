import json
from User import User
from ExcepBase import AcsessException, LevelException


class Project:
    def __init__(self, users_list, admin):
        self.users_list = users_list
        self.admin = admin

    @classmethod
    def load(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                usesrs_dict = json.load(f)
        except Exception as e:
            print(f'При открытии файла {filename} возникла ошибка {e}')
            raise
        else:
            users = []
            for row in usesrs_dict:
                users.append(User(row['name'], row['id'], row['level']))
            return Project(users, admin=None)

    def __str__(self):
        str_u = ''
        for user in self.users_list:
            str_u += f' {user.name} {user.id} {user.level} '
        return f'{str_u}\n админ: {self.admin}'

    def enter(self, name, id):
        new_user = User(name, id, level=None)
        if new_user not in self.users_list:
            raise AcsessException(id)
        for user in self.users_list:
            if new_user == user:
                self.admin = user

    def add_user(self, name, id, level):
        if self.admin.level >= level:
            raise LevelException(self.admin.level)
        else:
            self.users_list.append(User(name, id, level))


if __name__ == '__main__':
    p1 = Project.load('users.jso')
    print(p1)
    p1.enter('Lena', 43)
    print(p1)
    p1.add_user('Uri', 32, 4)
    print(p1)