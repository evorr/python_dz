# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest

from Project import Project
from ExcepBase import AcsessException, LevelException
from User import User

@pytest.fixture
def create_instance():
    p1 = Project.load('users.json')
    return p1


def test_load(create_instance):
    assert type(create_instance) == Project


def test_load_excep():
    with pytest.raises(Exception):
        Project.load('users.jso')


def test_enter(create_instance):
    create_instance.enter('Leo', 23)
    assert create_instance.admin.name == 'Leo'


def test_enter_excep():
    with pytest.raises(AcsessException):
        p1 = Project.load('users.json')
        p1.enter('Leo', 24)


def test_add_user(create_instance):
    create_instance.enter('Leo', 23)
    create_instance.add_user('Maria', 8, 6)
    assert (User('Maria', 8, 6) in create_instance.users_list) == True


def test_add_user_excep():
    with pytest.raises(LevelException):
        p1 = Project.load('users.json')
        p1.enter('Leo', 23)
        p1.add_user('Maria', 8, 2)


