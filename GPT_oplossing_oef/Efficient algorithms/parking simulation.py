import heapq
class PriorityQueue:
    def __init__(self):
        self.content = []

    def add(self, item):
        heapq.heappush(self.content, item)

    def peek(self):
        return self.content[0]

    def poll(self):
        return heapq.heappop(self.content) if len(self.content) > 0 else None

    def is_empty(self):
        return len(self.content) == 0

    def __str__(self):
        return str(heapq.nsmallest(len(self.content), self.content))


def simuleer_parking(aantalParkeerplaatsen, blokTijd, klanten):
    # Sort customers by arrival time (natural arrival order)
    klanten = sorted(klanten, key=lambda x: x[0])

    # PQ of events: (time, type, data)
    # type 0 = departure, type 1 = arrival   → so departures happen before arrivals at same time
    events = PriorityQueue()

    # Load all arrival events
    for aankomst, duur in klanten:
        events.add((aankomst, 1, duur))

    vrije = aantalParkeerplaatsen
    laatste_vertrek = 0

    # Customer waiting queue (priority: shortest shopping time first, then earliest arrival)
    wacht = PriorityQueue()

    while not events.is_empty():
        tijd, typ, data = events.poll()

        if typ == 0:  
            # Departure
            vrije += 1
            laatste_vertrek = tijd

            # After a departure, try to park waiting customers
            if not wacht.is_empty():
                duur, aankomst = wacht.poll()   # shortest shopping time gets priority
                vrije -= 1
                vertrek = tijd + duur
                events.add((vertrek, 0, None))

        else:
            # Arrival
            aankomsttijd = tijd
            winkeltijd = data

            if vrije > 0:
                # Customer can park immediately
                vrije -= 1
                vertrek = aankomsttijd + winkeltijd
                events.add((vertrek, 0, None))
            else:
                # Parking full — customer drives around and comes back
                # but only after being inserted in WAIT queue in priority order
                wacht.add((winkeltijd, aankomsttijd))
                # They return later
                events.add((aankomsttijd + blokTijd, 1, winkeltijd))

    return laatste_vertrek