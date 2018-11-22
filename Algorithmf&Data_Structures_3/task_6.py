#6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

#=======================================================================================================
# далее блок из задачи task_3.py

print("\nВведите как можно более длинный ряд челых случайных чисел, для завершения ввода введите символ 'S'")
print("Если вообще не хотите вводить числа, введите 'S' вместо первого числа")
print("тогда список будет создан автоматически. И так начинаем:")
answer = input("Введите первое число или 'S': ")
random_list = []
random_list_LENGTH = 20
if answer.lower() == 's':
    for i in range(0, random_list_LENGTH + 1):
        random_list.append(random.randint(1, random_list_LENGTH))
else:
    while answer.lower() != 's':
        random_list.append(int(answer))
        answer = input("Введите следующее число или 'S': ")
curr_max = {}
curr_max['index'] = 0
curr_max['value'] = random_list[0]
curr_min = {}
curr_min['index'] = 0
curr_min['value'] = random_list[0]

for i in range(0, len(random_list)):
    if random_list[i] > curr_max['value']:
        curr_max['value'] = random_list[i]
        curr_max['index'] = i
        continue  # текущий элнмент уже заведоио не может оказаться минимальным
    else:
        if random_list[i] < curr_min['value']:
            curr_min['value'] = random_list[i]
            curr_min['index'] = i
print(random_list)
print('\nМаксимальный элемент: {: >2d} в позиции {: >2d}:'.format(curr_max['value'], curr_max['index']))
print('Минимальный элемент: {: >2d} в позиции {: >2d}:'.format(curr_min['value'], curr_min['index']))

# выше блок из задачи task_3.py
#=======================================================================================================
sum_elem = 0
if curr_max['index'] != curr_min['index']:
    if curr_max['index'] > curr_min['index']:
        for i in range(curr_min['index'] + 1, curr_max['index']):
            sum_elem += random_list[i]
    else:
        for i in range(curr_max['index'] + 1, curr_min['index']):
            sum_elem += random_list[i]

print('Сумма элементов между максимальным и минимальным значениями, составляет:{: >3d}'.format(sum_elem))
