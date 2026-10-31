''' to fetch the data using request.get() and convert the data into json .json() after conevrt the data into
dataframe  pd.Dataframe() after convert the data frame into csv file  .to_csv()
'''


import requests
import pandas as pd

response = requests.get('https://api.mfapi.in/mf/125497')

data = response.json()
nav_df = pd.DataFrame(data['data'])
nav_df.to_csv('data/processed/hdfc_top_100.csv',index= False)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for name, code in schemes.items():
    r = requests.get('https://api.mfapi.in/mf/119551')
    df = pd.DataFrame(r.json()['data'])
    df.to_csv(f'data/processed/{name}_nav.csv',index=False)


