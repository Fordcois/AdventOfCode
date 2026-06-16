import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_list_of_ints import file_as_list_of_ints

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_ints(f'{data_set}_input.txt')

# Puzzle
def solve():
    valid_triangles = 0
    for potential_triangle in data:
        short_edge,mid_edge,long_edge = sorted(potential_triangle)
        if short_edge+mid_edge > long_edge:
            valid_triangles += 1
    
    print (f"{valid_triangles} valid triangles")
    return

solve()