# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки)
# и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.
__all__ = ['saved_riddles', 'func', 'print_result']
ATTEMPTS = 3
_RESULT_OF_RIDDLES = {}


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
        result = func(key, value, ATTEMPTS)
        result_dict_make(key, result)


def result_dict_make(riddle, attempt):
    _RESULT_OF_RIDDLES[riddle] = attempt


def print_result():
    for key, value in _RESULT_OF_RIDDLES.items():
        print(f'{key} {"Не отгано" if value == 0 else "Отгадано с " + str(value) + " попытки"} ')


if __name__ == '__main__':
    saved_riddles()
    print_result()