# Программа клиента для отправки приветствия серверу и получения ответа
import sys
from socket import *
from datetime import datetime
import json
import logging

#cleint_log = logging.getLogger('messager')  # для совместного логгирования
#в общий лог
cleint_log = logging.getLogger('client')
cleint_log.setLevel(logging.INFO)
format = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %("
                           "message)s ")
client_file_handl = logging.FileHandler(r".\log\client_log.py", 'a',
                                      encoding='utf-8')
client_file_handl.setFormatter(format)
cleint_log.addHandler(client_file_handl)
#=======================================================================


def client(IP_addr, port=777):
    cleint_log.info('Запуск клиентской программы')
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((IP_addr, int(port)))  # соединиться с сервером

    timestamp = str(datetime.now())
    cleint_log.info('Запрос клиента на подключение к серверу и авторизацию')
    authen_msg = {
        "action": "authenticate",
        "time": timestamp,
        "user": {
            "account_name": "C0deMaverick",
            "password": "CorrectHorseBatterStaple"
        }
    }
    json_autent_msg = json.dumps(authen_msg)
    s.send(json_autent_msg.encode('utf-8'))
    data = s.recv(1000000)
    cleint_log.info(
        'Получение ответа сервера с разрешением или запретом подключения')
    server_answer = json.loads(data)

    print('Ответ сервера: ', data.decode('utf-8'), ', длиной ',
          len(data), 'байт получен')

    if server_answer["response"] == 200: # код ответа сервера == 'OK!'
        timestamp = str(datetime.now())
        presence_msg = {"action": "presence", "time": timestamp,
                        "type": "status",
                        "user": {"account_name": "CodeMaverick",
                                 "status": "Yep, I am here!"}}
        cleint_log.info('Посылка клиентом сервисного сообщения о присутствии')
        json_presence_msg = json.dumps(presence_msg)
        s.send(json_presence_msg.encode('utf-8'))
    else:
        pass

    s.close()
    cleint_log.info('Клиентская программа закрыта')


if __name__ == "__main__":
    client('127.0.0.1', 8080)
