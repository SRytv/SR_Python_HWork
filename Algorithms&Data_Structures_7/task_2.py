# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random

array_SIZE = 10

#  это не мой код,  он взят с указанного далее сайта, сам я ничего прдумать не
#  смог. Долго пытался понять, как он работает и почему не работает у меня.
#  Причина неработоспособности было элементарна, но гоаорить о ней не хочется,
#  Зато в коде разобрался. Было еще много других, но этот мне понравился больше
#===========http://www.cyberforum.ru/python/thread395180.html=====================
#=================================================================================

def merge(left, right):
    lst = []
    while left and right:
        if left[0] < right[0]:
            # в данном случае сортировка по возрастанию, для сортировки по убыванию
            # нужно поменять знак равенства на обратный
            lst.append(left.pop(0))
        else:
            lst.append(right.pop(0))
    if left:
        lst.extend(left)
    if right:
        lst.extend(right)
    return lst

#==============================================================================

def merge_sort(lst):
    length = len(lst)
    if length >= 2:
        mid = int(length / 2)
        lst = merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))
    return lst

#==============================================================================

if __name__ == "__main__":
    array = []
    for i in range(array_SIZE):
        array.append(random.uniform(0, 50 - 1e-100))
    print("Исходный  массив:      ", end=' ')
    for number in array:
        print('{: >7.4f}'.format(number), end=' ')
    array = merge_sort(array)
    print("\nОтсортированный массив:", end=' ')
    for number in array:
        print('{: >7.4f}'.format(number), end=' ')
