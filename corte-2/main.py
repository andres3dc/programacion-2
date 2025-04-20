from airline import Airline

airline = Airline()

while True:
    print("1. Crear vuelo")
    print("2. Vender tiquete")
    print("3. Check-in")
    print("4. Devolver pasaje")
    print("5. Reportes")
    print("6. Salir")

    try:
        option = int(input("Seleccione una opción: "))
    except:
        continue

    if option == 1:
        origin = input("Ciudad de origen: ")
        destination = input("Ciudad de destino: ")
        airline.create_flight(origin, destination)
    elif option == 2:
        origin = input("Ciudad de origen: ")
        destination = input("Ciudad de destino: ")
        flight = airline.find_flight(origin, destination)
        if flight:
            name = input("Nombre del pasajero: ")
            try:
                age = int(input("Edad: "))
                price = float(input("Valor del tiquete: "))
            except:
                continue
            gender = input("Género (masculino/femenino): ")
            travel_class = input("Clase (economica/ejecutiva/premium): ").lower()
            flight.sell_ticket(name, age, gender, travel_class, price)
    elif option == 3:
        origin = input("Ciudad de origen: ")
        destination = input("Ciudad de destino: ")
        flight = airline.find_flight(origin, destination)
        if flight:
            name = input("Nombre del pasajero: ")
            try:
                baggage_weight = float(input("Peso de maletas: "))
                bike_weight = float(input("Peso de bicicleta: "))
                dogs = int(input("Número de perros: "))
                cats = int(input("Número de gatos: "))
            except:
                continue
            flight.check_in(name, baggage_weight, bike_weight, dogs, cats)
    elif option == 4:
        origin = input("Ciudad de origen: ")
        destination = input("Ciudad de destino: ")
        flight = airline.find_flight(origin, destination)
        if flight:
            name = input("Nombre del pasajero: ")
            flight.refund_ticket(name)
    elif option == 5:
        result = airline.most_profitable_route()
        if result:
            print(f"Trayecto con mayor recaudo: {result[0]} -> {result[1]} con ${result[2]}")
        for flight in airline.flights:
            print(f"{flight.origin} -> {flight.destination}: Promedio tiquete: ${flight.average_ticket_price()}, Más viajan: {flight.gender_most_travel()}")
        print(f"Total recaudo por tiquetes: ${airline.total_ticket_revenue()}")
        print(f"Total recaudo por equipaje: ${airline.total_baggage_revenue()}")
    elif option == 6:
        break
