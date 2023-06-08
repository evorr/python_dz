# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print


exceptions = [1700, 1800, 1900]
STEP_BTW_YEARS = 4
leap_year = False
year = int(input('Введите год: '))
if year not in exceptions:
    if year % STEP_BTW_YEARS == 0:
        leap_year = True
print("високосный" if leap_year else "невисокосный")