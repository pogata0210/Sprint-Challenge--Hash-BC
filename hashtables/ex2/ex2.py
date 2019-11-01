#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = []

    # make hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # find the first ticket
    for ticket in tickets:
        if ticket.source == 'NONE':
            route.append(ticket.destination)
            break
    
    while len(route) < length:
        next_flight = hash_table_retrieve(hashtable, route[-1])
        route.append(next_flight)

    return route

    return route
