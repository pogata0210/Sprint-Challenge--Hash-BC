#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # first construct a hash table
    for i, weight in enumerate(weights):    # enumerates adds keys
        hash_table_insert(ht, weight, i)

    for i, weight in enumerate(weights):
        j = hash_table_retrieve(ht, limit - weight)
        if j is not None:
            if i > j:   # to make sure the larger index is first in the order
                return (i, j)

            else:
                return (j, i)

    return None

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
