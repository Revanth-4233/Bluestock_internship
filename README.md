# Bluestock Fintech — Data Analytics Internship

Welcome to the **Bluestock Fintech Data Analytics Internship** repository. This repository documents my end-to-end journey as a Data Analyst Intern — chronicling my day-to-day progression, data engineering workflows, statistical modeling, and the capstone **Mutual Fund Analytics Platform**.

---

## 👨‍💻 Intern Profile

- **Name:** Bacchu Venkata Mukesh Revanth
- **Role:** Data Analyst Intern
- **Organization:** Bluestock Fintech
- **Education:** B.Tech in CSE (AI & ML), Class of 2026
- **Domain Focus:** Financial Analytics, Quantitative Risk Modeling, SQL Database Engineering, and Business Intelligence

---

## 🚀 The Data Analytics Process: My Day-to-Day Journey

During this internship, I progressed from raw data collection and quality checks to building a full-stack, enterprise-grade financial analytics suite.

### 📅 Stage 1: Data Ingestion, API Integration & Quality Assurance (Day 1)

- **Objective:** Establish reliable data ingestion channels for historical mutual fund data and real-time NAV feeds.
- **Key Workflows:**
  - **Data Collection:** Ingested 10 core mutual fund datasets covering NAV history, fund master details, AUM by AMC, monthly SIP inflows, and benchmark indices.
  - **Live API Integration:** Developed `data_fetching_api.py` connecting with `mfapi.in` / RapidAPI to retrieve real-time daily NAV records for leading fund houses.
  - **Quality Assurance:** Implemented `data_quality_check.py` to audit schema types, null values, duplicates, and timeline continuity across date ranges.
  - **Initial Cleaning:** Structured modular scripts (`data_cleaning.py`) ensuring clean, standardized inputs for downstream analysis.
- **Key Outcome:** Reliable, automated ingestion pipelines with zero data loss or duplicate records.

---

### 📅 Stage 2: Relational Database Architecture & SQL Analytics (Day 2)

- **Objective:** Design and implement a normalized relational database in SQLite to replace flat files and enable complex financial queries.
- **Key Workflows:**
  - **Schema Modeling:** Designed a star-schema (`schema.sql`) with structured primary and foreign key constraints across funds, categories, AMCs, NAV records, and transactions.
  - **Database Migration:** Automated database loading via `load_db.py`, utilizing batch insertion for 46,000+ daily NAV records into `bluestock_mf.db`.
  - **Analytical Querying:** Authored 15+ business queries in `queries.sql`:
    - Identifying top-performing schemes by trailing 1-year, 3-year, and 5-year returns.
    - Calculating AMC market share and year-over-year AUM growth.
    - Analyzing investor transaction patterns (SIP vs. Lumpsum vs. Redemption).
- **Key Outcome:** High-performance, indexed database (`bluestock_mf.db`) with automated report generation via `run_queries.py`.

---

### 🏆 Stage 3: Mutual Fund Analytics Platform (Project 1 - Capstone)

- **Objective:** Develop an end-to-end analytics platform integrating ETL pipelines, quantitative risk-return modeling, machine learning heuristics, and an interactive executive Power BI dashboard.
- **Core Pillars:**
  1. **Automated ETL Pipeline (`run_pipeline.py`):** Unified data ingestion, live API synchronization, data cleaning, and database loading into a single automated run.
  2. **Exploratory Data Analysis (`EDA_Analysis.ipynb`):** Uncovered industry AUM trends (2022–2025), SIP stability through market volatility, investor demographics by age/tier/state, and sector concentration.
  3. **Quantitative Risk & Return Analytics (`Performance_Analytics.ipynb`):**
     - Computed annualized CAGR, annualized volatility, **Sharpe Ratio** (6.5% risk-free rate), **Sortino Ratio**, and **Treynor Ratio**.
     - Computed **Jensen's Alpha** and **Beta** via OLS regression against Nifty 100 benchmark.
     - Modeled **Maximum Drawdown** and built a composite **Fund Scorecard (0–100 score)**.
  4. **Advanced Risk Modeling (`Advanced_Analytics.ipynb`):**
     - Evaluated **Historical Value at Risk (VaR 95%)** and **Conditional VaR (CVaR / Expected Shortfall)**.
     - Tracked 90-day rolling Sharpe ratios to evaluate fund consistency across market cycles.
     - Quantified sector concentration using the **Herfindahl-Hirschman Index (HHI)**.
  5. **Fund Recommendation Engine (`recommender.py`):** Developed a CLI recommender suggesting optimized fund selections tailored to user risk appetites (`Low`, `Moderate`, `High`).
  6. **Interactive Power BI Dashboard (`MF_Analytic_Dashboard.pbix`):** Built a 5-page executive BI suite with dynamic KPI cards, benchmark comparison charts, category heatmaps, and fund drill-throughs.

---

## 📊 Power BI Dashboard Highlights

The Power BI dashboard provides executive reporting across 5 interactive modules:

| # | Dashboard Module | Description & Key Visuals |
|:---:|:---|:---|
| **1** | **Industry Overview** | Total AUM (₹62.74L Cr), SIP Inflows (₹31K Cr), Folios (26.12 Cr), 2022–2025 AUM growth curve, and AMC market share breakdown. |
| **2** | **Fund Performance** | 3-Year Return vs Risk scatter plot, NAV vs Benchmark index comparison, and sortable multi-metric Fund Scorecard. |
| **3** | **Investor Analytics** | Average SIP by Age Group, Transaction split (SIP 58.5% vs Redemption 35.3%), State-wise transaction volumes. |
| **4** | **SIP & Market Trends** | Dual-axis SIP inflows vs Nifty 50 movement, Category Inflow Heatmap, and Top 5 Inflow Categories FY25. |
| **5** | **NAV Details (Drill-Through)** | Deep-dive historical NAV trajectory for individual selected schemes (e.g., SBI Small Cap Fund). |

> 📸 **Visual Previews:** High-resolution screenshots of all 5 dashboard pages are documented in the [Project 1 Documentation](./PRoject%201/MF_Analytics_Platform/README.md#dashboard-pages--visualizations).

---

## 📁 Repository Organization

| Section | Directory / Link | Description |
|:---|:---|:---|
| **Day 1** | [`Day_1/`](./Day_1/) | Data ingestion scripts, RapidAPI / `mfapi.in` integration, and quality assurance checks. |
| **Day 2** | [`Day_2/`](./Day_2/) | Relational database schema, SQLite database (`bluestock_mf.db`), and 15+ analytical SQL queries. |
| **Project 1** | [`PRoject 1/MF_Analytics_Platform/`](./PRoject%201/MF_Analytics_Platform/) | Capstone project: ETL pipelines, EDA & risk notebooks, Power BI dashboard, and recommendation engine. |

### Detailed File Mapping

- **`Day_1/`**
  - `data_fetching_api.py` — Real-time API pull from `mfapi.in` / RapidAPI.
  - `data_quality_check.py` — Schema, null, and duplicate validation.
  - `data_cleaning.py` — Data transformation and cleaning pipeline.
  - `data/` — Raw and processed files.
- **`Day_2/`**
  - `bluestock_mf.db` — SQLite relational database.
  - `schema.sql` — Star-schema table definitions.
  - `queries.sql` — Business analytical SQL queries.
  - `load_db.py` & `run_queries.py` — Database population and query runners.
  - `data_dictionary.md` — Database data dictionary.
- **`PRoject 1/MF_Analytics_Platform/`**
  - `dashboard/` — Interactive Power BI file (`MF_Analytic_Dashboard.pbix`) and screenshots.
  - `notebooks/` — Jupyter notebooks for EDA, performance analytics, and advanced risk modeling.
  - `reports/` — Executive PDF reports, charts, and slide presentation.
  - `scripts/recommender.py` — Risk-matched fund recommender engine.
  - `run_pipeline.py` — Master execution script for the entire platform.

---

## 🛠️ Tech Stack & Analytical Tools

- **Programming & Analytics:** Python (Pandas, NumPy, SciPy)
- **Business Intelligence & Dashboards:** Microsoft Power BI Desktop
- **Database & Data Warehousing:** SQLite3, SQL, SQLAlchemy
- **Data Ingestion & APIs:** Requests, RapidAPI, MF API (`mfapi.in`)
- **Data Storytelling & Reporting:** Matplotlib, Seaborn, PowerPoint, Markdown
- **Financial & Risk Metrics:** CAGR, Volatility, Sharpe Ratio, Sortino Ratio, Treynor Ratio, Jensen's Alpha, Beta (OLS), VaR (95%), CVaR (95%), HHI Index

---

## 💡 Key Learnings & Outcomes

1. **End-to-End Data Ownership:** Navigated the full data lifecycle — from API scraping and schema design to risk analysis and C-suite reporting.
2. **Financial Data Rigor:** Accounted for real-world market dynamics: market holidays, 252 trading-day annualization, benchmark tracking, and downside risk metrics.
3. **Executive Communication:** Translated complex quantitative metrics into an intuitive Power BI dashboard and presentation deck for non-technical stakeholders.

---

## 📬 Contact & Links

- **Author:** Bacchu Venkata Mukesh Revanth
- **GitHub:** [@Revanth-4233](https://github.com/Revanth-4233)
- **Repository:** [Bluestock Fintech Internship](https://github.com/Revanth-4233/Bluestock_internship)
