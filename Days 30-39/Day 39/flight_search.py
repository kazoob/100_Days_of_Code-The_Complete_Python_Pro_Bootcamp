import os
import requests


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self):
        # API information.
        self._api_endpoint = "https://test.api.amadeus.com/v1"
        self._api_key = os.environ["AMADEUS_TEST_API_KEY"]
        self._api_secret = os.environ["AMADEUS_TEST_API_SECRET"]

        # Get API access token.
        self._token = self._get_new_token()

    def _get_new_token(self):
        # Token API information.
        token_api_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"

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
        response.raise_for_status()

        # Return access token.
        return response.json()["access_token"]

    def get_iata_code(self, city):
        return "TEST"
