import requests
import random

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
CUSTOM_PERCENTAGE = 5

AV_API_KEY = "1PM8KCEQ11T9WIBR"
AV_API_ENDPOINT = "https://www.alphavantage.co/query"

NEWS_API_KEY = "4cea9b09d6324f57912ebb7e630b92d6"
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"


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

#-----------------------------STOCK NEWS API----------------------------------#

if diff_percentage > CUSTOM_PERCENTAGE:
    news_parameters = {
        "q": COMPANY_NAME,
        "apikey": "4cea9b09d6324f57912ebb7e630b92d6",
    }
    news_response = requests.get(NEWS_API_ENDPOINT, params=news_parameters)
    news_response.raise_for_status()
    last_three_articles = news_response.json()["articles"][:3]
    random_number = random.randint(0, 2)
    title = last_three_articles[random_number]["title"]
    description = last_three_articles[random_number]["description"]
