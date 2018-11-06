"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:
a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);
b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data(), а также
сохранение подготовленных данных в соответствующий CSV-файл;
c. Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import re
import copy


def get_data():
    # имена подсписков в списке 'result_lists'
    os_prod_list = 0
    os_name_list = 1
    os_code_list = 2
    os_type_list = 3

    result_lists = [[], [], [], []] # списки для хранения промежуточных результатов чтения
    main_data = [[], [], [], []] # списки формирования окончательных результатов

    csv_header = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']

    pattern = re.compile(r'^(\w[^:]+)+:\s+([^:\n]+)\s*$')
    #pattern = re.compile(r'^(\w[^:]+).*:\s+([^:\n]+)\s*$')

    for file in ['info_1.txt', 'info_2.txt', 'info_3.txt']:
        with open(file, 'r') as curr_file:
            for curr_line in curr_file:
                if pattern.match(curr_line) != None:
                    patterns = pattern.findall(curr_line)
                    for i in range(len(csv_header)):
                        if patterns[0][0] == csv_header[i]:
                            result_lists[i].append(patterns[0][1])
                            break
    #====================================================================================

    zipped_elems = zip(result_lists[0], result_lists[1], result_lists[2], result_lists[3])
    main_data[0] = copy.copy(list(csv_header))
    i = 1
    for elem in zipped_elems:
        main_data[i] = copy.copy(list(elem))
        i += 1
    return main_data


def write_to_csv(data_to_csv, filename):
    with open(filename, 'w', encoding='utf8') as csv_out_file:
        csv_file_writer = csv.writer(csv_out_file, delimiter=',')
        csv_file_writer.writerow(data_to_csv[0])
        for i in range(len(data_to_csv)):
            csv_file_writer.writerow(data_to_csv[i])
    return None


if __name__ == "__main__":
    write_to_csv(get_data(), 'main_data.csv')
