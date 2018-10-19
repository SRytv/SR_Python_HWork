# Задание-1: Решите задачу (дублированную ниже):
 
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
 
# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла
 
class Worker:
    def __init__(self, name, surname, salary, position, norm_hours):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        self.position = position
        self.norm_hours = int(norm_hours)
        self.work_hours = 0
 
    def read_work_hours(self):
        with open('.\DATA\hours_of.txt', 'r', encoding='utf-8') as hours:
            for i in hours.readlines():
                if i == "":
                    break
                else:
                    curr_hours_data = [x for x in i.split(' ') if x != '']
                    if curr_hours_data[0] == self.name and curr_hours_data[1] == self.surname:
                        self.work_hours = int(curr_hours_data[2])
                        break
                    else:
                        continue
 
    def calc_salary(self):
        real_work = self.work_hours/ self.norm_hours
        return int((real_work * self.salary))


    def write_salary(self, salary):
        with open('.\DATA\salary_for_all.txt', 'a', encoding='utf-8') as f:
            f.write(self.name + ' ' + self.surname + ' ' + self.position + ' ' + str(salary))
            f.write('\n')
        f.close()


 
if __name__ == '__main__':
    with open(r'.\data\workers.txt', 'r', encoding='UTF-8') as wokers:
        print ('3', wokers)
        for line in wokers.readlines():
            print('4', line)
            if line == "":

                break
            else:
                splitted_line = [x for x in line.split(' ') if x != '']
                if splitted_line[0] == 'Имя':
                    continue #Это строка заголовка, пропустить ее
                else:
                    workman = Worker(* splitted_line)
                    workman.read_work_hours()
                    salary = workman.calc_salary()
                    workman.write_salary(salary)

 
 
