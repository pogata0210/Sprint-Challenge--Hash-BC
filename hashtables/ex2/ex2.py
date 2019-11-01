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
    route = [None] * length
    
    #initialize hashtable
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        
    # function to find the first ticket
    for ticket in tickets:
        if ticket.source == 'NONE': #if none there is no starting point. Therefore it must be the starting point.
            route.append(ticket.destination) #add to list.
            break 

    while len(route) < length:   #while there is more keep looping.
        next_flight = hash_table_retrieve(hashtable, route[-1]) 
        route.append(next_flight)       #add to the list  

    return route
