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

def is_invalid_id(int):
    string_num = str(int)
    length = len(string_num)
    for i in range(2,length+1):
        if length % i == 0:
            parts = [string_num[y:y + length // i] for y in range(0, length, length // i)]
            if len(set(parts)) == 1:
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