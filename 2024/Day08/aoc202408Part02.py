import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_array import read_file_as_array_array
import itertools

# Substitue test/real to switch inputs
data_set = 'real'
data = read_file_as_array_array(f'{data_set}_input.txt')

# Puzzle
antennas = {}

def extend_pairing(location_tuple, grid_size):
    location_1, location_2 = location_tuple
    location_arrays = [location_1, location_2]
    y_difference = location_2[0] - location_1[0]
    x_difference = location_2[1] - location_1[1]
    
    def extend_locations(multiplier):
        current_locations = location_arrays
        while (0 <= current_locations[-1][0] + multiplier * y_difference < grid_size and 0 <= current_locations[-1][1] + multiplier * x_difference < grid_size):
            next_location = [ current_locations[-1][0] + multiplier * y_difference, current_locations[-1][1] + multiplier * x_difference]
            current_locations.append(next_location)
        return current_locations
    
    # Extend in both positive and negative directions
    location_arrays.extend(extend_locations(1)[1:])
    location_arrays.extend(extend_locations(-1)[1:])
    
    # Clean Uniques
    return list({tuple(loc) for loc in location_arrays})

def solve():
    grid_size=len(data)
    anti_list=[]
    
    # Find Antennas
    for y_index,line in enumerate(data):
        for x_index,char in enumerate(line):
            if char != '.' and char != '#':
                if char in antennas.keys():
                    antennas[char].append ([y_index,x_index])
                else:
                    antennas[char] = [[y_index,x_index]]

    for aerial in antennas:
        found_antenna_pairings = list(itertools.combinations(antennas[aerial], 2))
        for pairing in found_antenna_pairings:
            for location in extend_pairing(pairing,grid_size):
                if location not in anti_list:
                    anti_list.append(location)

    print (f'We have {len(anti_list)} antinodes')
    

solve()