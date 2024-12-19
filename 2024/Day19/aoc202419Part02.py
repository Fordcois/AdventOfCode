import sys
import os
from functools import lru_cache
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')


towels_list=[]
patterns=[]
# Parse Data
for line in data:
    if ',' in line:
        for towel in line.split(','):
            towels_list.append(towel.strip())
    elif line != '':
        patterns.append(line)

towels = tuple(towels_list)  

@lru_cache(maxsize=None)  
def count_matches(pattern, start_index= 0):
    if start_index == len(pattern):
        return 1
    if start_index > len(pattern):
        return 0
    total = 0
    # Try each towel 
    for towel in towels:
        if pattern.startswith(towel, start_index):
            total += count_matches(pattern, start_index + len(towel))
    
    return total

def solve():
    total_matches = 0
    for pattern in patterns:
        matches = count_matches(pattern)
        total_matches += matches

    
    print(f'There are {total_matches} combinations')
solve()