import os
import requests

API_ENDPOINT = "https://test.api.amadeus.com"
API_KEY = os.environ["AMADEUS_TEST_API_KEY"]
API_SECRET = os.environ["AMADEUS_TEST_API_SECRET"]


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self):
        pass
