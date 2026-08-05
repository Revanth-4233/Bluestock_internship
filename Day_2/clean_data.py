#for cleaning all files 
import pandas as pd
import os
'''
files = ['01_fund_master.csv', '02_nav_history.csv','03_aum_by_fund_house.csv','04_monthly_sip_inflows.csv','05_category_inflows.csv','06_industry_folio_count.csv','07_scheme_performance.csv','08_investor_transactions.csv','09_portfolio_holdings.csv','10_benchmark_indices.csv']
for f in files:
    df = pd.read_csv(f'data/raw/{f}')
    print(f"\n======{f}======")
    print("Shape: ", df.shape)
    print("\nData Types: \n", df.dtypes)
    print("\nSample Rows: \n",df.head(3))
    print("\nNulls: ",df.isnull().sum())

'''
'''
# ===== Clean nav_history.csv =====
nav = pd.read_csv('data/raw/02_nav_history.csv')
nav['date'] = pd.to_datetime(nav['date'], errors='coerce')
nav = nav.sort_values(['amfi_code', 'date'])

before = len(nav)
nav = nav.drop_duplicates(subset=['amfi_code', 'date'])
print("Removed duplicate rows:", before - len(nav))

nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()

before = len(nav)
nav = nav[nav['nav'] > 0]
print("Removed NAV<=0 rows:", before - len(nav))

nav.to_csv('data/processed/nav_history_clean.csv', index=False)
print("nav_history_clean.csv saved:", nav.shape)

# ===== Sanity check on the CLEANED file (not raw) =====
check = pd.read_csv('data/processed/nav_history_clean.csv')
print("Min NAV:", check['nav'].min())
print("Null dates:", check['date'].isnull().sum())
print("Duplicate (amfi_code,date) pairs:", check.duplicated(subset=['amfi_code','date']).sum())

# ===== Check transaction_type and kyc_status values =====
txn_raw = pd.read_csv('data/raw/08_investor_transactions.csv')
print("transaction_type values:", txn_raw['transaction_type'].unique())
print("kyc_status values:", txn_raw['kyc_status'].unique())

'''
'''
# ===== Clean investor_transactions.csv =====
txn = pd.read_csv('data/raw/08_investor_transactions.csv')

# 1. transaction_type — already standardised, just confirm/enforce
valid_types = ['SIP', 'Lumpsum', 'Redemption']
txn = txn[txn['transaction_type'].isin(valid_types)]

# 2. Validate amount > 0
before = len(txn)
txn = txn[txn['amount_inr'] > 0]
print("Removed amount<=0 rows:", before - len(txn))

# 3. Fix date format
txn['transaction_date'] = pd.to_datetime(txn['transaction_date'], errors='coerce')
print("Null dates after parsing:", txn['transaction_date'].isnull().sum())

# 4. Validate kyc_status enum
valid_kyc = ['Verified', 'Pending']
before = len(txn)
txn = txn[txn['kyc_status'].isin(valid_kyc)]
print("Removed invalid KYC rows:", before - len(txn))

# 5. Save
txn.to_csv('data/processed/investor_transactions_clean.csv', index=False)
print("investor_transactions_clean.csv saved:", txn.shape)

# Sanity check
check = pd.read_csv('data/processed/investor_transactions_clean.csv')
print("Min amount:", check['amount_inr'].min())
print("Unique transaction_type:", check['transaction_type'].unique())
print("Unique kyc_status:", check['kyc_status'].unique())
'''

# ===== Clean scheme_performance.csv =====
perf = pd.read_csv('data/raw/07_scheme_performance.csv')

# 1. Validate return values are numeric (coerce bad values to NaN so we can spot them)
return_cols = ['return_1yr_pct', 'return_3yr_pct', 'return_5yr_pct']
for col in return_cols:
    before_nulls = perf[col].isnull().sum()
    perf[col] = pd.to_numeric(perf[col], errors='coerce')
    after_nulls = perf[col].isnull().sum()
    print(f"{col}: {after_nulls - before_nulls} values became NaN (non-numeric)")

# 2. Flag anomalies — return outside a sane range (-100% to +200%)
perf['is_anomaly'] = perf[return_cols].apply(
    lambda row: any((row < -100) | (row > 200)), axis=1
)
print("Anomalies flagged:", perf['is_anomaly'].sum())

# 3. Check expense_ratio_pct range (0.1% - 2.5%)
perf['expense_ratio_valid'] = perf['expense_ratio_pct'].between(0.1, 2.5)
print("Out-of-range expense ratios:", (~perf['expense_ratio_valid']).sum())

# 4. Save
perf.to_csv('data/processed/scheme_performance_clean.csv', index=False)
print("scheme_performance_clean.csv saved:", perf.shape)

# Sanity check
check = pd.read_csv('data/processed/scheme_performance_clean.csv')
print("Return columns dtype check:", check[return_cols].dtypes.tolist())
print("Anomaly count:", check['is_anomaly'].sum())
print("Expense ratio range:", check['expense_ratio_pct'].min(), "-", check['expense_ratio_pct'].max())