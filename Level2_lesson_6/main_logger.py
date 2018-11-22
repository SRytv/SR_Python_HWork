# программа сервера для получения приветствия от клиента и отпраки ответа
import sys
from socket import *
import json
import logging
from functools import wraps

#=======================================================================
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__name__)
        main_logger_log = logging.getLogger('main_logger')
        main_logger_log.setLevel(logging.INFO)
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(""message)s ")
        serv_file_handl = logging.FileHandler(r".\log\main_logger.log", 'a',
                                      encoding='utf-8')
        serv_file_handl.setFormatter(format)
        main_logger_log.addHandler(serv_file_handl)
        main_logger_log.info("Программа:  "+func.__name__+" запущена с параметрами: "
                             +str(args)+', '+str(kwargs))
        return func(*args, **kwargs)
    return wrapper
#=======================================================================
