-- ================================================
-- BlueStock Mutual Fund Analytics — Queries
-- ================================================

-- 1. Top 5 funds by AUM (from scheme performance, per-scheme AUM)
SELECT f.scheme_name, f.fund_house, p.aum_crore
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.aum_crore DESC
LIMIT 5;

-- 2. Average NAV per month (across all funds)
SELECT d.year, d.month, ROUND(AVG(n.nav), 2) AS avg_nav
FROM fact_nav n
JOIN dim_date d ON n.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;

-- 3. SIP inflow YoY growth (year-over-year totals)
SELECT d.year, SUM(t.amount_inr) AS total_sip_amount
FROM fact_transactions t
JOIN dim_date d ON t.date_id = d.date_id
WHERE t.transaction_type = 'SIP'
GROUP BY d.year
ORDER BY d.year;

-- 4. Transactions by state
SELECT state, COUNT(*) AS txn_count, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- 5. Funds with expense_ratio < 1%
SELECT f.scheme_name, f.fund_house, p.expense_ratio_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
WHERE p.expense_ratio_pct < 1.0
ORDER BY p.expense_ratio_pct;

-- 6. Top 5 fund houses by total AUM (latest date)
SELECT fund_house, aum_crore
FROM fact_aum
WHERE date_id = (SELECT MAX(date_id) FROM fact_aum)
ORDER BY aum_crore DESC
LIMIT 5;

-- 7. Highest Sharpe ratio funds (risk-adjusted return)
SELECT f.scheme_name, p.sharpe_ratio, p.return_1yr_pct
FROM fact_performance p
JOIN dim_fund f ON p.amfi_code = f.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 5;

-- 8. SIP vs Lumpsum vs Redemption — count and total amount by type
SELECT transaction_type, COUNT(*) AS txn_count, SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;

-- 9. Investor age group distribution with average SIP amount
SELECT age_group, COUNT(*) AS investor_count, ROUND(AVG(amount_inr), 2) AS avg_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY age_group
ORDER BY investor_count DESC;

-- 10. City tier (T30 vs B30 proxy) — transaction volume comparison
SELECT city_tier, COUNT(*) AS txn_count, SUM(amount_inr) AS total_amount,
       ROUND(AVG(amount_inr), 2) AS avg_amount
FROM fact_transactions
GROUP BY city_tier
ORDER BY total_amount DESC;