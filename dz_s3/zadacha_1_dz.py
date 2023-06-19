# Дан список повторяющихся элементов. Вернуть список с дублтрующимися элементами.
# В результирующем списке не должно быть дубликатов

old_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 8, 8]
new_list = []

for item in set(old_list):
    if old_list.count(item) > 1:
        new_list.append(item)


print(new_list)