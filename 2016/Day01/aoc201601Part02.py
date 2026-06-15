import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_str(f'{data_set}_input.txt')

instructions = [[instruction[0],int(instruction[1:])] for instruction in [char.strip() for char in data.split(',')]]

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

def take_step(starting_loc:tuple,direction) -> tuple:
    x,y = starting_loc
    if direction =='NORTH':
        y += 1
    if direction =='SOUTH':
        y -= 1
    if direction == 'EAST':
        x += 1
    if direction == 'WEST':
        x -= 1
    return x,y

# Puzzle
def solve():
    x,y = 0,0
    visited_locations=set()
    facing='NORTH'
    for direction,steps in instructions:
        facing=new_direction[facing][direction]
        for i in range (steps):
            x,y = take_step((x,y),facing)

            if (x,y) in visited_locations:
                return (abs(y)+abs(x))
            else:
                visited_locations.add((x,y))

    print (visited_locations)


print (solve())