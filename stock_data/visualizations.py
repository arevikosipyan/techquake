# stock_data/visualizations.py

import matplotlib.pyplot as plt
import pandas as pd

def plot_cumulative_returns(cumulative_returns: pd.DataFrame, figsize=(12, 6)):
    """
    Plot cumulative returns for each stock.
    
    Args:
        cumulative_returns (pd.DataFrame): Cumulative returns data for each ticker.
        figsize (tuple): The size of the figure for the plot (default is (12, 6)).
        
    Returns:
        None 
    """
    
    # Plot cumulative returns for all selected stocks
    cumulative_returns.plot(figsize=figsize, title="Cumulative Returns (Indexed to 100)")
    
    # Set labels for the x and y axes
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns")
    
    # Display grid for better readability
    plt.grid(True)
    
    # Rotate x-axis for better legibility
    plt.xticks(rotation=45, ha='right')
    
    # Adjust layout to avoid overlapping labels
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
def plot_volatility_with_events(rolling_volatility: pd.DataFrame, event_dates: dict, figsize=(12, 6)):
    """
    Plot 21-day rolling volatility with major historical events marked.
    
    Args:
        rolling_volatility (pd.DataFrame): Rolling volatility data for each ticker.
        event_dates (dict): Dictionary of event dates with event names as keys.
        figsize (tuple): The size of the figure for the plot (default is (12, 6)).
    
    Returns:
        None
    """
    # Plot the rolling volatility for all selected stocks
    rolling_volatility.plot(figsize=figsize, title="21-Day Rolling Volatility with Major Events")
    
    # Set labels for x and y axes
    plt.xlabel("Date")
    plt.ylabel("Volatility")
    
    # Mark historical events on the plot with vertical red dashed lines
    for event_name, event_date in event_dates.items():
        plt.axvline(x=event_date, color='r', linestyle='--', label=event_name)
    
    # Place the legend outside the plot to avoid cluttering
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    
    # Display grid for better readability
    plt.grid(True)
    
    # Rotate x-axis labels for better legibility
    plt.xticks(rotation=45, ha='right')
    
    # Adjust layout to avoid overlapping labels
    plt.tight_layout()
    
    # Show the plot
    plt.show()