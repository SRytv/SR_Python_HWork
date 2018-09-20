# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

#=============================================================
import os
def change_dir(dir_path):
        if not os.path.exists(dir_path):
            result = 2 # change fault, the directory is not exists
            return result
        try:
            os.chdir(dir_path)
            result = 0 # directory was changed
        except:
            result = 1 # directory was not changed
        return result

def delete_dir(dir_path):
    try:
        os.rmdir(dir_path)
        result = 0 # directory was deleted
    except:
        result = 1 # directory was not deleted
    return result

def make_dir(dir_path):
    if os.path.exists(dir_path):
        result = 2 # Error: a directory with the same name is already exists
        return result
    try:
        os.mkdir(dir_path)
        result = 0 # was created
    except:
        result = 1 # directory was not created
    return result

"""
#=1)==========================================================
import os
result = SRHw05_easy.make_dir('.\dir_1')
if result:
    print ("создать директорию '.\dir_1' не удалось")
    if result == 2:
        print ("создать директория с таким именем уже существует")
print ("директория '.\dir_1' успешно создана")

result = SRHw05_easy.make_dir('.\dir_9')
if result:
    print ("создать директорию '.\dir_9' не удалось")
    if result == 2:
        print ("создать директория с таким именем уже существует")
print ("директория '.\dir_9' успешно создана")

#=2)==========================================================
import os
if not os.path.exists('.\dir_1'):
    print ("директория '.\dir_1' не существует удалять нечего")
else:
    SRHw05_easy.delete_dir(r'.\dir_1')
if not os.path.exists('.\dir_1'):
    print ("директория '.\dir_1' успешно удалена")
if not os.path.exists('.\dir_9'):
    print ("директория '.\dir_9' не существует удалять нечего")
else:
    SRHw05_easy.delete_dir(r'.\dir_9')
if not os.path.exists('.\dir_9'):
    print ("директория '.\dir_9' успешно удалена")
#===========================================================
"""
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#===========================================================
import os
def list_dir(path):
        return [ elem for elem in os.listdir(r'.')], [ elem for elem in os.listdir(r'.')  if os.path.isdir(elem)]
        #возвражается кореж (все элементы: только дитрктории)
#===========================================================

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.