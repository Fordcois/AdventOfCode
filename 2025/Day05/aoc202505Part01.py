import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

for i,line in enumerate(data):
    if line == "":
        fresh_range = [[int(y) for y in x.split('-')] for x in data[:i]]
        ingredients_id = [int(x) for x in data[i+1:]]
        break

def within_range(number,range_arr):
    start,end = range_arr
    return start <= number <= end

# Puzzle
def solve():
    fresh_produce = 0
    for ingredident in ingredients_id:
        for range in fresh_range:
            if within_range(ingredident,range):
                fresh_produce += 1
                break

    return fresh_produce

print (f'The Answer is: {solve()}')