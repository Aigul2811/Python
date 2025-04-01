import gspread
from oauth2client.service_account import ServiceAccountCredentials

from datetime import date, datetime, timedelta

# Указываем необходимые права доступа к таблицам
scope = ['https://www.googleapis.com/auth/spreadsheets.readonly',
         'https://www.googleapis.com/auth/drive']

# Загружаем ключи аутентификации из файла json
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
#creds = ServiceAccountCredentials.from_json_keyfile_name('C:\Users\79777\OneDrive\Рабочий стол\case_2\creds.json', scope)

# Авторизуемся в Google Sheets API
client = gspread.authorize(creds)

sheet1 = client.open("Installments").worksheet("Лист1")
sheet2 = client.open("Installments").worksheet("Лист2")
sheet3 = client.open("Installments").worksheet("Лист3")

sheet1_data = sheet1.get_all_records()
sheet2_data = sheet2.get_all_records()
sheet3_data = sheet3.get_all_records()


def generate_report(sheet1, sheet2, sheet3):
    arrears = {}

    for el in sheet2_data:
        days_arrears = datetime(2023, 3, 1) - datetime.strptime(el["last_payment_date"], '%d.%m.%Y')
        number_delays = days_arrears.days // 183
        if number_delays >= 1:
            arrears[el["student_id"]] = number_delays

    for i in sheet3_data:
        if i["student_id"] in arrears.keys():
            arrears[i["student_id"]] = i["one-time_payment"] * arrears[i["student_id"]]

    for j in sheet1_data:
        if j["student_id"] in arrears.keys():
            name = j["student_name"]
            debt = arrears[j["student_id"]]
            print(f"Студент {name} - долг {debt} рублей")