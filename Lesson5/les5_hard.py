# Задание-1: SRHw05_hard.py
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# 5_with_args.py
# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys
import re
import SRHw05_easy

def print_help():
    print("help - получение справки")
    print("-md <dir_name> - создание директории")
    print("-cp <file_name> - копировать, указанный файл")
    print("-rm <file_name> - удаление, указанного файла")
    print("-dd <dir_name> - удаление, указанной директории")
    print("-cd <dir_name> - перейти в указанную директорию")
    print("-ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")

dir_path = ' '
def is_abs_filename(file_or_dir):
    # возвращает 1 если это абсолютная директория, и 0 если относительная
    pattern = re.compile(r'[A-Z]:\)', re.IGNORECASE)
    return pattern.match(file_or_dir) != None

def make_dir():
    if not file_dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if is_abs_filename(file_dir_name):
        dir_path = file_dir_name
    else:
        dir_path = os.path.join(os.getcwd(), file_dir_name)
    result = SRHw05_easy.make_dir(dir_path)
    if result:
        print (result)
        print ('создать директорию {} не удалось'.format(file_dir_name))
        if result == 2:
            print('директория с именем {} уже существует'.format(file_dir_name))
    if result == 0:
        print('директория {} успешно создана'.format(file_dir_name))

def show_dir():
    dir_path = os.getcwd()
    print ("текущая директория: ", dir_path)
    print ("Содержимое директории:")
    for elem in SRHw05_easy.list_dir(dir_path)[0]:
        print(elem)
    print ("Элементы сами являющиеся директориями: ")
    for elem in SRHw05_easy.list_dir(dir_path)[1]:
        print(elem)

def del_dir():
    if not file_dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if is_abs_filename(file_dir_name):
        dir_path = file_dir_name
    else:
        dir_path = os.path.join(os.getcwd(), file_dir_name)
    if not os.path.exists(dir_path):
        print ('директория {} не существует, удалять нечего!'.format(file_dir_name))
    else:
        print("Вы действительно хотите удалить директорию '{}'".format(file_dir_name))
        answer = input("Ведите 'Y', если 'да' или 'N', если нет:")
        if answer =='N' or answer == 'N':
            print ("удаление отменено!")
            return
        elif answer !='Y' and answer != 'y':
            print ("некорректный ответ, удаление не будет выполнено!")
            return
        SRHw05_easy.delete_dir(dir_path)
        if not os.path.exists(dir_path):
            print ('директория {} успешно удалена'.format(file_dir_name))

def change_dir():
    if not file_dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    if is_abs_filename(file_dir_name):
        dir_path = file_dir_name
    else:
        dir_path = os.path.join(os.getcwd(), file_dir_name)
    result = SRHw05_easy.change_dir(dir_path)
    if result:
        print ('перейти в директорию {} не удалось'.format(file_dir_name))
        if result == 2:
            print('директория с именем {} уже существует'.format(file_dir_name))
    if result == 0:
        print('переход в директорию {} успешно совершен'.format(file_dir_name))

def copy_dir():
    if not file_dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if is_abs_filename(file_dir_name):
        dir_path = file_dir_name
    else:
        dir_path = os.path.join(os.getcwd(), file_dir_name)
    print("файл будет сохранен с именем", dir_path+'.bak')
    if os.path.exists(dir_path+'.bak'):
        print('файл с именем {} уже существует'.format(file_dir_name)+'.bak')
        print("В случае продолжения копирования его первоначальное содержимое будет удалено!")
        answer = input("Ведите 'Y', если ВЫ хотите продолжить копирование или 'N', если нет:")
        if answer =='N' or answer == 'N':
            print ("Копирование отменено!")
            return
        elif answer !='Y' and answer != 'y':
            print ("некорректный ответ, копирование не будет выполнено!")
            return
#собственно копирование файла ее не реализовано!

def remove_file():
    if not file_dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if is_abs_filename(file_dir_name):
        dir_path = file_dir_name
    else:
        dir_path = os.path.join(os.getcwd(), file_dir_name)
    if os.path.isfile(file_dir_name):
        print("Вы действительно хотите удалить файл {}".format(file_dir_name))
        answer = input("Ведите 'Y', если 'да' или 'N', если нет:")
        if answer =='N' or answer == 'N':
            print ("удаление отменено!")
            return
        elif answer !='Y' and answer != 'y':
            print ("некорректный ответ, удаление не будет выполнено!")
            return
    os.remove(file_dir_name)
    if not os.path.isfile(file_dir_name):
        print ('файл {} успешно удален'.format(file_dir_name))


def ping():
    print("pong")

do = {
    "-h": print_help,
    "help": print_help,
    "-md": make_dir,
    "-cd": change_dir,
    "-cp": copy_dir,
    "-rm": remove_file,
    "-dd": del_dir,
    "-ls": show_dir,
    "-ping": ping
}

try:
    file_dir_name = sys.argv[2]
except IndexError:
    file_dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help или -h  для получения справки")
