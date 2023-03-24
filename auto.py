import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Обязательгные параметры
scope = ["https://spreadsheets.google.com/feeds",
         'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file",
         "https://www.googleapis.com/auth/drive"]

# Подключаем необходимые ключи
creds = ServiceAccountCredentials.from_json_keyfile_name("credents.json", scope)

# Авторизовываемся под своим аккаунтом
client = gspread.authorize(creds)

###########################
