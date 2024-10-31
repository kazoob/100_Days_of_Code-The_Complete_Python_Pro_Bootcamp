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
        return round(((current - previous) / previous) * 100.0, 2)
    except ZeroDivisionError:
        return float('inf')


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company: str):
    # news_parameters: dict[str, str] = {
    #     "apikey": os.environ["NEWSAPI_API_KEY"],
    #     "q": company,
    #     "language": "en",
    #     "sortBy": "publishedAt",
    #     "pageSize": 3,
    #     "page": 1,
    # }
    #
    # news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    # news_response.raise_for_status()
    # news_json = news_response.json()
    news_json = {
        "status": "ok",
        "totalResults": 805,
        "articles": [
            {
                "source": {
                    "id": None,
                    "name": "Motley Fool Australia"
                },
                "author": "Sebastian Bowen",
                "title": "7 hugely popular ASX ETFs smashing new record highs on Wednesday",
                "description": "Do you own any of these lucky ASX ETFs?\nThe post 7 hugely popular ASX ETFs smashing new record highs on Wednesday appeared first on The Motley Fool Australia.",
                "url": "https://www.fool.com.au/2024/10/30/7-hugely-popular-asx-etfs-smashing-new-record-highs-on-wednesday/",
                "urlToImage": "https://www.fool.com.au/wp-content/uploads/2022/02/gold-1200x675.jpg",
                "publishedAt": "2024-10-30T02:10:40Z",
                "content": "It's been a fairly miserable middle-of-the-week session for ASX shares so far this Wednesday. At the time of writing, the S&amp;P/ASX 200 Index (ASX: XJO) has lost 0.37% of its value and is down to a… [+4216 chars]"
            },
            {
                "source": {
                    "id": None,
                    "name": "Investing.com"
                },
                "author": "Investing.com",
                "title": "Cathie Wood's ARK sells Tesla, buys more Archer Aviation stock",
                "description": "Cathie Wood's ARK sells Tesla, buys more Archer Aviation stock",
                "url": "https://www.investing.com/news/company-news/cathie-woods-ark-sells-tesla-buys-more-archer-aviation-stock-93CH-3689803",
                "urlToImage": "https://i-invdn-com.investing.com/redesign/images/seo/investing_300X300.png",
                "publishedAt": "2024-10-30T00:01:52Z",
                "content": "Cathie Wood's ARK ETFs have made their daily trades for Tuesday, October 29th, 2024, with significant activity across a range of innovative companies. In a notable move, ARK sold 13,896 shares of Tes… [+2335 chars]"
            },
            {
                "source": {
                    "id": None,
                    "name": "Motley Fool Australia"
                },
                "author": "Mitchell Lawler",
                "title": "3 ASX shares you probably didn't know are founder-led and why it matters",
                "description": "'Founder mode'. It's more than a meme, it's a management style. One that might be worth investing in. \nThe post 3 ASX shares you probably didn't know are founder-led and why it matters appeared first on The Motley Fool Australia.",
                "url": "https://www.fool.com.au/2024/10/30/3-asx-shares-you-probably-didnt-know-are-founder-led-and-why-it-matters/",
                "urlToImage": "https://www.fool.com.au/wp-content/uploads/2021/09/New-boss-in-town-16_9-1200x675.jpg",
                "publishedAt": "2024-10-29T23:31:09Z",
                "content": "It's important who calls the shots at the companies you're invested in. A corporation is merely a legal structure. It alone holds no worth. The accumulation of skill and intellect of the people withi… [+4027 chars]"
            }
        ]
    }

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
print(get_news(COMPANY_NAME))

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
