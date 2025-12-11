import sys
import os
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

def move(start):
    if start == 'out':
        return 1
    else:
        return (sum([move(x) for x in map_dict[start]]))

# Puzzle
def solve():
    return move('you')


print(f'The Answer is {solve()}')