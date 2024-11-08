import requests
from bs4 import BeautifulSoup
import smtplib
import os

PRICE_THRESHOLD = 100

PRACTICE_URL = "https://appbrewery.github.io/instant_pot/"
LIVE_URL = "https://www.amazon.com/dp/B075CYMYK6"

# Get webpage.
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,en-CA;q=0.8",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Microsoft Edge\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
}

response = requests.get(url=PRACTICE_URL, headers=headers)
soup = BeautifulSoup(markup=response.text, features="html.parser")

# Get the price.
price = float(soup.find(name="span", class_="a-offscreen").get_text().split("$")[1])

print(f"${price}")

# Check the price against the threshold.
if price <= PRICE_THRESHOLD:
    # Get the title
    title = soup.find(id="productTitle").get_text().split("\r\n")[0].split(",")[0].strip()

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
