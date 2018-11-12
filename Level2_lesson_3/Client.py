# Программа клиента для отправки приветствия серверу и получения ответа
import sys
from socket import *
from datetime import datetime
import json


def client(IP_addr, port=777):
    s = socket(AF_INET, SOCK_STREAM)  # Создать сокет TCP
    s.connect((IP_addr, int(port)))  # соединиться с сервером

    timestamp = str(datetime.now())
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
    server_answer = json.loads(data)

    print('Ответ сервера: ', data.decode('utf-8'), ', длиной ',
          len(data), 'байт получен')

    if server_answer["response"] == 200: # код ответа сервера == 'OK!'
        timestamp = str(datetime.now())
        presence_msg = {"action": "presence", "time": timestamp,
                        "type": "status",
                        "user": {"account_name": "CodeMaverick",
                                 "status": "Yep, I am here!"}}
        json_presence_msg = json.dumps(presence_msg)
        s.send(json_presence_msg.encode('utf-8'))
    else:
        pass

    s.close()


if __name__ == "__main__":
    client('127.0.0.1', 8080)
