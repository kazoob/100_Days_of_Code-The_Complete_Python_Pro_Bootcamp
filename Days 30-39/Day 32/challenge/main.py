import smtplib
from datetime import datetime
import random
import os

QUOTES_FILE_NAME = "quotes.txt"

WEEKDAY_TRIGGER = 2  # 2 = Wednesday

day_of_week = datetime.now().weekday()

if day_of_week == WEEKDAY_TRIGGER:
    to_address = ""
    while not to_address:
        to_address = input("Enter the recipient's e-mail address: ")

    with open(QUOTES_FILE_NAME) as quotes_file:
        quotes = quotes_file.readlines()

    quote = random.choice(quotes)

    message = f"From: {os.environ["SMTP_FROM"]}\nTo: {to_address}\nSubject: Motivational Quote\n\n{quote}"

    with smtplib.SMTP(host=os.environ["SMTP_HOST"], port=int(os.environ["SMTP_PORT"])) as smtp:
        smtp.starttls()
        smtp.login(user=os.environ["SMTP_USERNAME"], password=os.environ["SMTP_PASSWORD"])
        smtp.sendmail(from_addr=os.environ["SMTP_FROM"], to_addrs=to_address, msg=message)
