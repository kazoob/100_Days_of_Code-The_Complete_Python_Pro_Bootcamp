# This class is responsible for structuring the flight data.
class FlightData:

    def __init__(self, price: int, origin_airport: str, destination_airport: str, out_date: str, return_date: str):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def __str__(self):
        return (f"Price: {self.price}, Origin Airport: {self.origin_airport}, "
                f"Destination Airport: {self.destination_airport}, Departure Date: {self.out_date}, "
                f"Return Date: {self.return_date}"
                )
