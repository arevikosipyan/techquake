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