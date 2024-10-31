import requests
import json
import os
from twilio.rest import Client

OPENWEATHER_PII_FILE_NAME = "../openweather_pii.json"
TWILIO_PII_FILE_NAME = "../twilio_pii.json"

with open(OPENWEATHER_PII_FILE_NAME) as openweather_pii_file:
    openweather_pii = json.load(openweather_pii_file)

# Get the Open Weather configuration fields
openweather_api_key = openweather_pii['api_key']
openweather_lat = openweather_pii['lat']
openweather_long = openweather_pii['long']

# Open the Twilio configuration file
with open(TWILIO_PII_FILE_NAME) as twilio_pii_file:
    twilio_pii = json.load(twilio_pii_file)

twilio_account_sid = twilio_pii["account_sid"]
twilio_auth_token = twilio_pii["auth_token"]
twilio_from = twilio_pii["from"]
twilio_to = twilio_pii["to"]

# Prepare the API parameters
parameters: dict[str, str | float | int] = {
    "appid": openweather_api_key,
    "lat": openweather_lat,
    "lon": openweather_long,
    "units": "metric",
    "cnt": 4,
}

# Send the API request
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

# Get the JSON data
weather_data = response.json()

will_rain: bool = False

# Loop through each hour data as well as each condition data, look for rain (< 700)
for hour_data in weather_data["list"]:
    for condition_data in hour_data["weather"]:
        if int(condition_data["id"]) < 700:
            will_rain = True

# Get the result
twilio_body: str

if will_rain:
    twilio_body = "Bring an umbrella! ☂️"
else:
    twilio_body = "No umbrella needed. ☀️"

# Send result via Twilio SMS
twilio_client = Client(twilio_account_sid, twilio_auth_token)

twilio_message = twilio_client.messages.create(
    body=twilio_body,
    from_=twilio_from,
    to=twilio_to,
)

print(twilio_message.status)
