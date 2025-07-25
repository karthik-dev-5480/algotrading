# stocks/utils.py
import yfinance as yf
import datetime

def fetch_stock_data(symbol, period="7d", interval="1d"):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period, interval=interval)
    return data.reset_index().to_dict(orient='records')