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
def calculate_shortest_sides(l,w,h):
    shortest_sides = sorted([l,w,h])
    return (shortest_sides[0] + shortest_sides[1])*2

def calculate_ribbon(l,w,h):
    return (l*w*h)
    

def solve():
    total_ribbon = 0
    for parcel in data:
        l,w,h = [int(x) for x in parcel.split('x')]
        total_ribbon += calculate_shortest_sides(l,w,h,) + calculate_ribbon(l,w,h)
    print (f'You need {total_ribbon} ft of Ribbon')
    return True

solve()
# You need 3842356ft of Ribbon


