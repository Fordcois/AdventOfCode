import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings
from utilities.get_from_grid import grid_get

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def descend(beam_loc):
    splits = 0
    new_levels = []

    below = grid_get(data, beam_loc[1], beam_loc[0] + 1)

    if below == '^':
        splits = 1
        new_levels.extend([
            [beam_loc[0]+1, beam_loc[1]-1],
            [beam_loc[0]+1, beam_loc[1]+1]
        ])
    else:
        new_levels.append([beam_loc[0]+1, beam_loc[1]])

    return new_levels, splits


# Puzzle
def solve():
    splits = 0
    height = len(data)
    start = [0,data[0].index('S')]
    beams=[start]
    for i in range(1, height):
        new_beams = []     
        for beam in beams:
            new_locs, split_count = descend(beam)
            splits += split_count
            for loc in new_locs:
                if loc not in new_beams:
                    new_beams.append(loc)

        beams = new_beams
    return splits

        
print(f' The answer is: {solve()}')
