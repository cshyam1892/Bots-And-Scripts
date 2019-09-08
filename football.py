#!/usr/bin/env python3

import requests
import json

#url = "https://api.football-data.org/v2/"
url = "https://api.football-data.org/v2/competitions/PL/matches"
headers = {'X-Auth-Token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}
response = requests.get(url + "competitions?plan=TIER_ONE", headers=headers)
for c in response.json()['competitions']:
    print(c)

   # print(c['area']['name'] + " - " + c['name'])
    

