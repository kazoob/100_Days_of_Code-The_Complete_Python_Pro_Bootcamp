import os
import requests


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        # Determine whether to use cached API data or get live data from API.
        self._use_cached_json = os.environ.get("USE_CACHED_JSON", "False")

        # API information.
        self._api_endpoint = (f"https://api.sheety.co/{os.environ["SHEETY_USERNAME"]}/"
                              f"{os.environ["SHEETY_FLIGHT_PROJECT_NAME"]}/"
                              f"{os.environ["SHEETY_FLIGHT_SHEET_NAME"]}")
        self._api_key = os.environ["SHEETY_API_KEY"]

        # API authentication headers.
        self._api_headers = {
            "Authorization": f"Bearer {self._api_key}",
        }

        # Get live results from API.
        if self._use_cached_json != "True":
            # API request.
            response = requests.get(url=self._api_endpoint, headers=self._api_headers)
            #response.raise_for_status()

            # Get JSON data.
            # TODO error checking
            self.sheet_data = response.json()["prices"]
        # Use cached API data.
        else:
            self.sheet_data = [{'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 1260, 'id': 2},
                               {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 1240, 'id': 3}]

    def get_sheet_data(self) -> list:
        """Return flight sheet data."""
        return self.sheet_data

    def update_iata_code(self, city: str, iata: str):
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
            response = requests.put(url=f"{self._api_endpoint}/{row["id"]}", headers=self._api_headers,
                                    json=update_params)
            #response.raise_for_status()
        # No row was found.
        else:
            print(f"{city} not found in sheet")
