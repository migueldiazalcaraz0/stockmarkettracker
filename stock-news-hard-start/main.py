import json
import requests
import os
from newsapi import NewsApiClient
from dotenv import load_dotenv
load_dotenv()


### implemented news api
news_api = os.environ.get("NEWS_API")
stock_api = os.environ.get("STOCK_API")

params = {
    "q" : "Apple",
    "apiKey": news_api,
    "sortBy": "popularity",
    "from": "2026-08-19",

}

response = requests.get("https://newsapi.org/v2/everything", params=params)
news_data = response.json()

# print(news_data)

articles = news_data["articles"][:3]

# for entry in articles:
#     print(entry["title"])
#     print(entry["description"])
#     print()

### stock news 


stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "AAPL",
    "apikey" : stock_api,
    "outputsize" : "compact",

}


url = 'https://www.alphavantage.co/query'
r = requests.get(url,params=stock_params)
stock_data = r.json()

# print(stock_data)

time_series = stock_data["Time Series (Daily)"]
latest_data = list(time_series.keys())[0]
latest_close = time_series[latest_data]["4. close"]

yesterday_time_series = stock_data["Time Series (Daily)"]
yesterday_latest_data = list(yesterday_time_series.keys())[1]
yesterday_close = yesterday_time_series[yesterday_latest_data]["4. close"]

print(latest_data)
print(latest_close)
print(yesterday_latest_data)
print(yesterday_close)
total = float(latest_close) - float(yesterday_close)
print(total)

# STOCK = "TSLA"
# COMPANY_NAME = "Tesla Inc"

# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

