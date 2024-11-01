import os
import requests
from twilio.rest import Client

CACHED_JSON = False
STOCK: str = "TSLA"
COMPANY_NAME: str = "Tesla Inc"
STOCK_CHANGE_THRESHOLD = 0.5


def get_stock_change(stock_name: str) -> float:
    """Return the percentage change of the previous 2 trading days' closing price."""

    # Get live result from API.
    if not CACHED_JSON:
        # API parameters.
        stock_parameters: dict[str, str] = {
            "apikey": os.environ["ALPHAVANTAGE_API_KEY"],
            "function": "TIME_SERIES_DAILY",
            "symbol": stock_name,
            "outputsize": "compact",
            "datatype": "json"
        }

        # API request / response.
        stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
        stock_response.raise_for_status()

        # Get API response JSON.
        stock_json: dict = stock_response.json()

    # Use cached JSON response.
    else:
        stock_json: dict = {
            'Time Series (Daily)': {
                '2024-10-30': {'1. open': '258.0350', '2. high': '263.3500', '3. low': '255.8201',
                               '4. close': '257.5500', '5. volume': '53993576'},
                '2024-10-29': {'1. open': '264.5100', '2. high': '264.9800', '3. low': '255.5100',
                               '4. close': '259.5200', '5. volume': '80521751'},
                '2024-10-28': {'1. open': '1264.5100', '2. high': '1264.9800', '3. low': '1255.5100',
                               '4. close': '1259.5200', '5. volume': '180521751'}}}

    # Get the two most recent closing prices. If the API is rate limiting us, catch the resulting KeyError exception.
    try:
        # Get the two most recent days.
        stock_json_list = list(stock_json["Time Series (Daily)"].values())[0:2]

        # Get the closing prices.
        stock_prices = [float(price["4. close"]) for price in stock_json_list]
    except KeyError as e:
        print("API error: Probably rate limited")
    else:
        # Return the percentage change between the two prices.
        return get_change(stock_prices[0], stock_prices[1])

    return 0


def get_change(current, previous):
    """Return the percentage change between two numbers."""

    # No change.
    if current == previous:
        return 0
    # Calculate change between two numbers.
    try:
        return round(((current - previous) / previous) * 100.0, 2)
    # Catch division by zero.
    except ZeroDivisionError:
        return float('inf')


def get_news(company: str):
    """Return the 3 most recent news articles for the given company name."""

    # Get live result from API.
    if not CACHED_JSON:
        # API parameters.
        news_parameters: dict[str, str] = {
            "apikey": os.environ["NEWSAPI_API_KEY"],
            "qInTitle": company,
            "language": "en",
            "sortBy": "publishedAt",
            "pageSize": 3,
            "page": 1,
        }

        # API request / response.
        news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
        news_response.raise_for_status()

        # Get API response JSON.
        news_json = news_response.json()

    # Use cached JSON response.
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

    # Build new dictionary with the title, description and url fields only.
    articles = []
    for article in news_json["articles"]:
        news_item = {
            "title": article["title"],
            "description": article["description"],
            "url": article["url"],
        }
        articles.append(news_item)

    # Return new dictionary.
    return articles


def send_sms(stock, stock_change, news):
    """Send SMS message with stock symbol, change percentage from previous day and news article."""

    # Set up Twilio client.
    twilio_client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    # Determine if the stock change was no change, positive or negative.
    if stock_change == 0:
        stock_change_symbol = "🔸"
    elif stock_change > 0:
        stock_change_symbol = "🔺"
    else:
        stock_change_symbol = "🔻"

    # Prepare SMS body. Include stock symbol, change percentage, change symbol, news headline and news URL.
    twilio_body = (f"{stock}: {stock_change_symbol}{abs(stock_change)}%\n"
                   f"Headline: {news["title"]}\n"
                   f"URL: {news["url"]}")

    # Send SMS message.
    twilio_message = twilio_client.messages.create(
        body=twilio_body,
        from_=os.environ["TWILIO_FROM"],
        to=os.environ["TWILIO_TO"],
    )


# Get the price change percent for stock symbol.
stock_change_pct = get_stock_change(STOCK)

# Proceed if change is over the threshold.
if abs(stock_change_pct) >= STOCK_CHANGE_THRESHOLD:
    # Get the news articles for the company.
    news_articles = get_news(COMPANY_NAME)

    # Send an SMS message for each news article.
    # for article in news_articles:
    #     send_sms(STOCK, stock_change_pct, article)

    # Send an SMS message for the first news article only.
    send_sms(STOCK, stock_change_pct, news_articles[0])
