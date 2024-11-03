import os
from twilio.rest import Client
from flight_data import FlightData
import smtplib


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

    def send_email(self, flight: FlightData, email: str):
        # Prepare the e-mail message
        message = (f"From: {os.environ["SMTP_FROM"]}\n"
                   f"To: {email}\n"
                   f"Subject: Flight Deal Alert to {flight.destination_airport}\n\n"
                   f"Only {flight.price} to fly from {flight.origin_airport} to {flight.destination_airport}, ")
        if flight.stops == 1:
            message += f"with {flight.stops} stop, "
        else:
            message += f"with {flight.stops} stops, "
        message += f"departing on {flight.out_date} and returning on {flight.return_date}."

        # Send the e-mail
        with smtplib.SMTP(host=os.environ["SMTP_HOST"], port=int(os.environ["SMTP_PORT"])) as smtp:
            smtp.starttls()
            smtp.login(user=os.environ["SMTP_USERNAME"], password=os.environ["SMTP_PASSWORD"])
            smtp.sendmail(from_addr=os.environ["SMTP_FROM"], to_addrs=email, msg=message)
