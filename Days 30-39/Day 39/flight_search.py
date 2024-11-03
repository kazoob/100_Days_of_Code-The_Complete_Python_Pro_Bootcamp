import os
import requests
from datetime import date, timedelta
from flight_data import FlightData

AMADEUS_TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_CITY_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_FLIGHT_SEARCH_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self):
        # API information.
        self._api_key = os.environ["AMADEUS_TEST_API_KEY"]
        self._api_secret = os.environ["AMADEUS_TEST_API_SECRET"]

        # Get API access token.
        self._api_token = self._get_new_token()
        self._api_header = {
            "Authorization": f"Bearer {self._api_token}",
        }

    def _get_new_token(self) -> str:
        """Get new access (bearer) token."""
        # Token API information.
        token_api_endpoint = AMADEUS_TOKEN_ENDPOINT

        # Token API headers.
        token_api_header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        # Token API body.
        token_api_body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        # API request.
        response = requests.post(url=token_api_endpoint, headers=token_api_header, data=token_api_body)
        # response.raise_for_status()

        # Return access token.
        # TODO error checking
        return response.json()["access_token"]

    def get_iata_code(self, city: str) -> str:
        """Get IATA code for provided city."""
        # API information.
        api_endpoint = AMADEUS_CITY_SEARCH_ENDPOINT

        # API parameters.
        api_parameters = {
            "keyword": city,
            "max": "1",
            "include": "AIRPORTS",
        }

        # API request.
        response = requests.get(url=api_endpoint, headers=self._api_header, params=api_parameters)
        # response.raise_for_status()

        # Return IATA code.
        # TODO error checking
        return response.json()["data"][0]['iataCode']

    def find_flights(self, iata_code: str, max_price: int) -> FlightData:
        """Find the cheapest flight available for the provided IATA code within a maximum price."""
        # API information.
        api_endpoint = AMADEUS_FLIGHT_SEARCH_ENDPOINT

        # Dates.
        departure_date = date.today()
        return_date = departure_date + timedelta(days=7)

        # API parameters.
        api_parameters = {
            "originLocationCode": "LON",
            "destinationLocationCode": iata_code,
            "departureDate": departure_date.strftime("%Y-%m-%d"),
            "returnDate": return_date.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "maxPrice": max_price,
            "max": 10,
        }

        # API request.
        response = requests.get(url=api_endpoint, headers=self._api_header, params=api_parameters)
        # response.raise_for_status()
        # TODO error checking

        # Check for valid response.
        if response.status_code == 200:
            # Get response JSON.
            response_json = response.json()

            lowest_price = None
            cheapest_flight = None

            # Compare each flight.
            for flight in response_json["data"]:
                # Get the flight price.
                price = int(round(float(flight["price"]["grandTotal"]), 0))

                # If no cheapest flight or current flight is cheaper, set new cheapest flight.
                if cheapest_flight is None or price < lowest_price:
                    lowest_price = price
                    origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                    destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                    out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                    return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

            return cheapest_flight
        # API error, return None.
        else:
            print(response.json())
            return None
