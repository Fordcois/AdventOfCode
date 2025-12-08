import sys
import os
from functools import lru_cache
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings
from utilities.get_from_grid import grid_get

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

bottom = len(data)

@lru_cache(maxsize=None)  
def reach_bottom(y,x):
    if y == bottom-1:
        return 1
    else:
        below = grid_get(data,x,y+1)
        if below == '^':
            return reach_bottom(y+1,x-1) + reach_bottom(y+1,x+1)
        else:
            return reach_bottom(y+1,x)
        
# Puzzle
def solve():
    start_x = data[0].index('S')
    total_timelines = reach_bottom(0, start_x)
    return total_timelines

print(f' The answer is: {solve()}')
