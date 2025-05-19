import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

# Puzzle
def calculate_volume(input_dimensions):
    l,w,h = [int(x) for x in input_dimensions.split('x')]
    sides = [l*w,w*h,h*l]
    return ((sum(sides)*2) + sorted(sides)[0])

def solve():
    total = 0
    for parcel in data:
        total += calculate_volume(parcel)
    print (f' The total is {total}')
    return

solve()
#  The total is 1606483