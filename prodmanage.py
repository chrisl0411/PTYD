# Title: PTYD Sample Project Implementation (Product Management)
# Description: Script to extract data from google spreadsheets
# Contributor: Chris Lee

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#set up credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

# login to Google API using OAuth2 credentials.
gc = gspread.authorize(creds)

# opens worksheet using sheet ID
sheet = gc.open_by_key('1Hdmr6T-NG35rmAqgHL-d5qqXbu_JQNaU6Kii0JJ1OAM').worksheet("Products")

# data gets all records
data = sheet.get_all_records()

# product_names extracts first column of spreadsheet
product_names = sheet.col_values(1)

#i terates through first column to print out all products
for product in range(1,len(product_names)-1):
    print(str(product_names[product]))

############Comments###########
#product names then can be applied to cratejoy api