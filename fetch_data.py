import requests
import os
import sys


api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
if not api_key:
    print("Error: Please set ALPHA_VANTAGE_API_KEY in your environment variables.")
    sys.exit(1)


def fetch_stock_data(api_key, symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": api_key,
        "outputsize": "compact"
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        return None
              
    data = response.json()
    if "Time Series (Daily)" not in data:
        print("Wrong Request. Check params or symbol.")
        return None

    return data


def parse_stock_data(data, symbol):
    time_series = data.get("Time Series (Daily)", {})

    print(f"Stock Data for {symbol} (Daily)")
    print("-" * 60)

    for date, values in list(time_series.items())[:5]:
        open_prices = values.get("1. open", "N/A")
        high_prices = values.get("2. high", "N/A")
        low_prices = values.get("3. low", "N/A")
        close_prices = values.get("4. close", "N/A")

        print(f"{date} | {open_prices} | {high_prices} | {low_prices} | {close_prices}")


if __name__ == "__main__":
    symbol = input("Enter stock ticker symbol (e.g., AAPL, TSLA): ").strip().upper()
    data = fetch_stock_data(api_key, symbol)

    if data:
        parse_stock_data(data, symbol)