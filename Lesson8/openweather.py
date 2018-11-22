import json
import gzip
import os
def get_openweather_map_city_list():
    if not os.path.exists(r".\data\city.list.json"):
        #=====================================================
        inF = gzip.GzipFile(r".\data\city.list.json.gz", 'rb')
        s = inF.read()
        inF.close()
        outF = open(r".\data\city.list.json", 'wb')
        outF.write(s)
        outF.close()
        #=====================================================
    return True

def check_city_in_base(city_to_find):
        city_to_find = "Moscow"
        found_dict = []
        with  open(r'.\data\city.list.json', 'r', encoding="utf-8") as fc:
               data = json.loads(fc.read())
               for i in range (len(data)):
                   if data[i]["name"] == city_to_find:
                       found_dict.append(i)
               if found_dict == "":
                   print("город в базе не найден")
               elif len(found_dict) == 1:
                   city_ID = data[found_dict[0]]["id"]
               else:
                   print ("В базе найдено", len(found_dict), "города с таким названием")
                   print("Необходимо уточнить страну!")
                   for j in range(0,len(found_dict)):
                       print (j+1, data[found_dict[j]]["name"], data[found_dict[j]]["country"], data[found_dict[j]]["coord"])
                   answer = int(input("введите номер строки из приведенного выше списка: "))
                   city_ID = data[found_dict[answer-1]]["id"]
               return (True, city_ID)


def get_weather(city_ID):
        appidF = open(r'.\data\app.id', 'r')
        appID = appidF.readline()
        print(appID)
        url = '    http://api.openweathermap.org/data/2.5/weather?id='
        url += str(city_ID)
        url += '&units=metric&appid='
        url += appID
        #===================================================================
    # собственно чтение погоды для города с сайта openweathermap.org,
    # #еще не реализовано,
    #полученый файл записывается в r'.\data\weather.json'
    #===================================================================

    #===================================================================================
    #
    # также требуется дополнительная реализация работы с базой SQLite в файле: SQLite.py
    # if DB_id = open_SQLite_Data_Base(openweathermap):
    #       save_data_into_database(DB_id, data)
    #
    #===================================================================================
