#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.


import random

random_list = []
random_list_LENGTH = 20
for i in range(0, random_list_LENGTH + 1):
    random_list.append(random.randint(1, 20))

curr_min_1 = {}
curr_min_1['index'] = 0
curr_min_1['value'] = random_list[0]

for i in range(0, random_list_LENGTH + 1):
    if random_list[i] < curr_min_1['value']:
        curr_min_1['value'] = random_list[i]
        curr_min_1['index'] = i

curr_min_2 = {}
curr_min_2['index'] = 0
curr_min_2['value'] = random_list[0]

for i in range(curr_min_1['index'] + 1, random_list_LENGTH + 1):
    if random_list[i] < curr_min_2['value']:
        curr_min_2['value'] = random_list[i]
        curr_min_2['index'] = i
print(random_list)
print('\n1й минимальный  элемент: {: >2d} в позиции {: >2d}:'.format(curr_min_1['value'], curr_min_1['index']))
print('2й минимальный элемент: {: >2d} в позиции {: >2d}:'.format(curr_min_2['value'], curr_min_2['index']))
