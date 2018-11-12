# программа сервера для получения приветствия от клиента и отпраки ответа
import sys
from socket import *
import json
import logging
from main_logger import log

serv_log = logging.getLogger('server')
serv_log.setLevel(logging.INFO)
format = logging.Formatter("%(asctime)s - %(levelname)s - %(""message)s ")
serv_file_handl = logging.FileHandler(r".\log\server.log", 'a',
                                      encoding='utf-8')
serv_file_handl.setFormatter(format)
serv_log.addHandler(serv_file_handl)
#=======================================================================

def check_user_authority(user):
    if True:
        serv_log.info("Проверка авторизации, соединение разрешено")
        return True
    else:
        serv_log.critical("Проверка авторизации, в соединении отказано")
    return False

@log
def server(IP_addr, port=777):
    serv_log.info('Запуск сервера')
    s = socket(AF_INET, SOCK_STREAM)  # Создает сокет TCP
    s.bind((IP_addr, int(port)))  # Присваивает IP аддрес и порт
    s.listen(5)                   # Переход в режим ожидания запросов;
                                  # одновременно обслуживается не более
                                  # 5 запросов
    while True:
        print('Before accept()')
        client, addr = s.accept()
        print('After accept()')
        data = client.recv(1000000)
        print('Сообщение: ', data.decode('utf-8'), 'длиной: ', len(data),
              ' байт, было отправлено клиентом: ', addr)
        serv_log.info('Получено сообщение от клиента')
        client_query = json.loads(data)
        if client_query["action"] == "authenticate":
            if check_user_authority(client_query["user"]):
                asnswer_msg = {"response": 200, "alert": "Connection allowed"}
                json_snswer_msg = json.dumps(asnswer_msg)
                serv_log.info("Клиенту передано разрешение на соединение")
            else:
                pass

        client.send(json_snswer_msg.encode('utf-8'))

        try :
            # имитация ошибки в работк сервера
            raise ValueError("connection parameters error")
        except ValueError:
            serv_log.warning("Ошибка в параметрах связи, работоспособность "
                                   "восстановлена")

        client.close()
        cleint_log.info('Сервер закрыт')


if __name__ == "__main__":
    server('127.0.0.1', 8080)

