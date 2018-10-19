#1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
#и проверить тип и содержание соответствующих переменных.
# Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
# и также проверить тип и содержимое переменных.

str_1 = "разработка"
print(str_1)
print(type(str_1))
print(str_1.encode('utf-8'))
print(type(str_1.encode('utf-8')))
print('='*80)

str_2 = "сокет"
print(str_2)
print(type(str_2))
print(str_2.encode('utf-8'))
print(type(str_2.encode('utf-8')))
print('='*80)

str_3 = "декоратор"
print(str_3)
print(type(str_3))
print(str_3.encode('utf-8'))
print(type(str_3.encode('utf-8')))
