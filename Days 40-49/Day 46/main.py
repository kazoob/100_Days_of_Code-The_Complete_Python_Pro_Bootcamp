import requests
from bs4 import BeautifulSoup
import re

BB_URL_BASE: str = "https://www.billboard.com/charts/hot-100"

date: str = ""

# Get date from user, verify format.
while not re.match('^[0-9]{4}-[0-9]{2}-[0-9]{2}$', date):
    date = input("Which year do you want to travel to? YYYY-MM-DD: ")

# Billboard website information.
bb_url = f"{BB_URL_BASE}/{date}"
bb_header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0"}

# Get Billboard website using requested date.
bb_response = requests.get(url=bb_url, headers=bb_header)
bb_soup = BeautifulSoup(markup=bb_response.text, features="html.parser")

# Get the track span elements.
tracks = bb_soup.select("li ul li h3")

# Get the track titles.
track_titles = [track.get_text().strip() for track in tracks]
print(track_titles)

