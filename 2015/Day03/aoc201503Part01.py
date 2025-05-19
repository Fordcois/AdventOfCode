import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_str(f'{data_set}_input.txt')

# Puzzle
def solve():
    visited_homes=[(0,0)]
    X_position = 0
    Y_position = 0
    for char in data:
        if char == '>':
            X_position += 1
        elif char == '<':
            X_position -= 1
        elif char == '^':
            Y_position +=1
        elif char == 'v':
            Y_position -= 1
        if (X_position,Y_position) not in visited_homes:
            visited_homes.append((X_position,Y_position))

    print (f'Presents at {len(visited_homes)} unique homes')
    return len(visited_homes)

solve()
# Presents at 2572 unique homes