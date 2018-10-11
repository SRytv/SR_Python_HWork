#1. В диапазоне натуральных чисел от 2 до 99 определить,
#  сколько из них кратны любому из чисел в диапазоне от 2 до 9.
#
multiplicity_count = [0, 0, ]  #список для хранения количеств кратностей
SEQ_LOWERBOUND = 2
SEQ_UPPERBOUND = 99
DEVIDERS_LOWERBOUND = 2
DEVIDERS_UPPERBOUND = 9
for i in range(DEVIDERS_LOWERBOUND, DEVIDERS_UPPERBOUND + 1):
    multiplicity_count.append(0, )
for k in range(SEQ_LOWERBOUND, SEQ_UPPERBOUND + 1):
    for j in range(DEVIDERS_LOWERBOUND, DEVIDERS_UPPERBOUND + 1):
        if k % j == 0:
            multiplicity_count[j] += 1
print('\nВ диапазоне натуральных чисел от {: >2d} до {: >2d}:'.format(SEQ_LOWERBOUND, SEQ_UPPERBOUND))
for i in range(DEVIDERS_LOWERBOUND, DEVIDERS_UPPERBOUND + 1):
    print('чисел кратных {: >2d}: {: >2d}'.format(i, multiplicity_count[i]))

#Здесь я в сомнении не нужно ли всюду отнять по '1', ведь числа-цифры [2-9] кратны сами себе?
#Как-то это вроде не слишком "математично", хотя и под условие данной задачи они подпадают?
