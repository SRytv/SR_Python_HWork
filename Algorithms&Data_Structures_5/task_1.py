#1. Пользователь вводит данные о количестве предприятий, их наименования
## и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

import collections

fact_numb = int(input("Введите количество предприяний : "))
fact_income = collections.defaultdict(int)
for i in range(fact_numb):
    fact_name = input("введите название {: >2d}-го предприятия : ".format(i + 1))
    for j in range(1, 5):
        profit = int(input("Введите его прибыль за {: >2d}-й квартал : ".format(j)))
        fact_income[fact_name] += profit
    print('I', fact_income[fact_name])
    fact_income[fact_name] /= 4
all_fact_profit_sum = 0
for key in fact_income.keys():
    all_fact_profit_sum += fact_income[key]
all_fact_average_profit = all_fact_profit_sum / fact_numb

print("Средняя прибыль за год по всем предприятиям : ", all_fact_average_profit)

print("Список предприятий с среднегодовой прибылью выше средней:")
for key in fact_income.keys():
    if fact_income[key] > all_fact_average_profit:
        print(key, fact_income[key])

print("Список предприятий с среднегодовой прибылью ниже средней:")
for key in fact_income.keys():
    if fact_income[key] < all_fact_average_profit:
        print(key, fact_income[key])

