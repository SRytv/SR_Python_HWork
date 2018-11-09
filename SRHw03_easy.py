# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

#def my_round(number, ndigits):
 #   pass
#=====================================================
 def my_round(number, ndigits):
    numb1 = number * (10**ndigits)
    int_part = numb1//1
    rational_part = numb1 - int_part
    if (rational_part >= 0.5):
        int_part +=1
    result = int_part/(10**ndigits)
    return result


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#=====================================================

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
#
#=====================================================

def lucky_ticket(ticket_number):

    def sum_digits(digits_str):
        sum1 = 0
        for i in range(len(digits_str)):
            sum1 +=  int(digits_str[i])
        return sum1

    if len(ticket_number)%2:
        print ("Ошибка: чтобы проверить счастливый это номер билета или нет,он должен иметь четное количество цифр")
        return False
    numb_str = '%6s' % ticket_number
    return sum_digits(numb_str[0:4]) == sum_digits(numb_str[3:])

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))