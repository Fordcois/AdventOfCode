import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings
from utilities.get_from_grid import grid_get
from utilities.visualise_grid import visualize_grid

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

map=[]
directions=''
robot_loc = None
# Parse Data into map Array, Direction String, and Find Robot
for y, line in enumerate(data):
    if any(char in line for char in ['#', '.', 'O', '@']):
        row = []
        for x, char in enumerate(line):
            if char == '@':
                robot_loc = [y, x]
                row.append('.')  # Replace robot with '.'
            else:
                row.append(char)
        map.append(row)
    elif any(char in line for char in ['v', '^', '>', '<']):
        directions += line

def move_robot(robot_coords,direction):
    global robot_loc
    y,x= robot_coords
    movement= {'v':[y+1,x], '^':[y-1,x], '>':[y,x+1], '<':[y,x-1]}    
    next_square = map[movement[direction][0]][movement[direction][1]]
    # If Free space move
    if next_square =='.':
        robot_loc = movement[direction]
    # If Wall don't move
    elif next_square == '#':
        return
    # If Box - Push!
    elif next_square == 'O':
        push_crate([y,x],direction)

def push_crate(starting_loc, direction):
    global map, robot_loc
    direction_params = {
        '>': {'stop': len(map[0]), 'increment': 1, 'axis': 'horizontal'},
        '<': {'stop': 0, 'increment': -1, 'axis': 'horizontal'},
        'v': {'stop': len(map), 'increment': 1, 'axis': 'vertical'},
        '^': {'stop': 0, 'increment': -1, 'axis': 'vertical'}
    }
    
    if direction_params[direction]['axis'] == 'horizontal':
        # Horizontal scan
        start = starting_loc[1]
        stop = direction_params[direction]['stop']
        step = direction_params[direction]['increment']
        crates_found = []
        can_push = False
        for i in range(start, stop, step):
            y, x = starting_loc[0], i
            square = grid_get(map,x,y,'#')
            if square == 'O':
                crates_found.append([y, x])
            if square == '.':
                if crates_found:
                    can_push = True
                    break
            if square == '#':
                break
        if can_push:
            for crate in crates_found:
                cy, cx = crate
                map[cy][cx] = '.'
            for crate in crates_found:
                cy, cx = crate
                map[cy][cx+step] = 'O'
            robot_loc = [starting_loc[0], starting_loc[1]+step]

    else: 
        # Vertical scan
        start = starting_loc[0]
        stop = direction_params[direction]['stop']
        step = direction_params[direction]['increment']
        crates_found = []
        can_push = False
        for i in range(start, stop, step):
            y, x = i, starting_loc[1]
            square = grid_get(map,x,y,'#')
            if square == 'O':
                crates_found.append([y, x])
            if square == '.':
                if crates_found:
                    can_push = True
                    break
            if square == '#':
                break
        if can_push:
            for crate in crates_found:
                cy, cx = crate
                map[cy][cx] = '.'
            for crate in crates_found:
                cy, cx = crate
                map[cy+step][cx] = 'O'
        
            robot_loc = [starting_loc[0]+step, starting_loc[1]]
    
def calculate_score():
    total=0
    for y,line in enumerate(map):
        for x,char in enumerate(line):
            if char == 'O':
                total += ((100 * y) + x)
    return total

def solve():
    for char in directions:
        move_robot(robot_loc,char)
    print (f'Total score is {calculate_score()}')

    

solve()