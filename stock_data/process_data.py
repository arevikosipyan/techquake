# stock_data/process_data.py

import pandas as pd
import numpy as np


def extract_price_table(
    raw_data: pd.DataFrame,
    price_field: str = "Close",
) -> pd.DataFrame:
    
    """
    Extract a clean price table (Date index, tickers as columns)
    from the raw data returned by fetch_data.py.

    This function takes a DataFrame from fetch_data.py and selects
    a single price type (for example, "Close", "Adj Close") for all tickers.

    Args:
        raw_data (pd.DataFrame): DataFrame returned by fetch_data.py.
        price_field (str): Which price column to extract
            (for example, "Close", "Adj Close", "Open", "High", "Low").

    Returns:
        pd.DataFrame: Clean table with Date as index and one column per ticker.
    """
    
    # Work on a copy to avoid modifying the original data in the notebook
    data = raw_data.copy()
    
    # If "Date" is a column, make it the index
    if "Date" in data.columns:
        data = data.set_index("Date")
    
    # When downloading multiple tickers, yfinance creates a MultiIndex
    # Example: ("Close", "AAPL"), ("Close", "MSFT"), etc.
    if isinstance(data.columns, pd.MultiIndex):
        # Ensure the requested price_field exists
        if price_field not in data.columns.get_level_values(0):
            raise ValueError(f"'{price_field}' not found in raw data columns.")
        # Select the requested price field (for example, "Close" for all tickers)
        prices = data[price_field]
    else:
        # Single-ticker case: columns are already simple price columns
        prices = data
    
    # Sort rows by date and drop rows with all missing values
    prices = prices.sort_index().dropna(how="all")
    
    return prices