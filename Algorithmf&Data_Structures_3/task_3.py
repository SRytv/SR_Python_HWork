#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

random_list = []
random_list_LENGTH = 20
for i in range(0, random_list_LENGTH + 1):
    random_list.append(random.randint(1, 20))

curr_max = {}
curr_max['index'] = 0
curr_max['value'] = random_list[0]
curr_min = {}
curr_min['index'] = 0
curr_min['value'] = random_list[0]

for i in range(0, random_list_LENGTH):
    if random_list[i] > curr_max['value']:
        curr_max['value'] = random_list[i]
        curr_max['index'] = i
        continue  # текущий элнмент уже заведоио не может оказаться минимальным
    else:
        if random_list[i] < curr_min['value']:
            curr_min['value'] = random_list[i]
            curr_min['index'] = i
print('\nМаксимальный элемент: {: >2d} в позиции {: >2d}:'.format(curr_max['value'], curr_max['index']))
print('Минимальный элемент: {: >2d} в позиции {: >2d}:'.format(curr_min['value'], curr_min['index']))
changed_list = random_list[:]
changed_list[curr_max['index']] = curr_min['value']
changed_list[curr_min['index']] = curr_max['value']
print("\nИсходный массив  :", random_list)
print("измененный массив:", changed_list)