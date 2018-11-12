import random
import sys

cask_MAX_NUMBER = 90
curr_cask = 0
card_lines = [[],[],[]]
#==========================================================================

def prepare_card():
    for i in range(0,3):
        for j in range(0,9):
            card_lines[i].append(' ')
    all_allowed_numbers = [x for x in range(1,cask_MAX_NUMBER+1)]
    random.shuffle( all_allowed_numbers )

    for j in range(0,3):
        line = all_allowed_numbers[j*10: j*10+5]
        del all_allowed_numbers[j*10: j*10+5]
        line = sorted(line)
        random.seed()
        for x in range (0,5):
            numb_ins = False
            while not numb_ins:
                k = random.randint(0,8)
                if card_lines[j][k] == ' ':
                    card_lines[j][k] = line[x]
                    numb_ins = True
                else:
                    numb_ins = False #выбраная ячейка уже занята, попробавать еще раз

#==========================================================================
 #    def _str__(self):
def print_card():
    card_owners_name = "игрок"
    header = '{:-^37}\n'.format(card_owners_name)

    full_card = ''
    for i in range(0,3):
        main_part = '|'
        for j in range(0,9):
            if card_lines[i][j] == ' ':
                main_part += '   |'
            else:
                main_part +=  ('{: >3}'.format(card_lines[i][j]) +'|')
        main_part +='\n'
        full_card += main_part
    pass
    full_card = header + full_card + '='*37
    print('\n')
    print (full_card)


def casks_bag():
    random.seed()
    #return curr_cask = random.randint(1,cask_MAX_NUMBER)
    #получить заведомо сущнствующий номер на карте, для проверки
    for i in range(0,2):
        for j in range(0,9):
            if card_lines[i][j] != ' ':
                curr_cask = card_lines[i][j]
                break
    #casks_bag()
    print("извечен боченокс номером: ", curr_cask)
    return curr_cask


def check_number_in_card():
    for i in range(0,2):
        if curr_cask in card_lines[i]:
            cask_found = True
            cask_index1 = i
            cask_index2 = card_lines[i].index(curr_cask)
        else:
            cask_found = False
            cask_index1 = 0
            cask_index2 = 0
    return cask_found, cask_index1, cask_index2

def erase_number(*check_result):
        if check_result[0]:
            card_lines[check_result[1]][check_result[2]] = ' '

#================================================================================

if __name__ == '__main__':
    game_On = True
    prepare_card()
    while game_On:
        print_card()

        curr_cask = casks_bag()
        print (curr_cask)

        answer_again = True
        print("На Вашей карточке есть такой номер, и Вы хотите его зачеркнуть?")
        print("Если Вы ошибетесь и решите зачеркнуть несуществующий у Вас номер,")
        print("то Вы проиграете!")
        while answer_again:
            answer = input("И так Ваше решение? Зачеркнуть номер? 'Да' или 'Нет' Y/N :")
            if (answer.lower() != 'y' and answer.lower() != 'n'):
                print("Введен некорректный символ : '", answer, "'")
                print("Повторите ввод!")
            else:
                answer_again = False
            answer = answer.lower()

        check_result = check_number_in_card()
        if check_result[0]:
            print("Номер найден на карте!", "строка= ", check_result[1]+1, "позиция =", check_result[2]+1)
        else:
            print("Номер на карте не найден!")



        if answer =='y':
            if check_result[0]:
                erase_number(*check_result)
                print_card()
            else:
                print("Такого номера на карте нет; Вы проиграли!")
                game_On = False

        answer = input("Вы хотите продолжать? 'Да' или 'Нет' Y/N :")
        if (answer.lower() != 'y' and answer.lower() != 'n'):
            print("Введен некорректный символ : '", answer, "'")
            print("Повторите ввод!")
        else:
            answer_again = False
        answer = answer.lower()
        if answer == 'n':
            print("Игра закончена!")
            break