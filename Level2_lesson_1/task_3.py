#3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

from sys import getdefaultencoding
str_1 = "attribute"
str_2 = "класс"
str_3 = "функцция"
str_4 = "type"
print("Defaultencoding = ", getdefaultencoding())
print(str_1.encode("ascii", errors='ignore'))
print(str_1.encode("ascii", errors='replace'))
print('='*80)

print(str_2.encode("ascii", errors='ignore'))
print(str_2.encode("ascii", errors='replace'))
print('='*80)

print(str_3.encode("ascii", errors='ignore'))
print(str_3.encode("ascii", errors='replace'))
print('='*80)

print(str_4.encode("ascii", errors='ignore'))
print(str_4.encode("ascii", errors='replace'))
print('='*80)
