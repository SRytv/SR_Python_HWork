#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com
# и преобразовать результаты из байтовового в строковый тип на кириллице.

ping_file = open(r'ping.txt', 'r')
for line in ping_file:
    print(line.encode('utf-8', errors='replace').decode('cp866'))
    #ни одна из использованных кодовых таблиц:
    # koi8_r, cp866, windows-1251, cp819,
    #не дали положительного результата. Кириллица MS-DOS в списке отсутствует
    #
    #print(line.decode('cp866').encode('utf-8'))
    # показанная Вами на уроке на экране монитора приведенная выше строка
    # неизменно выдавала онибку: 'str' object has no attribute 'decode'
