# Дан список повторяющихся элементов. Вернуть список с дублтрующимися элементами.
# В результирующем списке не должно быть дубликатов

old_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 8, 8]
new_list = []

for item in old_list:
    if old_list.count(item) > 1 and item not in new_list:
        new_list.append(item)


print(new_list)