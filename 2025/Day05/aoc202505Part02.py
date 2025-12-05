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
        break

def overlap_ranges (r1,r2):
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    if r1_end < r2_start or r1_start > r2_end:
        return False
    return True
    
def merge_ranges(r1, r2):
    r1_start, r1_end = r1
    r2_start, r2_end = r2
    
    new_start = min(r1_start, r2_start)
    new_end = max(r1_end, r2_end) 
    
    return [new_start,new_end]

def solve():

    r_lib = [fresh_range[0]]
    for r in fresh_range[1:]:
        i = 0
        while i < len(r_lib):
            if overlap_ranges(r, r_lib[i]):
                r = merge_ranges(r, r_lib[i])
                r_lib.pop(i)  
                i = 0         
            else:
                i += 1
        r_lib.append(r)

    return (sum([x[1]-x[0]+1 for x in r_lib]))

print (f'The Answer is: {solve()}')