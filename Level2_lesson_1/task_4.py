#4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

str_1 = "разработка"
print(str_1)
print(type(str_1))
str_1b = str_1.encode('utf-8')
print("encoded = ", str_1b)
print(type(str_1b))
str_1d = str_1b.decode('utf-8')
print("decoded = ", str_1d)
print(type(str_1d))
print("str_1 == str_1d :", str_1 == str_1d)
print('='*80)

str_2 = "администрирование"
print(str_2)
print(type(str_2))
str_2b = str_2.encode('utf-8')
print("encoded = ", str_2b)
print(type(str_2b))
str_2d = str_2b.decode('utf-8')
print("decoded = ", str_2d)
print(type(str_2d))
print("str_2 == str_2d :", str_2 == str_2d)
print('='*80)

str_3 = "protocol"
print(str_3)
print(type(str_3))
str_3b = str_3.encode('utf-8')
print("encoded = ", str_3b)
print(type(str_3b))
str_3d = str_3b.decode('utf-8')
print("decoded = ", str_3d)
print(type(str_3d))
print("str_3 == str_3d :", str_3 == str_3d)
print('='*80)

str_4 = "standard"
print(str_4)
print(type(str_4))
str_4b = str_4.encode('utf-8')
print("encoded = ", str_4b)
print(type(str_4b))
str_4d = str_4b.decode('utf-8')
print("decoded = ", str_4d)
print(type(str_4d))
print("str_4 == str_4d :", str_4 == str_4d)
print('='*80)
