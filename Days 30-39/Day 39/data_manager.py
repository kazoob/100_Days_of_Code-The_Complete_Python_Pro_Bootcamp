import os
import requests

CACHED = True
API_ENDPOINT = (f"https://api.sheety.co/{os.environ["SHEETY_USERNAME"]}/"
                f"{os.environ["SHEETY_FLIGHT_PROJECT_NAME"]}/"
                f"{os.environ["SHEETY_FLIGHT_SHEET_NAME"]}")
API_KEY = os.environ["SHEETY_API_KEY"]


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        # API authentication headers.
        self.api_headers = {
            "Authorization": f"Bearer {API_KEY}",
        }

        # Get live results from API.
        if not CACHED:
            # API request.
            response = requests.get(url=API_ENDPOINT, headers=self.api_headers)
            response.raise_for_status()

            # Get JSON data.
            self.sheet_data = response.json()["prices"]
        # Use cached API data.
        else:
            self.sheet_data = [{'city': 'Tokyo', 'iataCode': 'TEST', 'lowestPrice': 485, 'id': 2},
                               {'city': 'San Francisco', 'iataCode': 'TEST', 'lowestPrice': 260, 'id': 3},
                               {'city': 'Dublin', 'iataCode': 'TEST', 'lowestPrice': 378, 'id': 4}]

    def get_sheet_data(self):
        """Return flight sheet data."""
        print(self.sheet_data)
        return self.sheet_data

    def update_iata(self, city, iata):
        """Update the IATA code for a given city."""

        # Get the sheet row (dictionary) matching the provided city.
        row = next((item for item in self.sheet_data if item['city'] == city), None)

        # If a row was found, update the IATA code.
        if row:
            # Update the sheet row (dictionary).
            row["iataCode"] = iata

            # Update the sheet via API.
            update_params = {
                "price": {
                    "iataCode": row["iataCode"],
                }
            }
            response = requests.put(url=f"{API_ENDPOINT}/{row["id"]}", headers=self.api_headers, json=update_params)
            response.raise_for_status()
        # No row was found.
        else:
            print(f"{city} not found in sheet")
