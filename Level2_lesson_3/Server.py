# программа сервера для получения приветствия от клиента и отпраки ответа
import sys
from socket import *
import json


def check_user_authority(user):
    pass
    return True


def server(IP_addr, port=777):
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    s.bind((IP_addr, int(port)))      # Присваивает IP аддрес и порт
    s.listen(5)                       # Переход в режим ожидания запросов;
                                      # одновременно обслуживается не более
                                      # 5 запросов
    while True:
        print('Before accept()')
        client, addr = s.accept()
        print('After accept()')
        data = client.recv(1000000)
        print('Сообщение: ', data.decode('utf-8'), 'длиной: ', len(data),
              ' байт, было отправлено клиентом: ', addr)
        client_query = json.loads(data)
        if client_query["action"] == "authenticate":
            if check_user_authority(client_query["user"]):
                asnswer_msg = {"response": 200, "alert": "Connection allowed"}
                json_snswer_msg = json.dumps(asnswer_msg)
            else:
                pass

        client.send(json_snswer_msg.encode('utf-8'))
        client.close()


if __name__ == "__main__":
    server('127.0.0.1', 8080)
