import json
import sys
from openweather import *
import SQLite


print('sys.argv = ', sys.argv)

#if __name__ == '__main__':
export_type = sys.argv[1]
file_export_to = sys.argv[2]
city = sys.argv[3]
if file_export_to == "":
    print ("необходимо задать имя файла лия сохранения результатов")
#city = sys.argv[3]
if city == "":
    print ("необходимо указать город, чьей погодой интересуетесь")
else:
    city = "Moscow"


get_openweather_map_city_list()

check_result = check_city_in_base(city)

if check_result[0]:
    print ("OK! ", city," is in base, city ID: ", check_result[1])
    get_weather(check_result[1])
    with  open(r'.\data\weather.json', 'r', encoding="utf-8") as fweath:
        weather = json.loads(fweath.read())
        print (weather)
        for key in weather:
            print(key, weather[key])
#=====================================================
# работа с базой данных требует отдельной реализации
#=====================================================


