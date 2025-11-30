# stock_data/visualizations.py

import matplotlib.pyplot as plt
import pandas as pd


def plot_cumulative_returns(
    cumulative_returns: pd.DataFrame,
    figsize: tuple = (12, 6),
) -> None:
    """
    Plot cumulative returns for each stock.

    Args:
        cumulative_returns (pd.DataFrame): Cumulative returns data for each ticker.
        figsize (tuple): The size of the figure for the plot (default is (12, 6)).

    Returns:
        None
    """
    # Plot cumulative returns for all selected stocks
    ax = cumulative_returns.plot(
        figsize=figsize,
        title="Cumulative Returns (Indexed to 100)",
    )

    # Set labels for the x and y axes
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Returns")

    # Display grid for better readability
    ax.grid(True)

    # Rotate x-axis for better legibility
    plt.xticks(rotation=45, ha="right")

    # Adjust layout to avoid overlapping labels
    plt.tight_layout()

    # Show the plot
    plt.show()


def plot_stock_comparison(
    cumulative_returns: pd.DataFrame,
    tickers: list,
    figsize: tuple = (12, 6),
) -> None:
    """
    Plot cumulative returns for a selected subset of stocks.

    Args:
        cumulative_returns (pd.DataFrame): Cumulative return index for each ticker.
        tickers (list): List of ticker symbols to include in the plot.
        figsize (tuple): Size of the figure for the plot (default is (12, 6)).

    Returns:
        None
    """
    # Plot cumulative returns for the selected tickers
    ax = cumulative_returns[tickers].plot(
        figsize=figsize,
        title="Stock Performance Comparison",
    )

    # Set labels for x and y axes
    ax.set_xlabel("Date")
    ax.set_ylabel("Cumulative Returns")

    # Display grid for better readability
    ax.grid(True)

    # Rotate x-axis labels for better legibility
    plt.xticks(rotation=45, ha="right")

    # Adjust layout to avoid overlapping labels
    plt.tight_layout()

    # Show the plot
    plt.show()


def plot_volatility_with_events(
    rolling_volatility: pd.DataFrame,
    event_dates: dict,
    figsize: tuple = (12, 6),
) -> None:
    """
    Plot 21-day rolling volatility with major historical events marked.

    Args:
        rolling_volatility (pd.DataFrame): Rolling volatility data for each ticker.
        event_dates (dict): Dictionary of event dates with event names as keys.
            The values should be strings in 'YYYY-MM-DD' format.
        figsize (tuple): Size of the figure for the plot (default is (12, 6)).

    Returns:
        None
    """
    # If there is no volatility data, there is nothing to plot
    if rolling_volatility.empty:
        print("No rolling volatility data to plot.")
        return

    # Work on a copy and make sure the index is a DateTimeIndex
    data = rolling_volatility.copy()
    data.index = pd.to_datetime(data.index)

    # Determine the visible date range of the data
    start_date = data.index.min()
    end_date = data.index.max()

    # Plot the rolling volatility for all selected stocks
    ax = data.plot(
        figsize=figsize,
        title="21-Day Rolling Volatility with Major Events",
    )

    # Set labels for x and y axes
    ax.set_xlabel("Date")
    ax.set_ylabel("Annualised Volatility")

    # Mark only those events that fall inside the data range
    for event_name, event_date in event_dates.items():
        event_dt = pd.to_datetime(event_date)
        if start_date <= event_dt <= end_date:
            ax.axvline(
                x=event_dt,
                color="red",
                linestyle="--",
                linewidth=1.0,
                label=event_name,
            )

    # Place the legend outside the plot area to avoid clutter
    ax.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0))

    # Display grid for better readability
    ax.grid(True)

    # Rotate x-axis labels for better legibility
    plt.xticks(rotation=45, ha="right")

    # Adjust layout to avoid overlapping labels
    plt.tight_layout()

    # Show the plot
    plt.show()