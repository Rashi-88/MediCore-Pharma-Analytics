# MediCore Pharma Analytics Dashboard

## Pharmaceutical Sales & Commercial Performance Analytics

MediCore Pharma Analytics is an interactive business intelligence dashboard developed using **Python, Pandas, Matplotlib, and Streamlit** to analyze pharmaceutical sales performance, revenue trends, profitability, product performance, market distribution, and sales representative effectiveness.

The project demonstrates an end-to-end analytics workflow including data cleaning, exploratory data analysis, KPI development, visualization, and business insight generation.

---

# Project Overview

This dashboard transforms pharmaceutical transaction data into actionable business insights.

Key analysis areas:

- Revenue and profitability analysis
- Product performance evaluation
- Country and market comparison
- Sales representative performance
- Customer segment analysis
- Year-over-year growth analysis
- Interactive filtering

---

# Dashboard Preview

## Dashboard Overview

![Dashboard Overview](images%20dashboard/dashboard_overview.png)

---

## Revenue Analysis

The dashboard analyzes revenue contribution across products and markets.

Key insights:

- GlycoCare is one of the strongest revenue-generating products.
- Germany represents the strongest performing market.
- Product and regional performance varies significantly.

![Revenue by Product and Country](images%20dashboard/revenue_product_country.png)

---

## Monthly Revenue Trends

Revenue trends are analyzed over time to identify fluctuations and performance patterns.

![Monthly Revenue Trend](images%20dashboard/monthly_revenue_trend.png)

---

## Year-over-Year Revenue and Product Contribution

The dashboard compares yearly performance and identifies products driving business growth.

Key findings:

- Revenue increased approximately 3.2% from 2024 to 2025.
- Immunexa showed the strongest year-over-year growth.
- CardioMax experienced the largest revenue decline.

![Yearly Revenue and Product Contribution](images%20dashboard/yearly_revenue_product_share.png)

---

## Profitability Analysis

Profitability metrics are analyzed using gross profit and profit margin comparisons.

Insights:

- GlycoCare generated the highest gross profit.
- GastroRelief demonstrated strong profitability.
- Product margins vary across the portfolio.

![Profit Analysis](images%20dashboard/profit_analysis.png)

---

## Sales Representative Performance

Sales team performance is evaluated based on revenue contribution.

![Sales Representative Performance](images%20dashboard/sales_representative_performance.png)

---

## Customer Segment Analysis

Customer groups are analyzed to understand revenue contribution.

![Customer Segment Analysis](images%20dashboard/customer_segment_analysis.png)

---

## Business Insights

The dashboard summarizes important commercial findings.

![Business Insights](images%20dashboard/business_insights.png)

---

# Key Business Insights

## Product Performance

- GlycoCare and CardioMax are major revenue contributors.
- Immunexa achieved the strongest growth.
- CardioMax showed a significant decline.
- Dermacare and GastroRelief demonstrated positive growth.

## Market Performance

- Germany is the strongest overall market.
- Belgium represents a lower-performing market.
- Regional performance differs considerably.

## Overall Performance

- Revenue increased from 2024 to 2025.
- Business performance remains positive with mixed product trends.
- Monthly revenue shows fluctuations throughout the period.

---

# Technology Stack

## Programming
- Python

## Data Analysis
- Pandas
- NumPy

## Visualization
- Matplotlib
- Streamlit

## Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

# Project Structure
MediCore_Pharma_Analytics/

│
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│ └── cleaned/
│ └── sales_analytics_cleaned.csv
│
├── notebooks/
│ └── 01_data_quality_assessment.ipynb
│
├── images dashboard/
│ ├── dashboard_overview.png
│ ├── revenue_product_country.png
│ ├── monthly_revenue_trend.png
│ ├── yearly_revenue_product_share.png
│ ├── profit_analysis.png
│ ├── sales_representative_performance.png
│ ├── customer_segment_analysis.png
│ └── business_insights.png
│
└── scripts/


---

# Running the Dashboard Locally

Clone the repository:

```bash
git clone https://github.com/Rashi-88/MediCore-Pharma-Analytics.git

Navigate into the project:

cd MediCore-Pharma-Analytics

Install dependencies:

pip install -r requirements.txt

Run Streamlit:

streamlit run app.py
Dataset

The dataset contains pharmaceutical sales transactions including:

Transaction information
Product details
Customer information
Geographic markets
Sales representative data
Revenue and profitability metrics

Dataset size:

15,000 transactions
Multiple products
Multiple European markets
Multiple customer segments
Future Improvements

Possible extensions:

Interactive Plotly visualizations
Cloud deployment
Automated reporting
Predictive analytics models
Author

Rashi Malghe

M.Sc. Digital Health & Data Science

GitHub:
https://github.com/Rashi-88