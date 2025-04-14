'''
Посчитайте Rolling-retention 30 дня (в процентах) для пользователей из той же когорты(для пользователей, зарегистрированных в январе)
Примечание: результат округлите до 5 знаков после запятой
'''
import csv
from datetime import datetime, timedelta

users_month = {}
filter_entries = []
# Открываем на чтение файл "registrations.csv"
with open('registrations.csv', 'r') as registrations:
      reader = csv.DictReader(registrations, delimiter=';', quotechar='"')
# Фильтруем данные файла по регистрации в январе(if datee.month == 1) и записываем в словавь "users_month" (пользователь:дата регистрации)
      for line in reader:
        datee = datetime.strptime(line['registration_date'], '%Y-%m-%d')        
        if datee.month == 1:
            users_month[line['user_id']] = line['registration_date']
# Открываем на чтение файл "entries.csv"
with open('entries.csv', 'r') as entries:
    reader = csv.DictReader(entries, delimiter=';', quotechar='"')
# Фильтруем данные файла по пользователям из словаря users_month (if line['user_id'] in users_month.keys()) и записываем в список "filter_entries"
    for line in reader:
        if line['user_id'] in users_month.keys():
            filter_entries.append(line)
# Создаем функцию, для того чтобы расчитать количество уникальных активных пользователей ...
def qnt_us_day(day):
    day_use = set()
    for i in filter_entries:
# в 0 день
        if day == 0:
            if (datetime.strptime(i['entry_date'], '%Y-%m-%d') - datetime.strptime(users_month[i['user_id']], '%Y-%m-%d')) == timedelta(days=day):
                day_use.add(i['user_id'])
# с "х" дня до последнего дня
        else:
            if (datetime.strptime(i['entry_date'], '%Y-%m-%d') - datetime.strptime(users_month[i['user_id']], '%Y-%m-%d')) >= timedelta(days=day):
                day_use.add(i['user_id'])
    return len(day_use)
# Расчитываем rolling-retention 30 дня и округляем до 5 знаков
rolling_retention = round(qnt_us_day(day=30) / (qnt_us_day(day=0)/100), 5)

print(rolling_retention)



