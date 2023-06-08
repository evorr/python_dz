# Нарисовать в консоли елку спросив у пользователя количество рядов
# Пример результата:
# Сколько рядов у елки? 5


quantity_lane = int(input('Сколько рядов у елки? '))

spruce_lane = ''
for i in range(1, quantity_lane + 1):
    spruce_lane = (quantity_lane - i) * ' ' + (i * '* ')
    print(spruce_lane)


