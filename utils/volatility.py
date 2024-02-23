from yahoo_fin import options, stock_info
from scipy.stats import norm
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import requests

def get_sp500():
    sp500_url = 'https://raw.githubusercontent.com/datasets/s-and-p-500-companies/master/data/constituents.csv'
    response = requests.get(sp500_url)
    data = response.text.split('\n')
    symbols = [line.split(',')[0] for line in data[1:-1]]  # Ignore header and empty last line
    return symbols

def get_volatility(symbol):
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=14)
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    stock_data['Return'] = stock_data['Adj Close'].pct_change()
    volatility = np.std(stock_data['Return'])

    return volatility

def get_sp500_highest_volatility(amount):
    sp500_symbols = get_sp500()
    volatilities = []
    for symbol in sp500_symbols:
        volatility = get_volatility(symbol)
        volatilities.append((symbol, volatility))

    volatilities.sort(key=lambda x: x[1])

    return volatilities[:amount]

