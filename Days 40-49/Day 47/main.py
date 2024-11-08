import requests
from bs4 import BeautifulSoup

PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6"

response = requests.get(url=PRACTICE_URL)
soup = BeautifulSoup(markup=response.text, features="html.parser")

price_element = soup.find(name="span", class_="a-offscreen").get_text()
price = float(price_element.split("$")[1])

print(price)
