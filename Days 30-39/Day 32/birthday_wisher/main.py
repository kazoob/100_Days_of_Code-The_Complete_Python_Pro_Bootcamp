import smtplib
from datetime import datetime
import random
import pandas
import os

# Birthday CSV file
BIRTHDAY_FILE_NAME = "birthdays_pii.csv"

# List of available letter file names to choose from
LETTER_FILE_NAMES = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt",
]


def ordinal(n: int):
    """Code from https://stackoverflow.com/questions/9647202/ordinal-numbers-replacement"""
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix


# Get the current year, month and day
year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

# Read the birthday CSV file
birthday_data = pandas.read_csv(BIRTHDAY_FILE_NAME)

# Search for birthdays matching the current month and day
birthdays = birthday_data[(birthday_data['month'] == month) & (birthday_data['day'] == day)]

# Loop through any birthdays found
for index, row in birthdays.iterrows():
    # Get the name and e-mail
    name = row["name"]
    email = row["email"]
    birthday_year = row["year"]

    # Choose and open a random letter, replacing [NAME] with the actual name
    with open(random.choice(LETTER_FILE_NAMES)) as letter_file:
        letter = letter_file.read().replace("[NAME]", name)

    # Prepare the e-mail message
    message = f"From: {os.environ["SMTP_FROM"]}\nTo: {email}\nSubject: Happy {ordinal(year - birthday_year)} Birthday!\n\n{letter}"

    # Send the e-mail
    with smtplib.SMTP(host=os.environ["SMTP_HOST"], port=int(os.environ["SMTP_PORT"])) as smtp:
        smtp.starttls()
        smtp.login(user=os.environ["SMTP_USERNAME"], password=os.environ["SMTP_PASSWORD"])
        smtp.sendmail(from_addr=os.environ["SMTP_FROM"], to_addrs=email, msg=message)
