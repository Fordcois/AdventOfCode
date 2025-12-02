import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_str(f'{data_set}_input.txt')

# Split Inputs into list
scales = [tuple(map(int, r.split('-'))) for r in data.split(',')]

def is_invalid_id(number):
    str_pass=str(number)
    id_length = len(str_pass)
    first_half = str_pass[:id_length//2]
    second_half = str_pass[id_length//2:]
    if first_half == second_half:
        return True
# Puzzle
def solve():
    invalid_id_total = 0
    for scale in scales:
        for i in range(scale[0],scale[1]+1):
            if is_invalid_id(i):
                invalid_id_total += i

    print (f'Total of invalid Ids: {invalid_id_total}')
    return

solve()