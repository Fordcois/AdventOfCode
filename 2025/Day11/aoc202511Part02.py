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

map_dict={}
for line in data:
    split_line = line.split(':')
    k = split_line[0]

    v = [x.strip() for x in split_line[1].split(' ')][1:]
    map_dict[k]=v


@lru_cache(maxsize=None)
def move(start, dac_visited,fft_visisted):
    if start == 'out':
        if dac_visited and fft_visisted:
            return 1
        else:
            return 0
    if start == 'fft':
        fft_visisted = True
    if start == 'dac':
        dac_visited = True
    
    return sum([move(x,dac_visited,fft_visisted) for x in map_dict[start]])

def solve():
    return move('svr',False,False)

print(f'The Answer is {solve()}')

