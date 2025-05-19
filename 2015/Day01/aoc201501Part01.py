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
    up_instructions = data.count('(')
    down_instructions = data.count(')')
    final_floor = (up_instructions-down_instructions)
    print (f'You end on floor {final_floor}')

solve()
# You end on floor 74