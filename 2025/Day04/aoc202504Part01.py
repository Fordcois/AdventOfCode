import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_of_str_arrays import file_as_list_of_string_arrays
from utilities.get_from_grid import grid_get

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_string_arrays(f'{data_set}_input.txt')

# Puzzle

def count_surrounding_rolls(y,x):
    surrounding_rolls = 0
    neighbors = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),          ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1),
    ]
    for x_offset,y_offset in neighbors:
        if grid_get(data,x+x_offset,y+y_offset) == '@':
            surrounding_rolls += 1
    return surrounding_rolls

def solve():
    grabbed_rolls = 0

    for x_index,row in enumerate(data):
        for y_index, item in enumerate(row):
            if grid_get(data,x_index,y_index) == '@' and count_surrounding_rolls(y_index,x_index) < 4:
                grabbed_rolls += 1

                

    print (f'Grabbed Rolls: {grabbed_rolls}')
    return grabbed_rolls

solve()

