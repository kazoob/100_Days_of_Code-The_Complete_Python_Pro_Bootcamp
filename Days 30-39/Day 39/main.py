# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

# Get sheet data.
sheet_data = data_manager.get_sheet_data()

# Get any sheet rows with missing IATA code.
iata_missing = [row["city"] for row in sheet_data if not row["iataCode"]]

# Check if there are any rows with missing IATA codes.
if iata_missing:

    # Get missing IATA Codes and update sheet.
    for city in iata_missing:
        iata = flight_search.get_iata_code(city)
        data_manager.update_iata(city, iata)

    # Get updated sheet data.
    sheet_data = data_manager.get_sheet_data()
