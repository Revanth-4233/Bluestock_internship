# Bluestock Fintech — Data Analytics Internship

Welcome to my **Data Analytics Internship Repository** at **Bluestock Fintech**. This repository documents my end-to-end journey as a Data Analyst Intern — chronicling my day-to-day analytical workflows, technical milestones, and the capstone **Mutual Fund Analytics Platform**.

---

## 👨‍💻 Intern Profile
- **Name:** Bacchu Venkata Mukesh Revanth
- **Degree:** B.Tech in Computer Science & Engineering (AI & ML), Class of 2026
- **Role:** Data Analyst Intern
- **Company:** Bluestock Fintech
- **Focus Areas:** Financial Data Analytics, Quantitative Risk Modeling, SQL Database Engineering, ETL Pipelines, and Business Intelligence (Power BI).

---

## 📖 The Data Analytics Process: My Day-to-Day Journey

During this internship, I transitioned from foundational data engineering tasks to designing an enterprise-grade financial analytics suite. Here is how my day-to-day process evolved:

`
+-------------------------+     +-------------------------+     +-----------------------------------+
|         DAY 1           |     |         DAY 2           |     |             PROJECT 1             |
|  Data Ingestion & APIs  | --> | Database Design & SQL   | --> | Full-Stack MF Analytics Platform  |
|  * Ingest 10 CSVs       |     |  * SQLite star-schema   |     |  * Quantitative Risk & Return     |
|  * RapidAPI live fetch  |     |  * Data normalization   |     |  * 5-Page Power BI Dashboard      |
|  * Data quality checks  |     |  * 15+ business queries |     |  * Fund Recommendation Engine     |
+-------------------------+     +-------------------------+     +-----------------------------------+
`

---

### 🔹 Day 1: Data Ingestion, API Integration & Quality Assurance
**The Challenge:** Build robust ingestion pipelines to capture raw financial datasets and live market feeds with zero data loss.

- **What I Did:**
  - Ingested 10 distinct mutual fund datasets covering NAV history, fund master details, AUM by AMC, monthly SIP inflows, and benchmark indices.
  - Developed data_fetching_api.py to interface with the live mutual fund API (mfapi.in / RapidAPI), retrieving real-time NAV records for leading fund houses.
  - Implemented data_quality_check.py to validate schema integrity, check for missing values, identify duplicate records, and ensure correct data typing.
  - Structured modular cleaning scripts (data_cleaning.py) to prepare initial datasets for downstream processing.
- **Key Takeaway:** Real-world financial data is messy and asynchronous. Establishing automated validation rules on Day 1 prevented downstream data anomalies.

---

### 🔹 Day 2: Relational Database Architecture & SQL Analytics
**The Challenge:** Move beyond flat CSV files by architecting a scalable relational database and querying business insights.

- **What I Did:**
  - Designed a normalized relational schema (schema.sql) modeling funds, categories, AMCs, NAV records, transactions, and benchmark indices in SQLite (luestock_mf.db).
  - Automated database loading via load_db.py, utilizing chunked batch insertions to handle 46,000+ daily NAV records efficiently.
  - Authored advanced analytical queries in queries.sql answering critical business questions:
    - Identifying top-performing funds by 1-year, 3-year, and 5-year returns.
    - Calculating AMC market share and year-over-year AUM growth.
    - Analyzing investor transaction behavior (SIP vs. Lumpsum vs. Redemption).
  - Built 
un_queries.py to automate report generation directly from the database.
- **Key Takeaway:** Optimized indexing and foreign key constraints are essential when querying multi-year time-series financial datasets.

---

### 🔹 Project 1: Mutual Fund Analytics Platform (Capstone)
**The Challenge:** Integrate all previous modules into an end-to-end, production-ready analytics platform combining advanced financial engineering, statistical modeling, machine learning heuristics, and an interactive executive BI dashboard.

- **Core Capabilities Built:**
  1. **Automated ETL Pipeline (
un_pipeline.py):**
     - Orchestrated end-to-end execution across ingestion, live API synchronization, cleaning, metric computation, and database loading.
  2. **Exploratory Data Analysis (EDA_Analysis.ipynb):**
     - Investigated industry AUM trends (2022–2025), SIP volume vs. market cycles, investor demographics by age/tier/state, and sector concentration.
  3. **Performance & Risk Analytics (Performance_Analytics.ipynb):**
     - Computed annualized CAGR, annualized volatility, **Sharpe Ratio** (6.5% risk-free rate), **Sortino Ratio**, **Treynor Ratio**, **Jensen's Alpha**, and **Beta** (OLS regression against Nifty 100).
     - Calculated Maximum Drawdown and developed a multi-factor **Fund Scorecard (0–100 score)**.
  4. **Advanced Risk Modeling (Advanced_Analytics.ipynb):**
     - **Historical Value at Risk (VaR 95%)** and **Conditional VaR (CVaR / Expected Shortfall)**.
     - 90-day rolling Sharpe ratio to identify risk-adjusted consistency through bull and bear markets.
     - **Herfindahl-Hirschman Index (HHI)** to quantify portfolio sector concentration.
  5. **Fund Recommendation Engine (
ecommender.py):**
     - Created a command-line recommendation system that suggests top-ranked mutual funds matching an investor’s risk profile (Low, Moderate, High).
  6. **Interactive Power BI Executive Dashboard (MF_Analytic_Dashboard.pbix):**
     - Built a 5-page enterprise dashboard with dynamic KPI cards, cross-filtering, and drill-through capabilities.

---

## 📊 Power BI Dashboard Highlights

| Page | Title | Key Metrics & Visualizations |
|:---:|:---|:---|
| **1** | **Industry Overview** | Total AUM (₹62.74L Cr), Monthly SIP (₹31K Cr), Folios (26.12 Cr), 2022–2025 AUM Growth Curve, AMC Market Share. |
| **2** | **Fund Performance** | 3-Year Return vs Risk Scatter Plot, NAV vs Benchmark (Nifty 100) trend, Sortable Multi-Metric Fund Scorecard. |
| **3** | **Investor Analytics** | Average SIP by Age Group, Transaction split (SIP 58.5% vs Redemption 35.3%), State-wise Inflow Distribution. |
| **4** | **SIP & Market Trends** | Dual-axis SIP inflows vs Nifty 50 movement, Category Inflow Heatmap, Top 5 Inflow Categories FY25. |
| **5** | **NAV Drill-Through** | Granular historical NAV trajectory for individual funds (e.g., SBI Small Cap Fund). |

> *Full screenshots and visual previews are documented in the [Project 1 Documentation](./PRoject%201/MF_Analytics_Platform/README.md).*

---

## 📁 Repository Structure

`
Bluestock_internship/
│
├── README.md                                 # Root: Internship Journey & Analytics Process
│
├── Day_1/                                    # Day 1: Data Ingestion & Quality Checks
│   ├── data/                                 # Raw & processed data
│   ├── data_cleaning.py                      # Cleaning pipeline
│   ├── data_fetching_api.py                  # Live API ingestion (RapidAPI / mfapi.in)
│   ├── data_quality_check.py                 # Schema & null validation
│   └── requirements.txt
│
├── Day_2/                                    # Day 2: Relational Database & SQL Analytics
│   ├── data/                                 # Source CSVs
│   ├── bluestock_mf.db                       # Normalized SQLite Database
│   ├── clean_data.py                         # Data normalization
│   ├── data_dictionary.md                    # Data dictionary
│   ├── load_db.py                            # Database population script
│   ├── schema.sql                            # Relational schema
│   ├── queries.sql                           # Business analytical SQL queries
│   └── run_queries.py                        # Query execution runner
│
└── PRoject 1/
    └── MF_Analytics_Platform/                # Capstone Project: Mutual Fund Analytics Platform
        ├── dashboard/
        │   ├── MF_Analytic_Dashboard.pbix    # Interactive Power BI Dashboard
        │   └── screenshots/                  # High-resolution dashboard page screenshots
        ├── data/
        │   ├── raw/                          # 10 raw CSVs + live NAV feeds
        │   └── processed/                    # Cleaned data + computed metric reports
        ├── notebooks/
        │   ├── EDA_Analysis.ipynb            # Exploratory Data Analysis
        │   ├── Performance_Analytics.ipynb   # Risk-return & scorecard computations
        │   └── Advanced_Analytics.ipynb      # VaR, CVaR, Rolling Sharpe, HHI
        ├── reports/
        │   ├── charts/                       # 12 high-resolution analytical plots
        │   ├── EDA_Findings.md               # Analytical report
        │   ├── Final_Report.pdf              # Comprehensive project report
        │   └── Presentation.pptx             # Executive slide deck
        ├── scripts/
        │   └── recommender.py                # Fund recommendation engine
        ├── sql/
        │   ├── schema.sql                    # Production SQL schema
        │   └── queries.sql                   # 15+ complex analytical queries
        ├── data_cleaning.py                  # Production cleaning script
        ├── data_ingestion.py                 # Pipeline ingestion
        ├── database_setup.py                 # Database loader
        ├── fetch_live_nav.py                 # Real-time NAV puller
        ├── run_pipeline.py                   # Master pipeline runner
        ├── requirements.txt                  # Python dependencies
        └── README.md                         # Detailed project documentation
`

---

## 🛠️ Technology Stack & Analytical Tooling

- **Data Processing & Analytics:** Python (Pandas, NumPy, SciPy)
- **Data Visualization & Storytelling:** Power BI Desktop, Matplotlib, Seaborn
- **Database & Data Warehousing:** SQLite3, SQL, SQLAlchemy
- **APIs & Ingestion:** Requests, RapidAPI, MF API (mfapi.in)
- **Version Control & Collaboration:** Git, GitHub
- **Analytical Metrics Applied:** CAGR, Sharpe Ratio, Sortino Ratio, Treynor Ratio, Jensen's Alpha, Beta (OLS), Historical VaR (95%), CVaR (95%), HHI Concentration Index.

---

## 💡 Key Learnings & Outcomes

1. **End-to-End Data Ownership:** Learned how to navigate the entire data lifecycle — from scraping/pulling raw data, handling missing records, and structuring databases, to performing financial analysis and presenting to stakeholders.
2. **Financial Data Rigor:** Mastered real-world nuances of mutual fund analytics: adjusting for market holidays, annualizing return metrics with 252 trading days, benchmarking against market indices, and modeling downside risk.
3. **Data Storytelling:** Discovered that complex quantitative calculations become powerful only when paired with clear, interactive BI dashboards that allow executives and investors to slice and drill down into insights.

---

## 📬 Contact

For questions, discussions, or opportunities, feel free to reach out:
- **Author:** Bacchu Venkata Mukesh Revanth
- **GitHub:** [@Revanth-4233](https://github.com/Revanth-4233)
- **Repository:** [Bluestock Fintech Internship](https://github.com/Revanth-4233/Bluestock_internship)
