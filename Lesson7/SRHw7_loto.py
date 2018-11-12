#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html

"""
import random
import sys

cask_MAX_NUMBER = 90

class Card():
    def __init__(self, name):
        self.card_owners_name = name
        self.card_lines = [[],[],[]]
        for i in range(0,3):
            for j in range(0,9):
                self.card_lines[i].append(' ')
        self.all_allowed_numbers = [x for x in range(1,cask_MAX_NUMBER+1)]
        random.shuffle( self.all_allowed_numbers )

        for j in range(0,3):
            self.line = self.all_allowed_numbers[j*10: j*10+5]
            del self.all_allowed_numbers[j*10: j*10+5]
            self.line = sorted(self.line)
            random.seed()
            for x in range (0,5):
                numb_ins = False
                while not numb_ins:
                    k = random.randint(0,8)
                    if self.card_lines[j][k] == ' ':
                        self.card_lines[j][k] = self.line[x]
                        numb_ins = True
                    else:
                        numb_ins = False #выбраная ячейка уже занята, попробавать еще раз
                pass
            pass

    def _str__(self):
        self.header = '{:-^37}\n'.format(self.card_owners_name)
        self.full_card = ''
        for i in range(0,3):
            main_part = '|'
            for j in range(0,9):
                if self.card_lines[i][j] == ' ':
                    main_part += '   |'
                else:
                    main_part +=  ('{: >3}'.format(self.card_lines[i][j]) +'|')
            main_part +='\n'
            self.full_card += main_part
        self.full_card = self.header + self.full_card + '='*37
        return ('\n' + self.full_card)

    def check_number_in_card(self, cask_to_check):
        for i in range(0,2):
            if cask_to_check in self.card_lines[i]:
                cask_found = True
                cask_index1 = i
                cask_index2 = self.card_lines[i].index(cask_to_check)
            else:
                cask_found = False
                cask_index1 = 0
                cask_index2 = 0
        return cask_found, cask_index1, cask_index2



if __name__ == '__main__':
    card1 = Card("игрок")
    card2 = Card("компьютер")
    print (card1)
    print(card2)
