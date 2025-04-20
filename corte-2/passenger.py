class Passenger:
    def __init__(self, name, age, gender, travel_class, ticket_price):
        self.name = name
        self.age = age
        self.gender = gender
        self.travel_class = travel_class
        self.ticket_price = ticket_price

    def baggage_limit(self):
        if self.travel_class == "economica":
            return 10
        elif self.travel_class == "ejecutiva":
            return 20
        elif self.travel_class == "premium":
            return 30
        return 0

    def extra_baggage_cost(self, extra_kilos):
        if extra_kilos <= 0:
            return 0
        if self.travel_class == "economica":
            return extra_kilos * 5000
        elif self.travel_class == "ejecutiva":
            return extra_kilos * 10000
        elif self.travel_class == "premium":
            return extra_kilos * self.ticket_price * 0.01
        return 0
