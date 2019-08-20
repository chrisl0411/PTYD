# Title: PTYD Sample Project Implementation (Product Management)
# Description: Script to extract data from google spreadsheets
# Contributor: Chris Lee

import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from activeshipments import getActiveSubs
from ratelimit import limits, sleep_and_retry
import time

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#set up credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

# login to Google API using OAuth2 credentials.
gc = gspread.authorize(creds)
def get_sheets_info(gc):
    # opens worksheet using sheet ID
    sheet = gc.open_by_key('1T9IxPUzCq0aeOumngHXWBuycv7BKowA4YDWDJBcttM0').worksheet("Text Reminder")

    # data gets all records
    data = sheet.get_all_records()

    # product_names extracts first column of spreadsheet
    product_names = sheet.col_values(1)

    #i terates through first column to print out all products
    for product in range(1,len(product_names)-1):
        print(str(product_names[product]))

#@limits(calls=100, period=100)
def push_active_subscribers(gc):
    subscribers = gc.open_by_key('1T9IxPUzCq0aeOumngHXWBuycv7BKowA4YDWDJBcttM0').worksheet("Active Subscribers")

    #gets data from activeshipments.py
    subscription_ids, first_names, last_names, emails, status, start_dates, end_dates, phone_numbers = getActiveSubs()

    all_data = []
    all_data.append(subscription_ids)
    all_data.append(first_names)
    all_data.append(last_names)
    all_data.append(emails)
    all_data.append(status)
    all_data.append(start_dates)
    all_data.append(end_dates)
    all_data.append(phone_numbers)

    for col in range(len(all_data)):
        for row in range(len(all_data[col])):
            subscribers.update_cell(row+2, col+1, all_data[col][row])
            time.sleep(1)

    #need to account for if there are fewer active members than last week, delete the extra lines of data

if __name__ == "__main__":
    #get_sheets_info(gc)
    push_active_subscribers(gc)

############Comments###########
#product names then can be applied to cratejoy api