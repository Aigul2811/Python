'''
Посчитайте Lifetime по всем пользователям, посчитанный как интеграл от n-day retention
Примечание: результат округлите до 5 знаков после запятой
'''
import csv
from datetime import datetime, timedelta

users_month = {}
filter_entries = []

# Открываем на чтение файл "registrations.csv". Переносим данные в наш датафрейм "users_month" (пользователь:дата регистрации)
with open('registrations.csv', 'r') as registrations:
      reader = csv.DictReader(registrations, delimiter=';', quotechar='"')
      for line in reader:       
        users_month[line['user_id']] = line['registration_date']
# Открываем на чтение файл "entries.csv". Переносим данные в наш датафрейм "filter_entries"
with open('entries.csv', 'r') as entries:
    reader = csv.DictReader(entries, delimiter=';', quotechar='"')
    for line in reader:        
        filter_entries.append(line)
# Создаем функцию, для того чтобы расчитать максимальный последний день захода пользователя относительно даты регистрации        
def max_day():
    max_day = timedelta(0)
    for i in filter_entries:
        day_us = (datetime.strptime(i['entry_date'], '%Y-%m-%d') - datetime.strptime(users_month[i['user_id']], '%Y-%m-%d')) 
        max_day = max(day_us, max_day)
    return int(max_day.total_seconds()/86400)
# Создаем список с количеством множеств max_day(). Каждое множество - это день захода относительно даты регистрации
day_use = [set() for r in range(max_day()+1)]
# Добавляем в список 'day_use' пользователей по дням захода относительно даты регистрации(множества сохранит только уникальных пользователей)   
for i in filter_entries:
    dat = int((datetime.strptime(i['entry_date'], '%Y-%m-%d') - datetime.strptime(users_month[i['user_id']], '%Y-%m-%d')).total_seconds()/86400)
    day_use[dat].add(i['user_id'])
# Рассчитывает Lifetime по всем пользователям
day_0 = len(day_use[0])
lifetime = 0
for j in day_use:
    lifetime += len(j)/day_0
# Округляем Lifetime
lifetime = round(lifetime, 5)

print(lifetime)



