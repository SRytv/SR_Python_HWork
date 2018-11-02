#2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 0, 3, 4, 5
# (индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
import random

list_1 = []
List_1_LENGTH = 20
for i in range(0, List_1_LENGTH + 1):
    list_1.append(random.randint(1, 20))

print("\nПервый массив: ", list_1)
#even_numbers_indixes = [i for i in range(0, len(list_1)) if list_1[i] % 2 == 0]
#print("Массив индексов четных чисел первого массива: ", even_numbers_indixes)
even_numbers_indixes = [i for i in range(0, List_1_LENGTH) if list_1[i] % 2 == 0]
print("Массив индексов четных чисел первого массива: ", even_numbers_indixes)

