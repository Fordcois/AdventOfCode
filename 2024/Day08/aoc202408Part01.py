import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_array import read_file_as_array_array
from utilities.get_from_grid import grid_get as location_in_bounds
import itertools

# Substitue test/real to switch inputs
data_set = 'real'
data = read_file_as_array_array(f'{data_set}_input.txt')

# Puzzle
antennas = {}

def find_antinode_locations(location_tuple):
    # Calculate differences
    y_difference = abs(location_tuple[0][0] - location_tuple[1][0])
    x_difference = abs(location_tuple[0][1] - location_tuple[1][1])

    y_sort = sorted(location_tuple, key=lambda x: x[0])
    # Modifications for y and x directions
    x_modify = ([0, -x_difference], [0, x_difference])
    y_modify = ([-y_difference, 0], [y_difference, 0])

    # Y modifications
    result_y = [
        (a[0] + b[0], a[1] + b[1])
        for a, b in zip(y_sort, y_modify)
    ]
    # Sort the result by x-coordinate
    x_sort = sorted(result_y, key=lambda x: x[1])

    # x modifications
    result_x = [
        (a[0] + b[0], a[1] + b[1])
        for a, b in zip(x_sort, x_modify)
    ]
    return tuple(result_x)

def solve():
    anti_list=[]

    for y_index,line in enumerate(data):
        for x_index,char in enumerate(line):
            if char != '.' and char != '#':
                if char in antennas.keys():
                    antennas[char].append ([y_index,x_index])
                else:
                    antennas[char] = [[y_index,x_index]]


        
    for aerial in antennas:
        found_antenna_pairings = list(itertools.combinations(antennas[aerial], 2))

        for pair in found_antenna_pairings:
            possible_antinode_spots=find_antinode_locations(pair)
            
            for spot in possible_antinode_spots:
                if location_in_bounds(data,spot[1],spot[0],False) != False:
                    if spot not in anti_list:
                        anti_list.append(spot)
                        
    print (f'We Found {len(anti_list)} antinodes')

solve()