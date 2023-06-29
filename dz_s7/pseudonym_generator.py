# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохранить в файл.
import random

__all__ = ['save_names', ]


def save_names(num, name):
    literals = 'qwertyuiopasdfghjklzxcvbnm'
    vowels = 'eyuioa'
    min_len = 4
    max_len = 7
    with open(name, 'w', encoding='utf-8') as file:
        for _ in range(num):
            name = random.sample(literals, random.randint(min_len, max_len))
            if not set(name) & set(vowels):
                half = len(name) // 2
                name = name[:half] + random.sample(vowels, half)
                random.shuffle(name)
            name = ''.join(name).capitalize()
            file.write(f'{name}\n')


if __name__ == '__main__':
    save_names(10, 'names.txt')
