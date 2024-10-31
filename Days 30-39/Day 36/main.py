import os
import requests
from twilio.rest import Client

CACHED_JSON = True
STOCK: str = "TSLA"
COMPANY_NAME: str = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def get_stock_change(stock_name: str) -> float:
    if not CACHED_JSON:
        stock_parameters: dict[str, str] = {
            "apikey": os.environ["ALPHAVANTAGE_API_KEY"],
            "function": "TIME_SERIES_DAILY",
            "symbol": stock_name,
            "outputsize": "compact",
            "datatype": "json"
        }

        stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
        stock_response.raise_for_status()
        stock_json: dict = stock_response.json()
    else:
        stock_json: dict = {
            'Time Series (Daily)': {
                '2024-10-30': {'1. open': '258.0350', '2. high': '263.3500', '3. low': '255.8201',
                               '4. close': '257.5500', '5. volume': '53993576'},
                '2024-10-29': {'1. open': '264.5100', '2. high': '264.9800', '3. low': '255.5100',
                               '4. close': '259.5200', '5. volume': '80521751'},
                '2024-10-28': {'1. open': '1264.5100', '2. high': '1264.9800', '3. low': '1255.5100',
                               '4. close': '1259.5200', '5. volume': '180521751'}}}

    try:
        stock_json_list = list(stock_json["Time Series (Daily)"].values())[0:2]
        stock_prices = [float(price["4. close"]) for price in stock_json_list]
    except KeyError as e:
        print("API error: Probably rate limited")
    else:
        return get_change(stock_prices[0], stock_prices[1])

    return 0


def get_change(current, previous):
    if current == previous:
        return 0
    try:
        return round(((current - previous) / previous) * 100.0, 2)
    except ZeroDivisionError:
        return float('inf')


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company: str):
    if not CACHED_JSON:
        news_parameters: dict[str, str] = {
            "apikey": os.environ["NEWSAPI_API_KEY"],
            "qInTitle": company,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "page": 1,
        }

        news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
        news_response.raise_for_status()
        news_json = news_response.json()
    else:
        news_json = {'status': 'ok', 'totalResults': 132, 'articles': [
            {'source': {'id': None, 'name': 'ETF Daily News'}, 'author': 'MarketBeat News',
             'title': 'Tesla, Inc. (NASDAQ:TSLA) Holdings Cut by Old Port Advisors',
             'description': 'Old Port Advisors reduced its stake in shares of Tesla, Inc. (NASDAQ:TSLA – Free Report) by 29.8% during the 3rd quarter, HoldingsChannel reports. The fund owned 836 shares of the electric vehicle producer’s stock after selling 355 shares during the period. O…',
             'url': 'https://www.etfdailynews.com/2024/10/30/tesla-inc-nasdaqtsla-holdings-cut-by-old-port-advisors/',
             'urlToImage': 'https://www.americanbankingnews.com/wp-content/timthumb/timthumb.php?src=https://www.marketbeat.com/logos/tesla-inc-logo-1200x675.png?v=20221020135629&w=240&h=240&zc=2',
             'publishedAt': '2024-10-30T11:59:25Z',
             'content': 'Old Port Advisors reduced its stake in shares of Tesla, Inc. (NASDAQ:TSLA – Free Report) by 29.8% during the 3rd quarter, HoldingsChannel reports. The fund owned 836 shares of the electric vehicle pr… [+6762 chars]'},
            {'source': {'id': None, 'name': 'Biztoc.com'}, 'author': 'marketbeat.com',
             'title': 'Tesla, Inc. (NASDAQ:TSLA) Shares Sold by Vanguard Capital Wealth Advisors',
             'description': 'Vanguard Capital Wealth Advisors decreased its holdings in Tesla, Inc. (NASDAQ:TSLA - Free Report) by 79.0% in the 3rd quarter, according to the company in its most recent Form 13F filing with the Securities & Exchange Commission. The institutional investor o…',
             'url': 'https://biztoc.com/x/08da6e6de65377a4', 'urlToImage': 'https://biztoc.com/cdn/806/og.png',
             'publishedAt': '2024-10-30T11:24:43Z',
             'content': 'Vanguard Capital Wealth Advisors decreased its holdings in Tesla, Inc. (NASDAQ:TSLA - Free Report) by 79.0% in the 3rd quarter, according to the company in its most recent Form 13F filing with the Se… [+148 chars]'},
            {'source': {'id': None, 'name': 'Biztoc.com'}, 'author': 'marketbeat.com',
             'title': 'Tesla, Inc. (NASDAQ:TSLA) Receives Consensus Recommendation of "Hold" from Analysts',
             'description': 'Shares of Tesla, Inc. (NASDAQ:TSLA - Get Free Report) have received an average recommendation of "Hold" from the thirty-eight analysts that are currently covering the stock, Marketbeat reports. Eight equities research analysts have rated the stock with a sell…',
             'url': 'https://biztoc.com/x/666ac5ccf73084a8', 'urlToImage': 'https://biztoc.com/cdn/806/og.png',
             'publishedAt': '2024-10-30T09:04:06Z',
             'content': 'Shares of Tesla, Inc. (NASDAQ:TSLA - Get Free Report) have received an average recommendation of "Hold" from the thirty-eight analysts that are currently covering the stock, Marketbeat reports. Eight… [+141 chars]'}]}

    news_articles = []
    for article in news_json["articles"]:
        news = {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
        }
        news_articles.append(news)

    return news_articles


print(f"{get_stock_change(STOCK)}%")
for news in get_news(COMPANY_NAME):
    print(news)

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
