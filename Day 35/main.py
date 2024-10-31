import requests
import os
from twilio.rest import Client

# Prepare the API parameters
parameters: dict[str, str | float | int] = {
    "appid": os.environ["OPENWEATHER_API_KEY"],
    "lat": os.environ["OPENWEATHER_LAT"],
    "lon": os.environ["OPENWEATHER_LONG"],
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
twilio_client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

twilio_message = twilio_client.messages.create(
    body=twilio_body,
    from_=os.environ["TWILIO_FROM"],
    to=os.environ["TWILIO_TO"],
)

print(twilio_message.status)
