from django.shortcuts import render
from .models import Stock
from django.http import JsonResponse
import yfinance as yf

def get_stock_data(request):
    ticker = yf.Ticker("TATASTEEL.NS")
    data = ticker.history(period="1d", interval="1m")

    if not data.empty:
        latest = data.tail(1).iloc[0]
        response = {
            "price": round(latest["Close"], 2),
            "time": latest.name.strftime("%H:%M:%S")
        }
    else:
        response = {
            "error": "No data available"
        }

    return JsonResponse(response)

def get_candles(request, symbol):
    try:
        print(f"[DEBUG] Fetching data for: {symbol}")  # Optional debug
        ticker = yf.Ticker(symbol)
        df = ticker.history(period="1d", interval="1m").tail(30)

        data = {
            "timestamps": [ts.strftime('%Y-%m-%d %H:%M:%S') for ts in df.index],
            "open": df["Open"].tolist(),
            "high": df["High"].tolist(),
            "low": df["Low"].tolist(),
            "close": df["Close"].tolist(),
        }
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

def dashboard(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/dashboard.html', {'stocks': stocks})
