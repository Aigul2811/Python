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

# Определяем максимальный день в году
min_day = datetime(2030,1,1)
max_day = datetime(2000,1,1)
for i in filter_entries:
    day_us = datetime.strptime(i['entry_date'], '%Y-%m-%d')
    min_day = min(min_day, day_us)
    max_day = max(max_day, day_us)

# Определяем количество дней между первым и последним заходом
cnt_day = int((max_day - min_day).total_seconds()/86400) + 1

# Создаем список с количеством множеств c max_week() месяцев в году
if cnt_day >= 365:
    d_use = [set() for r in range(365)]
else:
    d_use = [set() for r in range(cnt_day)]

# Расчитываем уникальных пользователей на каждый месяц  
[d_use[int(((datetime.strptime(el['entry_date'], '%Y-%m-%d')) - min_day).total_seconds()/86400)].add(el['user_id']) for el in filter_entries]

dec_dau = len(d_use[-1])
print(dec_dau)