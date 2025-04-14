'''
Посчитайте Mau, Wau, Dau за последний месяц/неделю/день записей
Примечание: последний месяц записей - декабрь. Поэтому mau рассчитываем для декабря (2021 года), 
для wau берем последнюю неделю - с 25 по 31 декабря, и для dau соответственно последний день - 31 декабря.
'''

import csv
from datetime import datetime
from functools import reduce

filter_entries = []

# Открываем на чтение файл "entries.csv". Переносим данные в наш датафрейм "filter_entries"
with open('entries.csv', 'r') as entries:
    reader = csv.DictReader(entries, delimiter=';', quotechar='"')
    for line in reader:        
        filter_entries.append(line)

# Определяем максимальный месяц в году
max_month = 0
for i in filter_entries:
    day_us = datetime.strptime(i['entry_date'], '%Y-%m-%d')
    max_month = max(max_month, day_us.month)    

# Создаем список с количеством множеств c max_month() месяцев в году
month_use = [set() for r in range(max_month)]

# Расчитываем уникальных пользователей на каждый месяц   
[month_use[(datetime.strptime(el['entry_date'], '%Y-%m-%d')).month-1].add(el['user_id']) for el in filter_entries]

dec_mau = len(month_use[-1])
print(dec_mau)