import requests
import random

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CUSTOM_PERCENTAGE = 5

AV_API_KEY = "1PM8KCEQ11T9WIBR"
AV_API_ENDPOINT = "https://www.alphavantage.co/query"


#------------------------------STOCK PRICE API-----------------------------#
av_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": AV_API_KEY,
}
av_response = requests.get(AV_API_ENDPOINT, params=av_parameters)
av_response.raise_for_status()
av_data= av_response.json()["Time Series (Daily)"]
close_prices = []
for time in list(av_data.keys())[:2]:
    close_prices.append(float(av_data[time]["4. close"]))

diff_percentage = (abs(close_prices[1]-close_prices[0]) / close_prices[0]) * 100

