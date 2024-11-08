import requests
from bs4 import BeautifulSoup
import smtplib
import os

PRICE_THRESHOLD = 100

PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6"

# Get webpage.
response = requests.get(url=PRACTICE_URL)
soup = BeautifulSoup(markup=response.text, features="html.parser")

# Get the price.
price = float(soup.find(name="span", class_="a-offscreen").get_text().split("$")[1])

print(f"${price}")

# Check the price against the threshold.
if price <= PRICE_THRESHOLD:
    # Get the title
    title = soup.find(id="productTitle").get_text().split("\r\n")[0].strip()

    print(title)

    # Prepare the e-mail message
    message = (f"From: {os.environ["SMTP_FROM"]}\n"
               f"To: {os.environ["SMTP_FROM"]}\n"
               f"Subject: Amazon price alert!\n\n"
               f"{title} is now ${price}!\n{response.url}")

    # Send the e-mail
    with smtplib.SMTP(host=os.environ["SMTP_HOST"], port=int(os.environ["SMTP_PORT"])) as smtp:
        smtp.starttls()
        smtp.login(user=os.environ["SMTP_USERNAME"], password=os.environ["SMTP_PASSWORD"])
        smtp.sendmail(from_addr=os.environ["SMTP_FROM"], to_addrs=os.environ["SMTP_FROM"], msg=message)
