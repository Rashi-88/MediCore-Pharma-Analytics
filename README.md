# MediCore Pharma Analytics Dashboard

## Pharmaceutical Sales & Commercial Performance Analysis

An interactive analytics dashboard developed to analyze pharmaceutical sales performance across products, customers, geographic markets, and sales representatives.

The project transforms transactional sales data into actionable business insights covering revenue, profitability, product growth, market performance, customer segments, and sales effectiveness.

---

# Project Overview

Pharmaceutical companies generate large volumes of commercial data across products, customers, markets, and sales teams.

This project analyzes pharmaceutical sales data to answer key business questions:

- Which products generate the highest revenue and profitability?
- Which products are growing or declining?
- Which geographic markets perform best?
- Which customer segments contribute the most revenue?
- How are sales representatives performing?
- How has business performance changed between 2024 and 2025?

The final outcome is an interactive Streamlit dashboard designed to support data-driven commercial decision-making.

---

# Dataset

The dataset contains pharmaceutical sales transactions from 2024–2025.

## Dataset Characteristics

- 15,000+ sales transactions
- 8 pharmaceutical products
- 6 European markets
- Customer segmentation information
- Sales representative performance data
- Revenue and profitability metrics

## Key Data Attributes

| Category | Features |
|---|---|
| Transaction Data | Transaction ID, Date, Units Sold, Revenue |
| Product Information | Product Name, Therapeutic Area, Launch Year, Unit Cost |
| Customer Information | Customer Name, Customer Type, Customer Segment |
| Market Information | Country, Region, Market Region, Currency |
| Sales Team | Sales Representative, Experience, Annual Target |
| Financial Metrics | Revenue, Gross Profit, Profit Margin |

---

# Objectives

The main objectives of this project were:

1. Perform exploratory data analysis on pharmaceutical sales data.
2. Identify revenue and profitability drivers.
3. Analyze product-level growth and decline patterns.
4. Evaluate geographic market performance.
5. Understand customer segment contribution.
6. Analyze sales representative performance.
7. Develop an interactive analytics dashboard.

---

# Technologies Used

## Programming & Data Analysis

- Python
- Pandas
- NumPy

## Data Visualization & Dashboard

- Matplotlib
- Streamlit

## Development Tools

- Jupyter Notebook
- Git
- GitHub

---

# Project Workflow

## 1. Data Quality Assessment

Performed data validation including:

- Missing value analysis
- Duplicate transaction detection
- Data consistency checks
- Revenue validation
- Price validation
- Feature verification

---

## 2. Data Preparation

Performed data transformation and feature engineering:

- Date formatting
- Year and month extraction
- Revenue validation
- Gross profit calculation
- Profit margin calculation
- Customer segmentation analysis
- Sales performance metrics

---

## 3. Exploratory Data Analysis

Analyzed:

- Revenue trends
- Product performance
- Product growth and decline
- Geographic market performance
- Customer segments
- Sales representative effectiveness
- Year-over-year changes

---

## 4. Dashboard Development

Developed an interactive Streamlit dashboard containing:

- Executive KPI overview
- Revenue analysis
- Product performance analysis
- Country and market analysis
- Monthly revenue trends
- Profitability analysis
- Customer segment analysis
- Sales representative performance
- Interactive filters

---

# Key Business Insights

## Product Performance

- GlycoCare was one of the strongest revenue-generating products.
- Immunexa demonstrated the strongest year-over-year growth with approximately 26% revenue growth.
- CardioMax experienced the largest decline with approximately 17% revenue reduction.
- Dermacare and GastroRelief showed positive growth trends.
- Product performance varied significantly, highlighting opportunities for targeted commercial strategies.

---

## Market Performance

- Germany was the strongest-performing market based on overall revenue contribution.
- Belgium showed comparatively lower revenue performance.
- Geographic markets demonstrated different growth patterns and business opportunities.

---

## Overall Business Performance

- Total revenue increased by approximately 3.2% between 2024 and 2025.
- Overall business performance improved despite individual product declines.
- Monthly revenue fluctuations indicate opportunities for improved sales planning and market analysis.

---

# Dashboard Preview

## Executive Dashboard Overview

![Dashboard Overview](images/dashboard/Screenshot%202026-08-12%20172140.png)

---

## Product Performance Analysis

![Product Performance](images/dashboard/Screenshot%202026-08-12%20172247.png)

---

## Market Performance Analysis

![Market Analysis](images/dashboard/Screenshot%202026-08-12%20172406.png)

---

## Revenue Trend Analysis

![Revenue Trend](images/dashboard/Screenshot%202026-08-12%20172459.png)

---

## Product Revenue Contribution

![Product Revenue Contribution](images/dashboard/Screenshot%202026-08-12%20172951.png)

---

## Profitability Analysis

![Profitability Analysis](images/dashboard/Screenshot%202026-08-12%20173048.png)

---

## Sales Representative Performance

![Sales Performance](images/dashboard/Screenshot%202026-08-12%20173216.png)

---

## Customer Segment Analysis

![Customer Segment Analysis](images/dashboard/Screenshot%202026-08-12%20173312.png)

---

# Project Structure

```
MediCore_Pharma_Analytics/

│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   └── cleaned/
│       └── sales_analytics_cleaned.csv
│
├── notebooks/
│   └── 01_data_quality_assessment.ipynb
│
└── images/
    └── dashboard/
        ├── Screenshot 2026-08-12 172140.png
        ├── Screenshot 2026-08-12 172247.png
        ├── Screenshot 2026-08-12 172406.png
        ├── Screenshot 2026-08-12 172459.png
        ├── Screenshot 2026-08-12 172951.png
        ├── Screenshot 2026-08-12 173048.png
        ├── Screenshot 2026-08-12 173216.png
        └── Screenshot 2026-08-12 173312.png
```

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>

cd MediCore_Pharma_Analytics
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your browser.

---

# Key Skills Demonstrated

- Exploratory Data Analysis
- Data Cleaning and Validation
- Business Intelligence
- Sales Analytics
- Revenue Analysis
- Profitability Analysis
- Product Performance Analysis
- Geographic Market Analysis
- Data Visualization
- Interactive Dashboard Development
- Python Programming
- Pandas
- Streamlit

---

# Future Improvements

Potential extensions:

- Integration with real-time sales databases
- Automated reporting pipelines
- Cloud deployment
- Integration with enterprise BI platforms

---

# Author

**Rashi Sunil Malghe**

M.Sc. Digital Health & Data Science

Technical Skills:
Python | Data Analytics | Business Intelligence | Healthcare Analytics | Streamlit | Data Visualization