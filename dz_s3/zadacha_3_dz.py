# Создайте словарь со списком вещей для похода в качестве ключа и их массой
# в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъемность
# Достаточно вернуть один допустимый вариант
# * Верните все возможные варианты комплектации рюкзака


dict_items = {('вода', 'aptechka', 'eda', 'spichki', 'fonarik', 'palatka', 'nozh', 'paket', 'repellent', 'dozdevik', 'powerbank', 'noski'):
                  [2, 0.5, 1.5, 0.1, 0.5, 5, 0.3, 0.1, 0.3, 0.5, 0.4, 0.2]}

limit = 10
empty_bag = 0
items_in_bag = []
for i in dict_items:
    for j in dict_items[i]:
        if empty_bag < 10:
            empty_bag += j
            print(empty_bag)
print(empty_bag)