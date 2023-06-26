# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, из предыдущей задачи, чтобы передать ей все свои загадки.
__all__ = ['saved_riddles', 'func']
ATTEMPTS = 3


def func(riddle, answers, attempts):
    print(riddle)
    for attempt in range(1, attempts + 1):
        answer = input('Ответ: ')
        if answer in answers:
            print(f'угадали с {attempt} попытки')
            return attempt
        else:
            print('неверно')
    print('кончились попытки')
    return 0


def saved_riddles():
    riddles_dict = {'Музыкант, певец, рассказчик — А всего труба да ящик.': ['граммофон', 'радио'],
                    'На раскрашенных страницах Много праздников хранится.': ['календарь', 'график'],
                    'Ах, не трогайте меня: Обожгу и без огня!': ['крапива', 'борщевик', 'химический ожог']}
    for key, value in riddles_dict.items():
        func(key, value, ATTEMPTS)


if __name__ == '__main__':
    saved_riddles()