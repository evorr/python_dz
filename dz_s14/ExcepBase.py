class BaseException(Exception):
    pass


class LevelException(BaseException):
    def __init__(self, level):
        self.level = level

    def __str__(self):
        return f'{self.level} не подходит уровень'


class AcsessException(BaseException):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'{self.id} не подходит пользователь'
