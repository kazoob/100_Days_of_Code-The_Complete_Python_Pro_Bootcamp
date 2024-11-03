import os
import requests

SHEETY_ENDPOINT_BASE = "https://api.sheety.co"


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        # Determine whether to use cached API data or get live data from API.
        self._use_cached_json = os.environ.get("USE_CACHED_JSON", "False")

        # API information.
        self._api_endpoint_project = (
            f"{SHEETY_ENDPOINT_BASE}/{os.environ["SHEETY_USERNAME"]}/{os.environ["SHEETY_FLIGHT_PROJECT_NAME"]}")
        self._api_endpoint_prices = (
            f"{self._api_endpoint_project}/{os.environ["SHEETY_FLIGHT_PRICES_SHEET_NAME"]}")
        self._api_endpoint_users = (
            f"{self._api_endpoint_project}/{os.environ["SHEETY_FLIGHT_USERS_SHEET_NAME"]}")
        self._api_key = os.environ["SHEETY_API_KEY"]

        # API authentication headers.
        self._api_headers = {
            "Authorization": f"Bearer {self._api_key}",
        }

        # Get live results from API.
        if self._use_cached_json != "True":
            # API request for prices.
            prices_response = requests.get(url=self._api_endpoint_prices, headers=self._api_headers)
            # prices_response.raise_for_status()

            # Get JSON data.
            # TODO error checking
            self.sheet_data = prices_response.json()["prices"]

            # API request for users.
            users_response = requests.get(url=self._api_endpoint_users, headers=self._api_headers)
            # users_response.raise_for_status()

            # Get JSON data.
            # TODO error checking
            self.emails = [row["whatIsYourEMailAddress?"] for row in users_response.json()["users"]]
            print(self.emails)
        # Use cached API data.
        else:
            self.sheet_data = [{'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 1260, 'id': 2},
                               {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 1240, 'id': 3}]
            self.emails = ['cordial.home5226@gridmail.ca']

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
            response = requests.put(url=f"{self._api_endpoint_prices}/{row["id"]}", headers=self._api_headers,
                                    json=update_params)
            # response.raise_for_status()
        # No row was found.
        else:
            print(f"{city} not found in sheet")

    def get_user_emails(self):
        """Return user e-mail list."""
        return self.emails
