import yfinance as yf
import pandas as pd
from datetime import datetime

def calculate_cumulative_returns():
    allocations = {
        'BTC-USD': 0.25,
        'ETH-USD': 0.25,
        'LDO-USD': 0.075,
        'MATIC-USD': 0.075,
        'ARB11841-USD': 0.075,
        'LINK-USD': 0.075,
        'SOL-USD': 0.04,
        'OP-USD': 0.04,
        'STX4847-USD': 0.04,
        'DYDX-USD': 0.04,
        'PRIME23711-USD': 0.04,
    }

    dfs = {}  # Dictionary to store data for each asset

    # Iterate through the keys in allocations
    for asset_symbol in allocations.keys():
        # Download data for the current asset
        data = yf.download(asset_symbol, start='2023-08-24', 
                           interval='15m')['Adj Close']

        # Store the data in the dictionary
        dfs[asset_symbol] = data

    # Combine the data from the dictionary into a DataFrame
    df = pd.concat(dfs, axis=1)

    # Calculate daily percentage changes
    df = df.pct_change()

    # Calculate cumulative returns on each column
    df = (df + 1).cumprod() - 1

    # Multiply each column by its respective weight
    for asset_symbol, weight in allocations.items():
        df[asset_symbol] = (df[asset_symbol] * weight) * 100

    df['Total'] = df.sum(axis=1)
    df.to_csv('dadosgerais.csv')
    return df


def assets_prices():
    allocations = {
        'BTC-USD': 0.25,
        'ETH-USD': 0.25,
        'LDO-USD': 0.075,
        'MATIC-USD': 0.075,
        'ARB11841-USD': 0.075,
        'LINK-USD': 0.075,
        'SOL-USD': 0.04,
        'OP-USD': 0.04,
        'STX4847-USD': 0.04,
        'DYDX-USD': 0.04,
        'PRIME23711-USD': 0.04,
    }

    dfs = {}  # Dictionary to store data for each asset

    # Iterate through the keys in allocations
    for asset_symbol in allocations.keys():
        # Download data for the current asset
        data = yf.download(asset_symbol, start='2023-08-24', 
                           interval='15m')['Adj Close']

        # Store the data in the dictionary
        dfs[asset_symbol] = data

    # Combine the data from the dictionary into a DataFrame
    df = pd.concat(dfs, axis=1)
    df.to_csv('prices.csv')
    return df
