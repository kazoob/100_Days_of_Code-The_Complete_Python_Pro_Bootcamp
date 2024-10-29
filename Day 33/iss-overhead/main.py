import requests
from datetime import datetime
import smtplib
import json
import tzlocal

MY_LAT = -50.1357  # Your latitude
MY_LONG = -151.7149  # Your longitude

SMTP_PII_FILE_NAME = "../../smtp_pii.json"


def is_iss_overhead(lat, long):
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    if lat - 5 <= iss_latitude <= lat + 5 and long - 5 <= iss_longitude <= long + 5:
        return True
    else:
        return False


def is_dark_outside(lat, long):
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
        "tzid": tzlocal.get_localzone_name()
    }

    sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()
    sunset_data = sunset_response.json()

    sunrise = int(sunset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sunset_data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if sunset <= hour_now or hour_now <= sunrise:
        print("Dark")
        return True
    else:
        print("Light")
        return False


iss_overhead = is_iss_overhead(MY_LAT, MY_LONG)
dark_outside = is_dark_outside(MY_LAT, MY_LONG)

if iss_overhead and dark_outside:
    print("The ISS is overhead and it is dark outside!")

    # Open the SMTP configuration file
    with open(SMTP_PII_FILE_NAME) as smtp_pii_file:
        smtp_pii = json.load(smtp_pii_file)

    # Get the SMTP configuration fields
    smtp_username = smtp_pii['username']
    smtp_password = smtp_pii['password']
    smtp_from = smtp_pii['from']
    smtp_host = smtp_pii['host']
    smtp_port = smtp_pii['port']

    # Prepare the e-mail message
    message = f"From: {smtp_from}\nTo: {smtp_from}\nSubject: Look up!\n\nThe ISS is overhead and it is dark outside!"

    # Send the e-mail
    with smtplib.SMTP(host=smtp_host, port=smtp_port) as smtp:
        smtp.starttls()
        smtp.login(user=smtp_username, password=smtp_password)
        smtp.sendmail(from_addr=smtp_from, to_addrs=smtp_from, msg=message)
elif iss_overhead:
    print("The ISS is overhead but it is not dark outside.")
else:
    print("The ISS is not overhead.")

# BONUS: run the code every 60 seconds.
