from flight import Flight

class Airline:
    def __init__(self):
        self.flights = []

    def create_flight(self, origin, destination):
        self.flights.append(Flight(origin, destination))

    def find_flight(self, origin, destination):
        for flight in self.flights:
            if flight.origin == origin and flight.destination == destination:
                return flight
        print("Vuelo no encontrado.")
        return None

    def most_profitable_route(self):
        if not self.flights:
            return None
        max_flight = max(self.flights, key=lambda f: f.total_revenue())
        return (max_flight.origin, max_flight.destination, max_flight.total_revenue())

    def total_ticket_revenue(self):
        return sum(flight.ticket_revenue for flight in self.flights)

    def total_baggage_revenue(self):
        return sum(flight.baggage_revenue for flight in self.flights)
