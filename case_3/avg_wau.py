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
max_week = reduce(lambda x, y: max(x, y), [datetime.strptime(i['entry_date'], '%Y-%m-%d').isocalendar().week for i in filter_entries], 0)

# Создаем список с количеством множеств c max_week() месяцев в году
if max_week >= 53:
    week_use = [set() for r in range(53)]
else:
    week_use = [set() for r in range(max_week)]

# Расчитываем уникальных пользователей на каждую неделю
for i in filter_entries:
    w_u = int((datetime.strptime(i['entry_date'], '%Y-%m-%d')).strftime("%W"))
    week_use[w_u].add(i['user_id'])
      
avg_wau = round(reduce(lambda x, y: x + y, [len(j) for j in week_use], 0)/len(week_use), 5)
print(avg_wau)