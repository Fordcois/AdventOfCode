import sys
import os
import math
import itertools

# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitute test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')
data = [tuple(int(y) for y in x.split(',')) for x in data]  

def solve():
    combos = list(itertools.combinations(data, 2))

    distance_combos = [[math.dist(a, b), (a, b)] for a, b in combos]

    # Sort by disnttance
    data_sorted = [x[1] for x in sorted(distance_combos, key=lambda x: x[0])]

    junctions =[set([box]) for box in data]
    complete_circuit_size = len(data)

    for connection in data_sorted:
        a,b = connection
        group_a = next(g for g in junctions if a in g)
        group_b = next(g for g in junctions if b in g)
        if group_a != group_b:
            junctions.remove(group_a)
            junctions.remove(group_b)
            merged = group_a | group_b
            if len(merged) == complete_circuit_size:
                final_connector = connection
                break
            junctions.append(merged)


    return (final_connector[0][0])*(final_connector[1][0])

print (f'The answer is {solve()}')


