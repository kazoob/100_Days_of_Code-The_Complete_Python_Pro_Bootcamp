import requests
from datetime import datetime
import smtplib
import tzlocal
import os

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

    # Prepare the e-mail message
    message = f"From: {os.environ["SMTP_FROM"]}\nTo: {os.environ["SMTP_FROM"]}\nSubject: Look up!\n\nThe ISS is overhead and it is dark outside!"

    # Send the e-mail
    with smtplib.SMTP(host=os.environ["SMTP_HOST"], port=int(os.environ["SMTP_PORT"])) as smtp:
        smtp.starttls()
        smtp.login(user=os.environ["SMTP_USERNAME"], password=os.environ["SMTP_PASSWORD"])
        smtp.sendmail(from_addr=os.environ["SMTP_FROM"], to_addrs=os.environ["SMTP_FROM"], msg=message)
elif iss_overhead:
    print("The ISS is overhead but it is not dark outside.")
else:
    print("The ISS is not overhead.")

# BONUS: run the code every 60 seconds.
