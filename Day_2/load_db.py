import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# ===== 1. Create database + tables from schema.sql =====
conn = sqlite3.connect('bluestock_mf.db')
with open('schema.sql', 'r') as f:
    conn.executescript(f.read())
conn.close()
print("Tables created.")

engine = create_engine('sqlite:///bluestock_mf.db')

# ===== 2. Load cleaned + raw source files =====
fund_master = pd.read_csv('data/raw/01_fund_master.csv')
nav = pd.read_csv('data/processed/nav_history_clean.csv', parse_dates=['date'])
txn = pd.read_csv('data/processed/investor_transactions_clean.csv', parse_dates=['transaction_date'])
perf = pd.read_csv('data/processed/scheme_performance_clean.csv')
aum = pd.read_csv('data/raw/03_aum_by_fund_house.csv', parse_dates=['date'])

# ===== 3. Build dim_date from every date seen across datasets =====
all_dates = pd.concat([nav['date'], txn['transaction_date'], aum['date']]).dropna().unique()
dim_date = pd.DataFrame({'full_date': pd.to_datetime(all_dates)})
dim_date['date_id'] = dim_date['full_date'].dt.strftime('%Y%m%d').astype(int)
dim_date['year'] = dim_date['full_date'].dt.year
dim_date['month'] = dim_date['full_date'].dt.month
dim_date['day'] = dim_date['full_date'].dt.day
dim_date['quarter'] = dim_date['full_date'].dt.quarter
dim_date['is_weekend'] = dim_date['full_date'].dt.dayofweek >= 5
dim_date = dim_date.drop_duplicates(subset='date_id').sort_values('date_id')

# ===== 4. Map date_id into fact tables =====
nav['date_id'] = nav['date'].dt.strftime('%Y%m%d').astype(int)
txn['date_id'] = txn['transaction_date'].dt.strftime('%Y%m%d').astype(int)
aum['date_id'] = aum['date'].dt.strftime('%Y%m%d').astype(int)

# ===== 5. Load into SQLite =====
fund_master.to_sql('dim_fund', engine, if_exists='append', index=False)
dim_date.to_sql('dim_date', engine, if_exists='append', index=False)
nav[['amfi_code', 'date_id', 'nav']].to_sql('fact_nav', engine, if_exists='append', index=False)

txn_cols = ['investor_id','amfi_code','date_id','transaction_type','amount_inr','state',
            'city','city_tier','age_group','gender','annual_income_lakh','payment_mode','kyc_status']
txn[txn_cols].to_sql('fact_transactions', engine, if_exists='append', index=False)

perf_cols = ['amfi_code','return_1yr_pct','return_3yr_pct','return_5yr_pct','benchmark_3yr_pct',
             'alpha','beta','sharpe_ratio','sortino_ratio','std_dev_ann_pct','max_drawdown_pct',
             'aum_crore','expense_ratio_pct','morningstar_rating','risk_grade','is_anomaly','expense_ratio_valid']
perf[perf_cols].to_sql('fact_performance', engine, if_exists='append', index=False)

aum[['date_id','fund_house','aum_lakh_crore','aum_crore','num_schemes']].to_sql('fact_aum', engine, if_exists='append', index=False)

print("All tables loaded.")

# ===== 6. Verify row counts =====
conn = sqlite3.connect('bluestock_mf.db')
checks = {
    'dim_fund': len(fund_master),
    'dim_date': len(dim_date),
    'fact_nav': len(nav),
    'fact_transactions': len(txn),
    'fact_performance': len(perf),
    'fact_aum': len(aum)
}
for table, expected in checks.items():
    actual = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
    status = "OK" if actual == expected else "MISMATCH"
    print(f"{table}: expected {expected}, got {actual} -> {status}")
conn.close()