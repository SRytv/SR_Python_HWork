"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт,
автоматизирующий сохранение данных в файле YAML-формата. Для этого:
a. Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
b. Реализовать сохранение данных в файл формата YAML — например, в файл
file.yaml. При этом обеспечить стилизацию файла с помощью параметра
default_flow_style, а также установить возможность работы с юникодом:
allow_unicode = True;
c. Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml


def write_to_yaml_file(data_to_yanl, yaml_file_name, fl_unicode):
    with open(yaml_file_name, 'w', encoding='utf8') as yaml_file:
        yaml.dump(data_to_yaml, yaml_file, default_flow_style=False,
                  allow_unicode=fl_unicode)


def read_from_yaml_file(yaml_file_name):
    with open(yaml_file_name, 'r', encoding='utf8') as yaml_file:
        return yaml.load(yaml_file)


if __name__ == '__main__':
    data_to_yaml = {1: 'Sergey R.', 2: '20000€',
                    3: {1: '100€', 2: 50, 3: 1, }}
    write_to_yaml_file(data_to_yaml, 'file.yaml', True)
    data_from_file = read_from_yaml_file('file.yaml')
    print("В файл передано   : ", data_to_yaml)
    print("Из файла прочитано: ", data_from_file)
    print("Прочитанные данные совпадают с исходными: ", data_to_yaml ==
          data_from_file)
