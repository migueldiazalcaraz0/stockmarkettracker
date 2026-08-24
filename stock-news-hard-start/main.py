import json
import requests
import os
from newsapi import NewsApiClient
from dotenv import load_dotenv
load_dotenv()


### implemented news api
news_api = os.environ.get("NEWS_API")
stock_api = os.environ.get("STOCK_API")
## Wanted Paramters
params = {
    "q" : "Apple",
    "apiKey": news_api,
    "sortBy": "popularity",
    "from": "2026-08-19",

}

## APi response stuff
response = requests.get("https://newsapi.org/v2/everything", params=params)
news_data = response.json()

## only grab 3 articels
articles = news_data["articles"][:3]

# for entry in articles:
#     print(entry["title"])
#     print(entry["description"])
#     print()

### stock price paramters 

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "AAPL",
    "apikey" : stock_api,
    "outputsize" : "compact",

}

## Stock price api config
url = 'https://www.alphavantage.co/query'
r = requests.get(url,params=stock_params)
stock_data = r.json()

## Selecting todays closing data or latest closing data avaliable (doesnt fetch weekends)
time_series = stock_data["Time Series (Daily)"]
latest_data = list(time_series.keys())[0]
latest_close = time_series[latest_data]["4. close"]

## yesterday closing data or last yesterday thats a market day
yesterday_time_series = stock_data["Time Series (Daily)"]
yesterday_latest_data = list(yesterday_time_series.keys())[1]
yesterday_close = yesterday_time_series[yesterday_latest_data]["4. close"]
### prints date followed by price
# print(latest_data)
# print(latest_close)


### prints yesterdays date and closing price
# print(yesterday_latest_data)
# print(yesterday_close)

## Total change calcuation 
total = float(latest_close) - float(yesterday_close)


# print(f"Total net is {total}")

## check 5 percents value of yesterdays stock closing price
five_percent = float(yesterday_close) *0.05
# print(f"A change of five percent would be {five_percent}")

## function that gets news if the five percent of yesterdays closing price is less or greater then the total profit of todays price mines yesterdays so if its less.
def getnews():
    if abs(total) >= five_percent:
        print("get news")
    else:
        print("no news to print today")

    


getnews()



##Skipping twillio as only paid services allowed now not intrested in paying for api i wont use 

print("completed")