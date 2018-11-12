# 1. Отсортировать по убыванию методом «пузырька» одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Вывести на экран исходный и отсортированный массивы.

import random

array_SIZE = 10
#==============================================================================

def buble_sort(array):
    n = 1
    last_i = 1
    while n < len(array):
        no_swaps = True
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                no_swaps = False
        if no_swaps:
            break  # обменов не было массив отсортирован, продолжать нет смысла
        n += 1

#==============================================================================

if __name__ == "__main__":
    array = []
    for i in range(array_SIZE):
        array.append(random.randint(-100, 99))
    print("Исходный  массив:      ", end=' ')
    print(array)
    buble_sort(array)
    print("Ссортированный массив:", end=' ')
    print(array)


