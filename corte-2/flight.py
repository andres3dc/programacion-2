from passenger import Passenger

class Flight:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.passengers = []
        self.ticket_revenue = 0
        self.baggage_revenue = 0

    def sell_ticket(self, name, age, gender, travel_class, price):
        if age < 0 or price < 0:
            return
        if age <= 13:
            price *= 0.93
        passenger = Passenger(name, age, gender, travel_class, price)
        self.passengers.append(passenger)
        self.ticket_revenue += price

    def find_passenger(self, name):
        for p in self.passengers:
            if p.name == name:
                return p
        print("Pasajero no encontrado.")
        return None

    def check_in(self, name, baggage_weight, bike_weight, dogs, cats):
        passenger = self.find_passenger(name)
        if not passenger:
            return
        extra_baggage = max(0, baggage_weight - passenger.baggage_limit())
        baggage_cost = passenger.extra_baggage_cost(extra_baggage)
        special_cargo_cost = (bike_weight * 3000) + (dogs * passenger.ticket_price * 0.05) + (cats * passenger.ticket_price * 0.02)
        total = baggage_cost + special_cargo_cost
        self.baggage_revenue += total

    def refund_ticket(self, name):
        passenger = self.find_passenger(name)
        if passenger:
            self.ticket_revenue -= passenger.ticket_price
            self.passengers.remove(passenger)

    def gender_most_travel(self):
        male = sum(1 for p in self.passengers if p.gender.lower() == "masculino")
        female = sum(1 for p in self.passengers if p.gender.lower() == "femenino")
        return "femeninas" if female > male else "masculinos"

    def average_ticket_price(self):
        if not self.passengers:
            return 0
        return round(sum(p.ticket_price for p in self.passengers) / len(self.passengers), 2)

    def total_revenue(self):
        return self.ticket_revenue + self.baggage_revenue
