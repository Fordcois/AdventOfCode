import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_str(f'{data_set}_input.txt')

instructions = [[str[0],int(str[1:])] for str in [char.strip() for char in data.split(',')]]

new_direction={
    'NORTH':
        {'L':'WEST',
        'R':'EAST'},
    'EAST':
        {'L':'NORTH',
        'R':'SOUTH'},
    'SOUTH':
        {'L':'EAST',
        'R':'WEST'},
    'WEST':
        {'L':'SOUTH',
        'R':'NORTH'},
}

# Puzzle
def solve():
    x,y = 0,0
    facing='NORTH'
    for direction,steps in instructions:
        facing=new_direction[facing][direction]
    
        if facing =='NORTH':
            y += steps
        if facing =='SOUTH':
            y -= steps
        if facing == 'EAST':
            x += steps
        if facing == 'WEST':
            x -= steps
        print (f'x: {x} - y:{y}')

    return (abs(y)+abs(x))

print (solve())