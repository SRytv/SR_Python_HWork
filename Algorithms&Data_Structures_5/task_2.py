#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
#
#Например, пользователь ввёл A2 и C4F.
#Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
#Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
#Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

DEBUGGING_RUN = False
import collections
import copy

hex_values = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, }


def value_to_hex(value):
    keys = hex_values.keys()
    values = hex_values.values()
    for key in keys:
        if hex_values[key] == value:
            break
    return key

#==================================================================================================================
if not DEBUGGING_RUN:
    print("Введите 1-е шестнадцатеричное число", end=' ')
    hex_1_input = input("в виде строки символов[0-9]|[a-f], например: ab12345: ")
    print("Введите 1-е шестнадцатеричное число", end=' ')
    hex_2_input = input("в виде строки символов[0-9]|[a-f], например: ab12345: ")
    operation = input("Введите символ операции +|* : ")
else:
    operation = '+'

    hex_1_input = 'c4f'
    hex_2_input = 'a2'

#==================================================================================================================

hex_1 = collections.deque(list((hex_1_input).lower()))
hex_2 = collections.deque(list((hex_2_input).lower()))

#==================================================================================================================
def mult_hex(hex_1, hex_2):
    hex_1c = copy.copy(hex_1)
    hex_tmpresult = collections.deque([])
    hex_result = collections.deque([])
    hex_l_len = len(hex_1)
    hex_2_len = len(hex_2)
    for i in range(hex_l_len):# подготовка массивов для хранения промежуточных произведний
        hex_tmpresult.append(collections.deque([]))
        hex_result.append('0')

    for i in range(hex_l_len):
        hex_dig_1 = hex_1c.pop()
        carry = 0
        hex_2c = copy.copy(hex_2)

        for j in range(hex_2_len):
            hex_dig_2 = hex_2c.pop()
            res_dig = hex_values[hex_dig_1] * hex_values[hex_dig_2] + carry
            if int(res_dig / 16) >= 1:
                carry = int(res_dig / 16)
                res_dig = res_dig % 16
            else:
                carry = 0
            hex_tmpresult[i].appendleft(value_to_hex(res_dig))
        if carry != 0:
            hex_tmpresult[i].appendleft(value_to_hex(carry))
        if i > 0:  # компенсация того факта, что частичные умножения выполнялись без учета разряда множителей
            for k in range(i):
                hex_tmpresult[i].append('0')
    for i in range(hex_l_len):
        hex_result = sum_hex(hex_result, hex_tmpresult[i])
        #удалить незначащуе нули из старших разрядов
        while hex_result[0] == '0':
            hex_result.popleft()
    return hex_result


#==================================================================================================================

def sum_hex(hex_1, hex_2):
    hex_1c = copy.copy(hex_1)
    hex_2c = copy.copy(hex_2)

    #выравниваем числа по младшему (правому) разряду
    if len(hex_1c) > len(hex_2c):
        len_diff = len(hex_1c) - len(hex_2c)
        for i in range(len_diff):
            hex_2c.appendleft('0')
    else:
        len_diff = len(hex_2c) - len(hex_1c)
        for i in range(len_diff):
            hex_1c.appendleft('0')
    #доплнительные нули  для  обработки переноса за старший разряд
    hex_1c.appendleft('0')
    hex_2c.appendleft('0')

    hex_result = collections.deque([])
    hex_len = len(hex_1c)
    carry = 0
    for i in range(hex_len):
        hex_dig_1 = hex_1c.pop()
        hex_dig_2 = hex_2c.pop()
        res_dig = hex_values[hex_dig_1] + hex_values[hex_dig_2] + carry
        if res_dig >= 16:
            res_dig -= 16
            carry = 1
        else:
            carry = 0
        hex_result.appendleft(value_to_hex(res_dig))
    return hex_result


do = {
    "+": sum_hex,
    "*": mult_hex,
}

result = do[operation](hex_1, hex_2)
print("Врезультате выполнения операции:")
print('\n', ''.join(list(hex_1)), operation, ''.join(list(hex_2)), ' = ', ''.join(list(result)))



