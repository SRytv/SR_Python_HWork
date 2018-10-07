# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

random_list = []
List_LENGTH = 20
for i in range(0, List_LENGTH + 1):
    random_list.append(random.randint(-10, 20))

print(random_list)
max_negative = {}
for i in range(0, List_LENGTH):
    if random_list[i]< 0:
        max_negative["value"] = random_list[i]
        max_negative["index"] = i

if max_negative["index"] != List_LENGTH:
    for i in range(max_negative["index"], List_LENGTH):
        if random_list[i]<0:
            if random_list[i] > max_negative["value"]:
                max_negative["value"] = random_list[i]
                max_negative["index"] = i

print(random_list)
print("Максимальным отрицательным элементом массива является {: >-2d} ".format(max_negative["value"]))
print("Его индекс:  {: >-2d} ".format(max_negative["index"]))