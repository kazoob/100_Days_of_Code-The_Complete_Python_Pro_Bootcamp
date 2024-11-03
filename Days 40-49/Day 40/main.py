# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Create classes.
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Get sheet data.
sheet_data = data_manager.get_sheet_data()

# Get any sheet rows with missing IATA code.
iata_missing = [row["city"] for row in sheet_data if not row["iataCode"]]

# Check if there are any rows with missing IATA codes.
if iata_missing:

    # Get missing IATA Codes and update sheet.
    for city in iata_missing:
        iata = flight_search.get_iata_code(city)
        data_manager.update_iata_code(city, iata)

    # Get updated sheet data.
    sheet_data = data_manager.get_sheet_data()

# Get flight results.
for row in sheet_data:
    flight = flight_search.find_flights(row["iataCode"], int(row["lowestPrice"]))

    # Check for valid flight
    if flight:
        print(flight)

        # Send SMS message
        # notification_manager.send_sms(flight)

        # Send e-mail message to all users
        for email in data_manager.get_user_emails():
            notification_manager.send_email(flight, email)
    else:
        print(f"No flights found for {row["city"]}.")
