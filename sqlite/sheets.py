import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive',
'https://www.googleapis.com/auth/drive.file',
"https://spreadsheets.google.com/feeds", 
]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)



sh = client.open("Stock Watchlist")
worksheet = sh.get_worksheet(0)

#ws2 = sh.add_worksheet(title="number 1", rows="100", cols="20")

values_list = worksheet.row_values(1)
list_of_dicts = worksheet.get_all_records()
list_of_lists = worksheet.get_all_values()

pprint(list_of_dicts)
