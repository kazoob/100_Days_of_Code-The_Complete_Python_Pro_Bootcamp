import os
import requests

API_ENDPOINT = (f"https://api.sheety.co/{os.environ["SHEETY_USERNAME"]}/"
                f"{os.environ["SHEETY_FLIGHT_PROJECT_NAME"]}/"
                f"{os.environ["SHEETY_FLIGHT_SHEET_NAME"]}")
API_KEY = os.environ["SHEETY_API_KEY"]


# This class is responsible for talking to the Google Sheet.
class DataManager:

    def __init__(self):
        pass
