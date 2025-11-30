# app.py
#
# Simple Streamlit app for visualising drawdowns of a single tech stock
# using the same functions as in the techquake project.

import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

# Make sure the project root is on the Python path
ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# Import project functions
from test_stock_data.fetch_stock_data import fetch_stock_data
from test_stock_data.process_data import (
    extract_price_table,
    compute_daily_returns,
    compute_cumulative_returns,
    compute_drawdowns,
)

# ---------------- Page configuration ----------------
st.set_page_config(
    page_title="TechQuake – Drawdown Explorer",
    layout="wide",
)

st.title("📉 TechQuake – Drawdowns for a Single Tech Stock")

st.markdown(
    """
This mini app reuses the code from the **techquake** project to show
**drawdowns** (declines from previous peaks) for one selected stock.

Use the controls on the sidebar to:

- Pick a ticker (Apple, Microsoft, Nvidia, Amazon, or Spotify)  
- Choose a start and end date for the analysis  

The chart will show how far the stock trades below its previous peak
over the chosen period.
"""
)

# ---------------- Sidebar controls ----------------

st.sidebar.header("Settings")

# List of tickers used in the project
AVAILABLE_TICKERS = ["AAPL", "MSFT", "NVDA", "AMZN", "SPOT"]

# Let the user choose a single ticker
ticker = st.sidebar.selectbox(
    "Select a ticker",
    options=AVAILABLE_TICKERS,
    index=0,
)

# Let the user choose start and end dates
default_start = pd.to_datetime("2018-01-01")
default_end = pd.Timestamp.today().normalize()

start_date = st.sidebar.date_input("Start date", value=default_start)
end_date = st.sidebar.date_input("End date", value=default_end)

# Basic check that the date range makes sense
if start_date >= end_date:
    st.sidebar.error("Start date must be earlier than end date.")
    st.stop()

# ---------------- Fetch and process data ----------------

with st.spinner(f"Fetching price data for {ticker} from Yahoo Finance..."):
    raw_data = fetch_stock_data(
        tickers=[ticker],  # function expects a list
        start_date=start_date.strftime("%Y-%m-%d"),
        end_date=end_date.strftime("%Y-%m-%d"),
    )

# If nothing came back, stop here
if raw_data.empty:
    st.error("No data was returned for this ticker and date range.")
    st.stop()

# Work with closing prices only
prices = extract_price_table(raw_data, price_field="Close")

# In case there are gaps at the start (e.g. before SPOT IPO), drop all-NaN rows
prices = prices.dropna(how="all")

# Compute daily returns, cumulative index, and drawdowns
daily_returns = compute_daily_returns(prices)
cumulative = compute_cumulative_returns(daily_returns, base=100.0)
drawdowns = compute_drawdowns(cumulative)

# ---------------- Plot drawdowns ----------------

st.subheader(f"Drawdowns for {ticker}")

fig, ax = plt.subplots(figsize=(12, 6))

# drawdowns is a DataFrame; we select the single ticker column
drawdowns[ticker].plot(ax=ax)

ax.set_title(f"Drawdowns Over Time – {ticker}", fontsize=12)
ax.set_xlabel("Date")
ax.set_ylabel("Drawdown (fraction below peak)")
ax.grid(True)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

st.pyplot(fig)

st.markdown(
    """
**How to read this chart**

- A value of **0** means the stock is at or near a new peak.  
- A value of **-0.30** means it is **30% below** its previous peak.  
- Deeper and longer drawdowns indicate periods where the stock was
  more vulnerable during market stress.
"""
)