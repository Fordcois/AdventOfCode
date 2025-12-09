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



def merge_arrays(lists):
    sets = [set(lst) for lst in lists]
    merged = True

    while merged:
        merged = False
        new_sets = []

        while sets:
            first, *rest = sets
            first = set(first)
            i = 0
            while i < len(rest):
                if first & rest[i]:  
                    first |= rest.pop(i)
                    merged = True
                else:
                    i += 1
            new_sets.append(first)
            sets = rest

        sets = new_sets

    return sets

def solve():
    joins = 1000
    combos = list(itertools.combinations(data, 2))

    distance_combos = [[math.dist(a, b), (a, b)] for a, b in combos]

    data_sorted = [x[1] for x in sorted(distance_combos, key=lambda x: x[0])]
    top_combos = data_sorted[:joins]  

    pair_lists = [list(combo) for combo in top_combos]
    
    merged_groups = merge_arrays(pair_lists)
    circuit_sizes = [len(x) for x in merged_groups]
    circuit_sizes.sort(reverse=True)
    return math.prod(circuit_sizes[:3])

print (f'The answer is {solve()}')
