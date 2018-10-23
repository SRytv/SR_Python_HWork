# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# Конечно, хорошо бы воспользовать регулятные выражения, но я пока, увы, слаб...
$и до упрощения тоже не добрался
"""
print("введите строку выражения с простыми дробями: дробь +(или)- дробь")
expression = input("дроби в формате n x/y ,где n - целая часть(не обязательная), x - числитель, у - знаменатель: ")
"""
expression = '2 5/6 + 3 4/7'

def analyse_fraction(fraction_str):
    whole = 0 # предполагаем, сто целой части нет
    if (' ' in fraction_str):
        #дробь имеет целую часть
        whole =int(fraction_str.split(' ')[0])
        rational_part = fraction_str.split(' ')[1]
    else:
        rational_part = fraction_str
    if ('/' in rational_part):
        fr1 = rational_part.split('/')
        divident = int(fr1[0])
        divisor = int(fr1[1])
    else:
        whole = int(rational_part)
        divident = 1
        divisor = 1
    return (whole, divident, divisor)

splitted_expression = expression.split(' ')
if not ('/' in splitted_expression[0]):
    #splitted_expression[0] - это целая часть дроби
    fraction1 = splitted_expression[0]+' '+ splitted_expression[1]
    sign_of_operation = splitted_expression[2]
else:
    fraction1 = splitted_expression[0]
    sign_of_operation = splitted_expression[1]
if (not('/' in splitted_expression[-2])) and (splitted_expression[-2]!='+'and (splitted_expression[-2]!= '-')):
    #splitted_expression[-2] - это возможно целая часть  второй дроби
    fraction2 = splitted_expression[-2] +' '+ splitted_expression[-1]
else:
    fraction2 = splitted_expression[-1]
fraction1_parts = analyse_fraction(fraction1)
#print(fraction1_parts)
fraction2_parts = analyse_fraction(fraction2)
#print(fraction2_parts)
if (sign_of_operation == '+') or (sign_of_operation == '-'):
    operand1 = (fraction1_parts[1]*fraction2_parts[2])
    operand2 = (fraction2_parts[1]*fraction1_parts[2])
    if (sign_of_operation == '+'):
        work_result_divident = operand1 + operand2
    else:
        work_result_divident = operand1 - operand2
    result_divisor = fraction2_parts[2]*fraction1_parts[2]
    whole_result = fraction1_parts[0] + fraction2_parts[0] + (work_result_divident//result_divisor)
    result_divident = (work_result_divident % result_divisor)
    print (expression, " = ", whole_result, result_divident,"/", result_divisor)

#===================================================

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))

#===================================================

fruits=[]
for line in open(r'.\data\fruits.txt', 'r'):
    fruits.append(line)
    fruits.sort()
files_names = {}
for fruit in (fruits):
    files_names[fruit[0]] = [('open_'+fruit[0]), False, fruit[0]]
for fruit in (fruits):
    if not files_names[fruit[0]][1]:
        #Значение False, т.е. файл для буквы "А" еще не открыт, открыть!
        files_names[fruit[0]][0] = open(r'.\data\file_'+files_names[fruit[0]][2]+'.txt', 'w')
        files_names[fruit[0]][1] = True
        files_names[fruit[0]][0].write(fruit)
    else:
        files_names[fruit[0]][0].write(fruit)

for key in files_names:
    files_names[key][0].flush()
    files_names[key][0].close()