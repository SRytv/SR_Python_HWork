#4. Определить, какое число в массиве встречается чаще всего.

import random

count_list = []
numbers_list = []
List_LENGTH = 55
DIFF_NUMBS = 30
for i in range(0, List_LENGTH + 1):
    numbers_list.append(random.randint(1, DIFF_NUMBS))

for i in range(0, DIFF_NUMBS+1):
    count_list.append(0)

for i in range(0, List_LENGTH + 1):
    count_list[numbers_list[i]] += 1

print("исходный массив чисел:")
if List_LENGTH >30: #Если массив очень большой выводим его строками по 10 элементов в строке
    for j in range(0, int(List_LENGTH/10)):
        line_to_print = numbers_list[j*10:(j*10)+10]
        print (line_to_print)
else:
    print ('\n', numbers_list)

for i in range(0, DIFF_NUMBS):
    print("В данном массиые число: {: >3d} встречается {: >d} раз".format(i, count_list[i]))
