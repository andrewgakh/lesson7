import csv
import json
import datetime
import time
from docxtpl import DocxTemplate

# *********************************************************************************************************************
# Задача 1.
# Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
# *********************************************************************************************************************

with open('cars_info_txt.txt', 'w') as cars:
    cars.write("Марка авто     Модель авто     Расход топлива, л/100км    Стоимость, руб. \n")
    cars.write("Toyota         Land Cruiser            25                 4 000 000  \n")
    cars.write("Nissan         XTrail                  15                 3 000 000  \n")

print()
print('Задача 1.')
print('Содержимое файла cars_info_txt.txt :')
print()

with open('cars_info_txt.txt', 'r') as cars:
    for line in cars:
        print(line)

# *********************************************************************************************************************
# Задача 2.
# Создать doc шаблон, где будут использованы данные параметры. Шаблон price.docx
# Задача 3.
# Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2). price-final.docx
# *********************************************************************************************************************
def context_dict(l):
    '''
    :param l: Список значений
    :return: Формируется cont_dict
    '''
    tmp_name_list = ['retailer', 'marka_avt1', 'model_avt1', 'rashod_avt1', 'price_avt1', 'marka_avt2', 'model_avt2',
                      'rashod_avt2', 'price_avt2']
    cont_dict = {}
    for i in range (len(tmp_name_list)):
         cont_dict[tmp_name_list[i]] = l[i]
    return cont_dict

def gen_price(x, l1, l2):
     '''
     :param x: Наименование компании
     :param l1: Строка 1
     :param l2: Строка 2
     :return: Создание прайса
     '''
     # Формируем список значений
     l=[]
     l.append(x)
     l1+=l2
     for i in range (len(l1)):
         l.append(l1[i])

     # Наполняем шаблон значениями
     context = context_dict(l)
     doc = DocxTemplate("price.docx")
     doc.render(context)
     doc.save("price-final.docx")
     return

line1 = ['Toyota','Land Cruiser','25','4 000 000']
line2 = ['Nissan', 'XTrail', '15', '3 000 000']
name_ret = 'ООО Рога и копыта'

print()
print('Задача 3.')

time_1 = time.time()    # start report
gen_price(name_ret, line1, line2)
time_2 = time.time()    # stop report
delta_time = int((time_2 - time_1)*1000)

print('Файл price-final.docx создан.')
print('время затраченное на отчет', delta_time, ' мс')

# *********************************************************************************************************************
# Задача 4.
# Создать csv файл с данными о машине.
# *********************************************************************************************************************

print()
print('Задача 4.')
car_list = [['Марка авто', 'Модель авто', 'Расход топлива л/100км', 'Стоимость руб.'],
            ['Toyota','Land Cruiser','25','4 000 000'], ['Nissan', 'XTrail', '15', '3 000 000']]
time_rep = ['Время создания отчета']
time_1 = time.time()    # start report

with open('car_price.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(car_list)

time_2 = time.time()    # stop report
delta_time = int((time_2 - time_1)*1000000)
print(time_1)
print(time_2)
print(delta_time)
time_rep.append(delta_time)
time_rep.append('мкс')
car_list.append(time_rep)

with open('car_price.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(car_list)

print('Запись в car_price.csv закончена.')

# *********************************************************************************************************************
# Задача 5.
# Создать json файл с данными о машине.
# *********************************************************************************************************************

dict_cars_1 = {'brand':'Toyota', 'model':'Land Cruiser', 'raskhod':25, 'price':4000000,}
# dict_cars_2 = {'brand':'Nissan', 'model':'XTrail', 'raskhod':15, 'price':3000000,}
data_cars=[]

with open('price_json.txt', 'w') as f:
    json.dump(dict_cars_1, f)
    # json.dump(dict_cars_2, f)

print()
print('Задача 5.')
print('Запись в price_json.txt закончена.')

print('Просмотр файла price_json.txt')
print()
with open('price_json.txt') as f:

    # for i in f:
    data_cars = json.load(f)
    print(data_cars)

