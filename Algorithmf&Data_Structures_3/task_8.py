#8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
#  Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
#  в ее последнюю ячейку. В конце следует вывести полученную матрицу.

import random

print("\nВведите матрицу 5х4 из целых чисел, т.е. 4 раза по 5 чисел. ")
print("В конце ввода каждой строки из 5 чисел будет автоматически добавляться '0'. Не обращайте внмания!")
print("Если вообще не хотите вводить числа, введите 'S' вместо первого числа")
print("тогда матрица будет создана автоматически. И так начинаем:")
answer = input("Введите первое число или 'S': ")

matrix = [[], [], [], []]
columns_numb = 5
rows_numb = 4
if answer.lower() == 's':
    for j in range(0, rows_numb):
        for i in range(0, columns_numb):
            matrix[j].append(random.randint(1,20))
        else:
            matrix[j].append(0)
else:
    for j in range(0, rows_numb):
        for i in range(0, columns_numb):
            matrix[j].append(int(answer))
            answer = input("Введите следующее число: ")
        else:
            matrix[j].append(0)

for j in range(0, rows_numb):
    for i in range(0, columns_numb):
        matrix[j][columns_numb] += matrix[j][i]

print("\nВывод матрицы 5х4, последний 6й элемент каждой строки")
print(" - сумма всех элеменов данной строки матрицы:\n")
for j in range(0, rows_numb):
    for i in range(0, columns_numb):
        print(' |{: >3d} '.format(matrix[j][i]), end = '')
    print (' | {: >3d} |'.format(matrix[j][columns_numb]), end = '')
    print ('')

