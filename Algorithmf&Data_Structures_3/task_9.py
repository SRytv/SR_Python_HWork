#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []
columns_numb = 6
rows_numb = 5
for i in range(0, rows_numb + 1):
    matrix.append([])
#print(matrix)
for j in range(0, rows_numb):
    for i in range(0, columns_numb):
        matrix[j].append(random.randint(1, 20))
    else:
        matrix[j].append(' ')  # Этот последняя строка будет использована для хранения минимальных значений столбцов
for i in range(0, columns_numb + 1):
    matrix[rows_numb].append(0)

for i in range(0, columns_numb):
    matrix[rows_numb][i] = matrix[0][i]
    for j in range(1, rows_numb):
        if matrix[j][i] < matrix[rows_numb][i]:
            matrix[rows_numb][i] = matrix[j][i]
matrix[rows_numb][columns_numb] = matrix[rows_numb][0]
for i in range(0, columns_numb):
    if matrix[rows_numb][i] > matrix[rows_numb][columns_numb]:
        matrix[rows_numb][columns_numb] = matrix[rows_numb][i]

print("\nПострочный вывод матрицы, последняя строка содержит минимальные значения соответствующих колонок")
print("Элемент в последней колонке последней строки, максимальное значение из этих минимумов")
for j in range(0, rows_numb):
    for i in range(0, columns_numb):
        print(' |{: >3d} '.format(matrix[j][i]), end='')
    print(' | {: >3s} |'.format(matrix[j][columns_numb]), end='')
    print('')
for i in range(0, columns_numb + 1):
    print(' |{: >3d} '.format(matrix[rows_numb][i]), end='')
print(' |\n')
