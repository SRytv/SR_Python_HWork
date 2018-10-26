#2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.
# Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.

def erathosthen(up_to):
    primes = [i for i in range(2, up_to + 1)]

    for curr_prim in primes:
        if curr_prim != 0:
            for j in range(curr_prim + curr_prim, up_to + 1, curr_prim):
                primes[j - 2] = 0
    return primes


nth_prime = 5
primes = erathosthen(100)
#print(primes)
primes_counter = 0
#print([i for i in primes if i != 0])
for i in range(len(primes)):
    if primes[i]:
        primes_counter += 1
        if primes_counter == nth_prime:
            break
#print('{: >2d}е простое число = {: >2d}'.format(nth_prime, primes[i]))

#Все оценки проводились при отключенном выводе на экран!!
#C:\Users\Serg_\PycharmProjects\Algorithms&Data_Structures\Lesson_4>python -m cProfile -s time task_2.py 25
#         6 function calls in 0.000 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 task_2.py:6(erathosthen)
#        1    0.000    0.000    0.000    0.000 task_2.py:6(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method exec}
#        1    0.000    0.000    0.000    0.000 task_2.py:8(<listcomp>)
#        1    0.000    0.000    0.000    0.000 {built-in method len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#

# Не представляю, что можно здесь проанализирова!? Видимо слишком простая функция. Даже увеличение
#Даже увеличение параметра у функции erathosthen( до 1000 не влияет на результат!Разве что до 10000
#
#C:\Users\Serg_\PycharmProjects\Algorithms&Data_Structures\Lesson_4>python -m cProfile -s time task_2.py 10000
#         6 function calls in 0.003 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.003    0.003    0.003    0.003 task_2.py:6(erathosthen)
#        1    0.000    0.000    0.000    0.000 task_2.py:8(<listcomp>)
#        1    0.000    0.000    0.003    0.003 task_2.py:6(<module>)
#        1    0.000    0.000    0.003    0.003 {built-in method exec}
#        1    0.000    0.000    0.000    0.000 {built-in method len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
# Вообще же все это очень похоже на попытку померить толщину лески метровой линейкой...
# С другой стороны проход по массиву цикл в цикле должен бы дать сложность, теоретически порядка O(x**2)
