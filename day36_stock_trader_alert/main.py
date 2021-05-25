import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NewsAPI = "https://newsapi.org/"
NewsAPIkey = ""
AlphaVantageAPIKEY = ""

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": AlphaVantageAPIKEY
}
response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
data = response.json()["Time Series (Daily)"]
last_2_days = [(closing_date, val["5. adjusted close"]) for (closing_date, val) in data.items()][:2]
# last_2_days = [(closing_date, data[closing_date]["5. adjusted close"]) for (closing_date, val) in data.items()][:2]
print(last_2_days, last_2_days[0][1], last_2_days[1][1], abs(float(last_2_days[0][1]) - float(last_2_days[1][1])))
day1 = round(float(last_2_days[0][1]))

#2. - Get the day before yesterday's closing stock price
day2 = round(float(last_2_days[1][1]))
#3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
dif = abs(day1 - day2)
#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
pct_dif = round(100 * ((day1 - day2) / day2), 0)
print('day1',day1,' day2',day2,' dif',dif,' pct_dif',pct_dif)
#5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(pct_dif) > 0:
    NEWS_PARAMS = {
        "apiKey": NewsAPIkey,
        "qInTitle": COMPANY_NAME,

    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    articles = news_response.json()["articles"][:3]
    print(articles)
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
news_list = [f"Headline: {article['title']}, \nBrief: {article['description']}" for article in articles]
print('news_list',news_list)
#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

