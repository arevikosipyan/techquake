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

def compute_daily_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily percentage returns for each ticker.

    Args:
        prices (pd.DataFrame): Price table with Date index and tickers as columns.

    Returns:
        pd.DataFrame: Daily returns for each ticker as decimal values (for example, 0.01 means +1%).
    """
    # pct_change gives (P_t / P_{t-1}) - 1 for each day
    returns = prices.pct_change()
    
    # Drop the first row, which contains NaN values
    returns = returns.dropna(how="all")

    return returns

def compute_cumulative_returns(
    returns: pd.DataFrame,
    base: float = 100.0,
) -> pd.DataFrame:
    
    """
    Compute cumulative returns indexed to a starting value (for example, 100).

    Args:
        returns (pd.DataFrame): Daily returns for each ticker (for example, from compute_daily_returns).
        base (float): Starting index level for the cumulative return.

    Returns:
        pd.DataFrame: Cumulative return index for each ticker.
            Each column shows how an initial investment of `base` would grow over time.
    """
    
    # (1 + r).cumprod() gives the growth factor over time
    growth_factors = (1 + returns).cumprod()
    
    # Scale to the chosen base (for example, start at 100)
    cumulative = base * growth_factors
    
    return cumulative

def compute_rolling_volatility(
    returns: pd.DataFrame,
    window: int = 21,
    trading_days_per_year: int = 252,
) -> pd.DataFrame:
    """
    Compute annualized rolling volatility using daily returns.

    Args:
        returns (pd.DataFrame): Daily returns for each ticker.
        window (int): Rolling window size in days (21 ≈ one trading month).
        trading_days_per_year (int): Number of trading days per year, used to annualize the volatility.

    Returns:
        pd.DataFrame: Annualized rolling volatility for each ticker.
    """
    # Rolling standard deviation of daily returns over the chosen window
    rolling_std = returns.rolling(window=window).std()
    
    # Annualize the volatility: multiply by sqrt(number of trading days per year)
    annualized_vol = rolling_std * np.sqrt(trading_days_per_year)
    
    return annualized_vol

def compute_drawdowns(cumulative_returns: pd.DataFrame) -> pd.DataFrame:
    """
    Compute drawdowns as percentage decline from the running maximum.

    Args:
        cumulative_returns (pd.DataFrame): Cumulative return index for each ticker.

    Returns:
        pd.DataFrame: Drawdowns for each ticker.
        Values are 0 at peaks and negative during declines
        (for example, -0.3 means the stock is 30% below its peak).
    """
    # Running maximum of the cumulative return index
    running_max = cumulative_returns.cummax()

    # Drawdown is the percentage drop from the running maximum
    drawdowns = (cumulative_returns - running_max) / running_max

    return drawdowns