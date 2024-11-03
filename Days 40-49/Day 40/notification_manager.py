import os
from twilio.rest import Client
from flight_data import FlightData


# This class is responsible for sending notifications with the deal flight details.
class NotificationManager:

    def __init__(self):
        self.twilio_client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    def send_sms(self, flight: FlightData):
        # Send SMS message.
        twilio_message = self.twilio_client.messages.create(
            body=flight,
            from_=os.environ["TWILIO_FROM"],
            to=os.environ["TWILIO_TO"],
        )
