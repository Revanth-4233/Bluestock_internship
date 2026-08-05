# Data Dictionary — BlueStock Mutual Fund Analytics

## dim_fund
Source: `01_fund_master.csv`

| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER (PK) | Unique AMFI identifier for the fund scheme |
| fund_house | TEXT | Asset Management Company (AMC) managing the fund |
| scheme_name | TEXT | Full name of the mutual fund scheme |
| category | TEXT | Broad fund category (e.g. Equity, Debt, Hybrid) |
| sub_category | TEXT | Fund sub-category (e.g. Large Cap, Small Cap) |
| plan | TEXT | Plan type (Regular / Direct) |
| launch_date | DATE | Date the scheme was launched |
| benchmark | TEXT | Benchmark index the fund is measured against |
| expense_ratio_pct | REAL | Annual expense ratio (%) |
| exit_load_pct | REAL | Exit load charged on early redemption (%) |
| min_sip_amount | INTEGER | Minimum SIP investment amount (INR) |
| min_lumpsum_amount | INTEGER | Minimum lumpsum investment amount (INR) |
| fund_manager | TEXT | Name of the fund manager |
| risk_category | TEXT | Risk classification (Low/Moderate/High/Very High) |
| sebi_category_code | TEXT | SEBI-assigned category code |

## dim_date
Source: Generated calendar table (derived from all dates across fact tables)

| Column | Type | Description |
|---|---|---|
| date_id | INTEGER (PK) | Date key in YYYYMMDD format |
| full_date | DATE | Actual calendar date |
| year | INTEGER | Calendar year |
| month | INTEGER | Calendar month (1-12) |
| day | INTEGER | Day of month |
| quarter | INTEGER | Calendar quarter (1-4) |
| is_weekend | BOOLEAN | True if Saturday/Sunday |

## fact_nav
Source: `02_nav_history.csv` (cleaned → `nav_history_clean.csv`)

| Column | Type | Description |
|---|---|---|
| nav_id | INTEGER (PK) | Auto-generated surrogate key |
| amfi_code | INTEGER (FK) | Links to dim_fund |
| date_id | INTEGER (FK) | Links to dim_date |
| nav | REAL | Net Asset Value on that date |

**Cleaning notes:** dates parsed to datetime, sorted by amfi_code+date, forward-filled for missing NAV (weekends/holidays), duplicates removed, NAV<=0 rows removed. Source data had 0 issues — all 46,000 rows retained.

## fact_transactions
Source: `08_investor_transactions.csv` (cleaned → `investor_transactions_clean.csv`)

| Column | Type | Description |
|---|---|---|
| transaction_pk | INTEGER (PK) | Auto-generated surrogate key |
| investor_id | TEXT | Unique investor identifier |
| amfi_code | INTEGER (FK) | Links to dim_fund |
| date_id | INTEGER (FK) | Links to dim_date |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | T30 (top 30 cities) or B30 (beyond top 30) |
| age_group | TEXT | Investor age bracket |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Investor's annual income (INR lakh) |
| payment_mode | TEXT | UPI / Cheque / Mandate / etc. |
| kyc_status | TEXT | Verified / Pending |

**Cleaning notes:** transaction_type already standardised (SIP/Lumpsum/Redemption), dates parsed, amount validated > 0, KYC filtered to valid enum values (Verified/Pending — no "Rejected" present in this dataset). All 32,778 rows retained — no data quality issues found.
**Coverage note:** this dataset only contains transactions for 2024–2025 (does not go back to 2022 like NAV data).

## fact_performance
Source: `07_scheme_performance.csv` (cleaned → `scheme_performance_clean.csv`)

| Column | Type | Description |
|---|---|---|
| performance_id | INTEGER (PK) | Auto-generated surrogate key |
| amfi_code | INTEGER (FK) | Links to dim_fund |
| return_1yr_pct | REAL | 1-year trailing return (%) |
| return_3yr_pct | REAL | 3-year annualised return (%) |
| return_5yr_pct | REAL | 5-year annualised return (%) |
| benchmark_3yr_pct | REAL | Benchmark's 3-year return (%) |
| alpha | REAL | Excess return vs benchmark |
| beta | REAL | Volatility relative to benchmark |
| sharpe_ratio | REAL | Risk-adjusted return measure |
| sortino_ratio | REAL | Downside-risk-adjusted return |
| std_dev_ann_pct | REAL | Annualised standard deviation (%) |
| max_drawdown_pct | REAL | Maximum peak-to-trough decline (%) |
| aum_crore | INTEGER | Assets under management for this scheme (INR crore) |
| expense_ratio_pct | REAL | Annual expense ratio (%) |
| morningstar_rating | INTEGER | Morningstar star rating (1-5) |
| risk_grade | TEXT | Risk classification |
| is_anomaly | BOOLEAN | Flagged if any return value fell outside -100% to +200% |
| expense_ratio_valid | BOOLEAN | True if expense_ratio_pct within 0.1%-2.5% range |

**Cleaning notes:** all return values validated as numeric, no anomalies found, all expense ratios within valid range (0.55%-1.64%). This is a point-in-time snapshot — no date dimension linked.

## fact_aum
Source: `03_aum_by_fund_house.csv`

| Column | Type | Description |
|---|---|---|
| aum_id | INTEGER (PK) | Auto-generated surrogate key |
| date_id | INTEGER (FK) | Links to dim_date |
| fund_house | TEXT | AMC name |
| aum_lakh_crore | REAL | Total AUM in lakh crore INR |
| aum_crore | INTEGER | Total AUM in crore INR |
| num_schemes | INTEGER | Number of schemes managed by this fund house |

**Grain note:** this table is at fund-house level (quarterly snapshots), NOT per-scheme — different grain from fact_performance's aum_crore, which is per individual scheme.

---

## Row Count Summary (as of last load)
| Table | Row Count |
|---|---|
| dim_fund | 40 |
| dim_date | 1,297 |
| fact_nav | 46,000 |
| fact_transactions | 32,778 |
| fact_performance | 40 |
| fact_aum | 90 |