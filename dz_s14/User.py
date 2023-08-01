class User:
    def __init__(self, name, id, level):
        self.name = name
        self.id = id
        self.level = level

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __str__(self):
        return f'{self.name} {self.id} {self.level}'


def func(dct_users):
    i = 1
    while True:
        data = input('Enter the name, ID, and access level separated by a space: ')
        if data == '':
            break
        else:
            name, id, access = data.split()
            dct_users[i] = User(name, id, access)
            i += 1