import os
import requests
from twilio.rest import Client

STOCK: str = "TSLA"
COMPANY_NAME: str = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_change(stock_name: str) -> float:
    # stock_parameters: dict[str, str] = {
    #     "apikey": os.environ["ALPHAVANTAGE_API_KEY"],
    #     "function": "TIME_SERIES_DAILY",
    #     "symbol": stock_name,
    #     "outputsize": "compact",
    #     "datatype": "json"
    # }
    #
    # stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
    # stock_response.raise_for_status()
    # stock_json: dict = stock_response.json()
    stock_json: dict = {
        'Time Series (Daily)': {
            '2024-10-30': {'1. open': '258.0350', '2. high': '263.3500', '3. low': '255.8201', '4. close': '257.5500',
                           '5. volume': '53993576'},
            '2024-10-29': {'1. open': '264.5100', '2. high': '264.9800', '3. low': '255.5100', '4. close': '259.5200',
                           '5. volume': '80521751'}}}

    stock_prices: list = []

    try:
        stock_json_key_list = list(stock_json["Time Series (Daily)"])

        for i in range(0, 2):
            key = stock_json_key_list[i]
            value = stock_json["Time Series (Daily)"].get(key)["4. close"]
            stock_prices.append(float(value))
    except KeyError as e:
        print("Probably rate limited")
    else:
        return get_change(stock_prices[0], stock_prices[1])

    return 0


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return round((abs(current - previous) / previous) * 100.0, 2)
    except ZeroDivisionError:
        return float('inf')


print(f"{get_stock_change(STOCK)}%")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
