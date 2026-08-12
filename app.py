import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MediCore Pharma Analytics",
    page_icon="💊",
    layout="wide"
)

# =========================================================
# LOAD DATA
# =========================================================

@st.cache_data
def load_data():
    df = pd.read_csv(
        "data/cleaned/sales_analytics_cleaned.csv"
    )

    df["Date"] = pd.to_datetime(df["Date"])

    return df


df = load_data()

# =========================================================
# TITLE
# =========================================================

st.title("💊 MediCore Pharma Analytics")

st.markdown(
    """
    **Pharmaceutical Sales & Commercial Performance Dashboard**

    Explore revenue, profitability, product performance, market trends,
    and sales representative performance across 2024–2025.
    """
)

st.divider()

# =========================================================
# SIDEBAR FILTERS
# =========================================================

st.sidebar.header("🔎 Dashboard Filters")

selected_year = st.sidebar.multiselect(
    "Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

selected_product = st.sidebar.multiselect(
    "Product",
    sorted(df["Product_Name"].unique()),
    default=sorted(df["Product_Name"].unique())
)

selected_country = st.sidebar.multiselect(
    "Country",
    sorted(df["Country"].unique()),
    default=sorted(df["Country"].unique())
)

filtered_df = df[
    (df["Year"].isin(selected_year)) &
    (df["Product_Name"].isin(selected_product)) &
    (df["Country"].isin(selected_country))
]

# =========================================================
# KPI SECTION
# =========================================================

total_revenue = filtered_df["Revenue"].sum()
total_profit = filtered_df["Gross_Profit"].sum()
total_units = filtered_df["Units_Sold"].sum()
transactions = filtered_df["Transaction_ID"].nunique()

profit_margin = (
    total_profit / total_revenue * 100
    if total_revenue > 0 else 0
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "💰 Total Revenue",
    f"€{total_revenue:,.0f}"
)

col2.metric(
    "📈 Gross Profit",
    f"€{total_profit:,.0f}"
)

col3.metric(
    "📦 Units Sold",
    f"{total_units:,.0f}"
)

col4.metric(
    "🧾 Transactions",
    f"{transactions:,}"
)

col5.metric(
    "📊 Profit Margin",
    f"{profit_margin:.1f}%"
)

st.divider()

# =========================================================
# ROW 1 — PRODUCT + COUNTRY
# =========================================================

col1, col2 = st.columns(2)

# ---------------- PRODUCT REVENUE ----------------

with col1:

    st.subheader("💊 Revenue by Product")

    product_revenue = (
        filtered_df
        .groupby("Product_Name")["Revenue"]
        .sum()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(
        product_revenue.index,
        product_revenue.values
    )

    ax.set_xlabel("Revenue (€)")
    ax.set_ylabel("")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ---------------- COUNTRY REVENUE ----------------

with col2:

    st.subheader("🌍 Revenue by Country")

    country_revenue = (
        filtered_df
        .groupby("Country")["Revenue"]
        .sum()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(
        country_revenue.index,
        country_revenue.values
    )

    ax.set_xlabel("Revenue (€)")
    ax.set_ylabel("")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# =========================================================
# ROW 2 — MONTHLY TREND
# =========================================================

st.subheader("📅 Monthly Revenue Trend")

monthly_sales = (
    filtered_df
    .groupby(["Year", "Month"])["Revenue"]
    .sum()
    .reset_index()
)

monthly_sales["Period"] = (
    monthly_sales["Year"].astype(str)
    + "-"
    + monthly_sales["Month"].astype(str).str.zfill(2)
)

fig, ax = plt.subplots(figsize=(14, 5))

ax.plot(
    monthly_sales["Period"],
    monthly_sales["Revenue"],
    marker="o",
    linewidth=2
)

ax.set_xlabel("Period")
ax.set_ylabel("Revenue (€)")

plt.xticks(rotation=45)

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)

# =========================================================
# ROW 3 — YEARLY REVENUE + PRODUCT MIX
# =========================================================

col1, col2 = st.columns(2)

# ---------------- YEARLY REVENUE ----------------

with col1:

    st.subheader("📈 Year-over-Year Revenue")

    yearly_revenue = (
        filtered_df
        .groupby("Year")["Revenue"]
        .sum()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.bar(
        yearly_revenue.index.astype(str),
        yearly_revenue.values
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Revenue (€)")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ---------------- PRODUCT MIX ----------------

with col2:

    st.subheader("🥧 Revenue Contribution by Product")

    product_mix = (
        filtered_df
        .groupby("Product_Name")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.pie(
        product_mix.values,
        labels=product_mix.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Revenue Share")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# =========================================================
# ROW 4 — PROFITABILITY
# =========================================================

col1, col2 = st.columns(2)

# ---------------- PRODUCT PROFIT ----------------

with col1:

    st.subheader("💰 Gross Profit by Product")

    product_profit = (
        filtered_df
        .groupby("Product_Name")["Gross_Profit"]
        .sum()
        .sort_values()
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(
        product_profit.index,
        product_profit.values
    )

    ax.set_xlabel("Gross Profit (€)")
    ax.set_ylabel("")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# ---------------- PROFIT MARGIN ----------------

with col2:

    st.subheader("📊 Product Profit Margin")

    margin = (
        filtered_df
        .groupby("Product_Name")
        .agg(
            Revenue=("Revenue", "sum"),
            Gross_Profit=("Gross_Profit", "sum")
        )
    )

    margin["Profit_Margin"] = (
        margin["Gross_Profit"]
        / margin["Revenue"]
        * 100
    )

    margin = margin["Profit_Margin"].sort_values()

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.barh(
        margin.index,
        margin.values
    )

    ax.set_xlabel("Profit Margin (%)")
    ax.set_ylabel("")

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


# =========================================================
# SALES REPRESENTATIVE PERFORMANCE
# =========================================================

st.divider()

st.subheader("🏆 Top Sales Representatives")

sales_rep = (
    filtered_df
    .groupby("Sales_Rep_Name")
    .agg(
        Revenue=("Revenue", "sum"),
        Units=("Units_Sold", "sum"),
        Transactions=("Transaction_ID", "nunique")
    )
    .sort_values(
        "Revenue",
        ascending=False
    )
    .head(10)
)

fig, ax = plt.subplots(figsize=(12, 5))

ax.barh(
    sales_rep.index[::-1],
    sales_rep["Revenue"].values[::-1]
)

ax.set_xlabel("Revenue (€)")
ax.set_ylabel("Sales Representative")

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)

st.dataframe(
    sales_rep,
    use_container_width=True
)


# =========================================================
# CUSTOMER SEGMENT PERFORMANCE
# =========================================================

st.subheader("🏥 Revenue by Customer Segment")

segment_revenue = (
    filtered_df
    .groupby("Customer_Segment")["Revenue"]
    .sum()
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 4))

ax.bar(
    segment_revenue.index,
    segment_revenue.values
)

ax.set_xlabel("Customer Segment")
ax.set_ylabel("Revenue (€)")

plt.tight_layout()

st.pyplot(fig)

plt.close(fig)


# =========================================================
# BUSINESS INSIGHTS
# =========================================================

st.divider()

st.subheader("💡 Key Business Insights")

st.markdown(
    """
    ### Product Performance

    - **GlycoCare** is one of the strongest revenue-generating products.
    - **Immunexa** recorded the strongest year-over-year growth.
    - **CardioMax** experienced the largest revenue decline.
    - **Dermacare** and **GastroRelief** showed positive growth.

    ### Market Performance

    - **Germany** is the strongest overall market.
    - **Belgium** is among the weaker-performing markets and requires attention.
    - Market performance varies considerably between countries.

    ### Overall Performance

    - Revenue increased from 2024 to 2025 by approximately **3.2%**.
    - Overall performance is positive, but revenue shows substantial monthly fluctuations.
    - Product-level performance is mixed, with some products growing while others decline.
    """
)

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "MediCore Pharma Analytics | Sales & Commercial Performance Analysis | 2024–2025"
)