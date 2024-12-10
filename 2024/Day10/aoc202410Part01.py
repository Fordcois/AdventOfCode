import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_list_of_int_array import file_as_list_of_int_arrays
from utilities.get_from_grid import grid_get

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_int_arrays(f'{data_set}_input.txt')


def recursive_travel(current_level, y, x, current_path):
    if grid_get(data, x, y) == 9:
        complete_path.append(current_path)
        return
    
    directions = [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]
    for next_y, next_x in directions:
        if grid_get(data, next_x, next_y) == current_level + 1:
            new_path = current_path + [(next_y, next_x)]
            recursive_travel(current_level + 1, next_y, next_x, new_path)

def solve():
    total_trailheads=0
    
    for y_index, line in enumerate(data):
        for x_index, char in enumerate(line):
            if char == 0:
                global complete_path
                complete_paths = []
                complete_path = []
                unique_ends=[]
                recursive_travel(char, y_index, x_index, [(y_index, x_index)])
                complete_paths.extend(complete_path)
                
                for path in complete_path:
                    if path[-1] not in unique_ends:
                        unique_ends.append(path[-1])
            
                total_trailheads += len(unique_ends)

    print (f'The total is {total_trailheads}')
    
solve()