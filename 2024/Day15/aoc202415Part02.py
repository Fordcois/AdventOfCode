import sys
import os
from copy import deepcopy
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings
from utilities.get_from_grid import grid_get
# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')


map=[]
directions=''
replacements={'#':['#',"#"],'O':["[","]"],'.':['.','.'],'@':['@','.']}
for y, line in enumerate(data):
    if any(char in line for char in ['#', '.', 'O', '@']):
        row = []
        for char in line:
            row.extend(replacements[char])
        map.append(row.copy())
    elif any(char in line for char in ['v', '^', '>', '<']):
        directions += line
    #Find and replace Robot
for y,line in enumerate(map):
    for x, char in enumerate(line):
        if char == '@':
            map[y][x] = '.'
            robot_loc=[y,x]

direction_params = {
        '>': {'steps': (0, 1),'axis': 'horizontal'},
        '<': {'steps': (0, -1),'axis': 'horizontal'},
        'v': {'steps': (1, 0), 'axis': 'vertical'},
        '^': {'steps': (-1, 0),'axis': 'vertical'}
    }

def robot_go(grid, moves, start):
    robot_y, robot_x = start
    move_successful = False
    for move in moves:
        new_y, new_x = robot_y + direction_params[move]['steps'][0], robot_x + direction_params[move]['steps'][1]
        if grid_get(map,new_x,new_y,'#') == '#':
            pass
        elif (
            grid_get(grid,new_x,new_y,'#') == '.' or
            (direction_params[move]['axis']=='horizontal' and robot_go(grid, [move], (new_y, new_x)))
        ):
            temp_store = grid[new_y][new_x]
            grid[new_y][new_x] = grid[robot_y][robot_x]  
            grid[robot_y][robot_x] = temp_store
            robot_y, robot_x = new_y, new_x
            move_successful = True
        elif direction_params[move]['axis']=='vertical':

            side_offeset = 1 if grid[new_y][new_x] == '[' else -1
            grid_copy = deepcopy(grid)
            left_moved = robot_go(grid_copy, [move], (new_y, new_x))
            right_moved = robot_go(grid_copy, [move], (new_y, new_x + side_offeset))

            if left_moved and right_moved:
                robot_go(grid, [move], (new_y, new_x))
                robot_go(grid, [move], (new_y, new_x + side_offeset))
                temp_store = grid[new_y][new_x]  
                grid[new_y][new_x] = grid[robot_y][robot_x] 
                grid[robot_y][robot_x] = temp_store
                
                robot_y, robot_x = new_y, new_x
                move_successful = True

    return move_successful

def calculate_score():
    total=0
    for y,line in enumerate(map):
        for x,char in enumerate(line):
            if char == '[':
                total += ((100 * y) + x)
    return total

def solve():
    robot_go(map,directions,robot_loc)
    print (f'Total score is {calculate_score()}')


solve()