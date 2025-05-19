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
    current_floor = 0
    for position, instruction in enumerate(data, start=1):
        if instruction == '(':
            current_floor += 1
        elif instruction == ')':
            current_floor -= 1
        # If in Basement
        if current_floor == -1:
            print (f'You enter the Basement after {position} instructions')
            return position

solve()
# You enter the Basement after 1795 instructions