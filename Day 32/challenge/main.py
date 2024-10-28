import json
import smtplib
from datetime import datetime
import random

SMTP_PII_FILE_NAME = "../../smtp_pii.json"
QUOTES_FILE_NAME = "quotes.txt"

WEEKDAY_TRIGGER = 0  # 0 = Monday

day_of_week = datetime.now().weekday()

if day_of_week == WEEKDAY_TRIGGER:
    to_address = ""
    while not to_address:
        to_address = input("Enter the recipient's e-mail address: ")

    with open(SMTP_PII_FILE_NAME) as smtp_pii_file:
        smtp_pii = json.load(smtp_pii_file)

    smtp_username = smtp_pii['username']
    smtp_password = smtp_pii['password']
    smtp_from = smtp_pii['from']
    smtp_host = smtp_pii['host']
    smtp_port = smtp_pii['port']

    with open(QUOTES_FILE_NAME) as quotes_file:
        quotes = quotes_file.readlines()

    quote = random.choice(quotes)

    message = f"From: {smtp_from}\nTo: {to_address}\nSubject: Motivational Quote\n\n{quote}"

    with smtplib.SMTP(host=smtp_host, port=smtp_port) as smtp:
        smtp.starttls()
        smtp.login(user=smtp_username, password=smtp_password)
        smtp.sendmail(from_addr=smtp_from, to_addrs=to_address, msg=message)
