import sys
import os
import itertools
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')
red_tiles = [(int(a), int(b)) for a, b in (line.split(',') for line in data)]


def find_area(corners):
    y_distance = abs(corners[0][0]-corners[1][0])+1
    x_distance = abs(corners[0][1]-corners[1][1])+1
    return x_distance * y_distance


def is_valid(pair, edge):
    (bx1, by1), (bx2, by2) = pair
    rx_min, rx_max = min(bx1, bx2), max(bx1, bx2)
    ry_min, ry_max = min(by1, by2), max(by1, by2)

    for edge in edge:
        (lx1, ly1), (lx2, ly2) = edge
        lx_min, lx_max = min(lx1, lx2), max(lx1, lx2)
        ly_min, ly_max = min(ly1, ly2), max(ly1, ly2)

        if not (lx_max <= rx_min or lx_min >= rx_max or ly_max <= ry_min or ly_min >= ry_max):
            return False  
    return True  


# Puzzle
def solve():
    border = [ (red_tiles[i], red_tiles[(i+1)%len(red_tiles)]) for i in range(len(red_tiles)) ]

    pairs = list(itertools.combinations(red_tiles, 2))
    data_sorted = sorted(pairs, key=lambda x: find_area(x), reverse=True)

    for pair in data_sorted:
        if is_valid(pair, border):
            area = find_area(pair)
            return area

print (f'The answer is {solve()}')