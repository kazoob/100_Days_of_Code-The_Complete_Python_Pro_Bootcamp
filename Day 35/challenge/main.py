import requests
import json

OPENWEATHER_PII_FILE_NAME = "../../openweather_pii.json"

# Open the Open Weather configuration file
with open(OPENWEATHER_PII_FILE_NAME) as openweather_pii_file:
    openweather_pii = json.load(openweather_pii_file)

# Get the Open Weather configuration fields
openweather_api_key = openweather_pii['api_key']
openweather_lat = openweather_pii['lat']
openweather_long = openweather_pii['long']

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

# Display result
if will_rain:
    print("Bring an umbrella! ☂️")
else:
    print("No umbrella needed. ☀️")
