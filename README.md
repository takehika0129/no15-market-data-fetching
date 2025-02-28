# Simple Market Data Fetching Script
A Python script to fetch stock market data using the **Alpha Vantage API**. This script retrieves daily stock prices (Open, High, Low, Close) and displays the latest 5 days of data.


## Set up Your API Key
What is Alpha Vantage?:
- [Alpha Vantage](https://www.alphavantage.co/) is a **financial market data provider** offering free-tier API.


## Usage
Set your Alpha Vantage API key as an environment variable:
```sh
export "ALPHA_VANTAGE_API_KEY=your_api_key_here"
```

Run the script and input a stock symbol:
```sh
fetch_data.py
```


## Concept
[Visit (takehika0129.github.io)](https://takehika0129.github.io/takehika-github-pages/reviews/prototype15.html)


## Requirements
- Python 3.x
- `requests`

Install dependencies using:
```sh
pip install -r requirements.txt
```

## License
You are free to use this code for personal and educational purposes. Commercial use and redistribution are not allowed.