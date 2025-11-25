# stock_data/fetch_data.py

from datetime import datetime
import pandas as pd
import yfinance as yf


def fetch_stock_data(
    tickers: list,
    start_date: str = "1995-01-01",
    end_date: str = None,
) -> pd.DataFrame:
    
    """Fetch historical stock data for the given tickers from Yahoo Finance.

    Args:
        tickers (list): List of ticker symbols (for example, ["AAPL", "MSFT"]).
        start_date (str): Start date in 'YYYY-MM-DD' format. Defaults to '1995-01-01'.
        end_date (str): End date in 'YYYY-MM-DD' format. Defaults to today's date
            if not provided.

    Returns:
        pd.DataFrame: Historical price data for the requested tickers.
        If an error occurs, an empty DataFrame is returned.
    """
    # If the user does not specify the end date, use today's date
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")

    try:
        # Download historical price data from Yahoo Finance
        data = yf.download(
            tickers,
            start=start_date,
            end=end_date,
            progress=False, # Hide the progress bar in Jupyter notebooks
            auto_adjust=True, # Adjust prices for stock splits and dividends
        )

        # Remove any rows that have no data at all
        data = data.dropna(how="all").reset_index()

        # Inform the user if the request succeeded but returned no usable data
        if data.empty:
            print("No data returned for the given tickers and date range.")

        return data

    except Exception as error:
        # Print the error message for debugging, and return an empty DataFrame
        print(f"Error fetching data for {tickers}: {error}")
        return pd.DataFrame()