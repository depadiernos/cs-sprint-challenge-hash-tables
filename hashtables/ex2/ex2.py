#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    itinerary = {}

    for ticket in tickets:
        itinerary[ticket.source] = ticket.destination

    route = []
    stop = itinerary["NONE"]
    
    index = 0

    while index < length:
        route.append(stop)
        stop = itinerary[stop]
        index += 1

    

    return route
