class FlightData:

    def __init__(self, price: int, origin_airport: str, destination_airport: str, stops: int, out_date: str,
                 return_date: str):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.stops = stops
        self.out_date = out_date
        self.return_date = return_date

    def __str__(self):
        return (f"Price: {self.price}, Origin Airport: {self.origin_airport}, "
                f"Destination Airport: {self.destination_airport}, Stops: {self.stops}, "
                f"Departure Date: {self.out_date}, Return Date: {self.return_date}"
                )
