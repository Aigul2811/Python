'''
Посчитайте Churn rate 29 дня (в долях), посчитанный по всем пользователям
'''
import csv
from datetime import datetime, timedelta

users_month = {}
filter_entries = []
qnt_us = set()

# Открываем на чтение файл "registrations.csv". Создаем датафрейм"users_month" (пользователь:дата регистрации)
with open('registrations.csv', 'r') as registrations:
      reader = csv.DictReader(registrations, delimiter=';', quotechar='"')
      for line in reader:       
        users_month[line['user_id']] = line['registration_date']
# Открываем на чтение файл "entries.csv". Создаем датафрейм "filter_entries"
with open('entries.csv', 'r') as entries:
    reader = csv.DictReader(entries, delimiter=';', quotechar='"')
    for line in reader:        
        filter_entries.append(line)
# Добавляем в множество 'qnt_us' пользователей по дням захода относительно даты регистрации(множества сохранит только уникальных пользователей) с 29 дня до конца   
for i in filter_entries:    
    if (datetime.strptime(i['entry_date'], '%Y-%m-%d') - datetime.strptime(users_month[i['user_id']], '%Y-%m-%d')) >= timedelta(29):    
        qnt_us.add(i['user_id'])
# Рассчитаем количество уникальных пользователей в день регистрации
qnt_us_0 = len(users_month)
# Рассчитывает Churn rate 29 по всем пользователям
churn_29 = (qnt_us_0 - len(qnt_us))/ qnt_us_0

print(churn_29)




