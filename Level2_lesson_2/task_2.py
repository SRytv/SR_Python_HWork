"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item) , количество (quantity), цена (price), покупатель (buyer) , дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""
import json


order1 = {
    'item':'computer',
    'price':'20000',
    'quantity': 1,
    'buyer':'Sergey',
    'data':"2018, 2, 10",}
order2 = {
    'item':'printer',
    'price':'10000',
    'quantity': 1,
    'buyer':'Ivan',
    'data':"2017, 11, 20",}

order3 = {
    'item':'mouse',
    'price':'3000',
    'quantity': 2,
    'buyer':'Tatiana',
    'data':"2017, 8, 5",}
orders = [order1, order2, order3]

def write_order_to_json(item, price, quantity, buyer, data, filename):
    dict_to_json ={
    'item' : item,
    'price': price,
    'quantity': quantity,
    'buyer': buyer,
    'data': data,
    }
    print('dict_to_json: ', dict_to_json)
    with open( filename, 'w+' ) as json_file:
        json.dump(dict_to_json, json_file, sort_keys= True , indent= 4)

def read_order_from_json(filename):
    with open( filename, 'r', encoding="utf-8" ) as json_file:
        python_data = json.load(json_file)
    return python_data



if __name__ == '__main__':
    #print(orders)
    write_order_to_json(order1['item'], order1['price'], order1['quantity'], \
                        order1['buyer'], order1['data'], 'order.json')
    print(read_order_from_json('order.json'))
