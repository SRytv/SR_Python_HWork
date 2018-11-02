#2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Первый - использовать алгоритм решето Эратосфена. Второй - без использования "решета".
# Проанализировать скорость и сложность алгоритмов.
# Примечание: Результаты анализа сохранить в виде комментариев в файле с кодом.
# Данный файл содержит решене без решета Эратосфена.
#
def find_prime(up_to):
    primes = [2, 3]
    nth_prime = 5
    for i in range(2, up_to):
        prime = True
        for curr_prime in primes:
            if i % curr_prime == 0:
                prime = False
        if prime:
            primes.append(i)
    if len(primes) >= nth_prime:
        print('{: >2d}е простое число = {: >2d}'.format(nth_prime, primes[nth_prime - 1]))
    else:
        print('В диапазоне от 2 до {: >2d} найдено менее {: >2d}-ти простых чисел'.format(int(up_to), int(nth_prime)))
    return primes


primes = find_prime(1000)
#
#============================================================================================================
#поиск среди 100 натуральных чисел
#
#C:\Users\Serg_\PycharmProjects\Algorithms&Data_Structures\Lesson_4>python -m cProfile -s time task_2b.py
#5е простое число = 11
#        34 function calls in 0.000 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 task_2b.py:1(find_prime)
#        1    0.000    0.000    0.000    0.000 {built-in method print}
#        2    0.000    0.000    0.000    0.000 {built-in method charmap_encode}
#        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#       23    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        2    0.000    0.000    0.000    0.000 cp866.py:18(encode)
#        1    0.000    0.000    0.000    0.000 task_2b.py:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method exec}
#        1    0.000    0.000    0.000    0.000 {built-in method len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#============================================================================================================
#поиск среди 10000 натуральных чисел
#
#C:\Users\Serg_\PycharmProjects\Algorithms&Data_Structures\Lesson_4>python -m cProfile -s time task_2b.py
# 5е простое число = 11
#         1238 function calls in 0.573 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.573    0.573    0.573    0.573 task_2b.py:1(find_prime)
#        1    0.000    0.000    0.000    0.000 {built-in method print}
#     1227    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        2    0.000    0.000    0.000    0.000 {built-in method charmap_encode}
#        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#        2    0.000    0.000    0.000    0.000 cp866.py:18(encode)
#        1    0.000    0.000    0.573    0.573 task_2b.py:1(<module>)
#        1    0.000    0.000    0.573    0.573 {built-in method exec}
#        1    0.000    0.000    0.000    0.000 {built-in method len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#============================================================================================================
#поиск среди 100 натуральных чисел
#
#C:\Users\Serg_\PycharmProjects\Algorithms&Data_Structures\Lesson_4>python -m cProfile -s time task_2b.py
#5е простое число = 11
#         177 function calls in 0.008 seconds
#
#   Ordered by: internal time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.008    0.008    0.008    0.008 task_2b.py:1(find_prime)
#        1    0.000    0.000    0.000    0.000 {built-in method print}
#      166    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#        2    0.000    0.000    0.000    0.000 {built-in method charmap_encode}
#        2    0.000    0.000    0.000    0.000 cp866.py:18(encode)
#        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#        1    0.000    0.000    0.008    0.008 task_2b.py:1(<module>)
#        1    0.000    0.000    0.008    0.008 {built-in method exec}
#        1    0.000    0.000    0.000    0.000 {built-in method len}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#============================================================================================================
#
# Можно предположить, что в данном случае имеется линейная зависимость т.е. O(n)