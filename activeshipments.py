import requests
from requests.auth import HTTPBasicAuth
import json
from ratelimit import limits

base_url = 'https://api.cratejoy.com/v1/'
client_id = 'df94894a3515501d479afed2a44bec9e'
client_pass = 'aefd57c3ba705f6aec2d28174acbc1ef'

#function retrieves product information

@limits(calls=100, period=100)
def getActiveSubs():
    #get subscribers information with active parameter
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {
        'status': 'active'
    }
    #sub id, first name, last name, email, status, start date/time, end date/time, shipping phone
    #algorithm design: a.) append all data values into corresponding arrays, b.) append each instance into each
    subscription_ids = []
    first_names = []
    last_names = []
    emails = []
    status = []
    start_dates = []
    end_dates = []
    phone_numbers = []

    next_page = "?page=1"

    while next_page != None:

        r = requests.get(base_url+'subscriptions/'+ next_page, auth=HTTPBasicAuth(client_id, client_pass), params = payload, headers=headers)
        data = r.json()

        for subs in range(len(data['results'])):
            subscription_ids.append(data['results'][subs]['address']['id'])
            first_names.append(data['results'][subs]['customer']['first_name'])
            last_names.append(data['results'][subs]['customer']['last_name'])
            emails.append(data['results'][subs]['customer']['email'])
            status.append(data['results'][subs]['status'])
            start_dates.append(data['results'][subs]['start_date'])
            end_dates.append(data['results'][subs]['end_date'])
            phone_numbers.append(data['results'][subs]['address']['phone_number'])
        
        next_page = data['next']
    
    return subscription_ids, first_names, last_names, emails, status, start_dates, end_dates, phone_numbers

if __name__ == "__main__":
    getActiveSubs()