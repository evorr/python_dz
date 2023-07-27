class ArchiveException(Exception):
    pass


class IsDigitException(ArchiveException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value} не является int или float'
