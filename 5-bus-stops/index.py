def number(bus_stops):
    counter = 0

    for people_on_a_stop in bus_stops:
        counter += people_on_a_stop[0]
        counter -= people_on_a_stop[1]
    return counter
