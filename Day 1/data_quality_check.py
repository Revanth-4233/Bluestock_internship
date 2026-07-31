import pandas as pd

fund_master = pd.read_csv('data/processed/01_fund_master.csv')
nav_history = pd.read_csv('data/processed/02_nav_history.csv')
print(fund_master.columns)
'''
print("fund_house: ",fund_master['fund_house'].unique())
print("scheme_names: ",fund_master['scheme_name'].unique())
print("category: ",fund_master['category'].unique())
print("sub_category: ",fund_master['sub_category'].unique())
print("plan: ",fund_master['plan'].unique())
'''
master_code = set(fund_master['amfi_code'])
nav_code = set(nav_history['amfi_code'])

missing = master_code - nav_code
print(f"{len(missing)} codes missing NAV data")





