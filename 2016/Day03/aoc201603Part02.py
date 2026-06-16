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
    potential_triangles=[]
    valid_triangles = 0
    for i in range (0,len(data),3):
        print (i)
        potential_triangles.append([data[i][0],data[i+1][0],data[i+2][0]])
        potential_triangles.append([data[i][1],data[i+1][1],data[i+2][1]])
        potential_triangles.append([data[i][2],data[i+1][2],data[i+2][2]])

    for potential_triangle in potential_triangles:
        short_edge,mid_edge,long_edge = sorted(potential_triangle)
        if short_edge+mid_edge > long_edge:
            valid_triangles += 1
    
    print (f"{valid_triangles} valid triangles")
    return

solve()