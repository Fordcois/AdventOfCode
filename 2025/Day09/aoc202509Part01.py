import sys
import os
import itertools
import math
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings


# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')
# Swap X/Y Coordinates from input
data = [[int(a), int(b)] for a, b in (line.split(',') for line in data)]

def find_area(corners):
    y_distance = abs(corners[0][0]-corners[1][0])+1
    x_distance = abs(corners[0][1]-corners[1][1])+1
    return (x_distance * y_distance)


# Puzzle
def solve():

    combos = list(itertools.combinations(data, 2))
# Sort by disnttance
    data_sorted = [f'{find_area(x)} - {x}' for x in sorted(combos, key=lambda x: find_area(x),reverse=True)]
    print(data_sorted[1])


solve()