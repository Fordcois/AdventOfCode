import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_of_str_arrays import file_as_list_of_string_arrays
from utilities.visualise_grid import visualize_grid
from utilities.progress_reporter import ProgressChecker

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_string_arrays(f'{data_set}_input.txt')


def find_start_and_end(maze_grid):
    start = end = None
    for y,line in enumerate(maze_grid):
        for x,char in enumerate(line):
            if char == 'S':
                start = (y,x)
            elif char == 'E':
                end = (y,x)
            if start and end:
                return start, end
    return start, end
            
    

def take_step(maze_grid,last_visited,current_place):
    y,x = current_place
    if maze_grid[y][x] == 'E':
        return True
    directions = [[y-1,x],[y,x+1],[y+1,x],[y,x-1]]
    for next_step in directions:
        if next_step != last_visited and maze_grid[next_step[0]][next_step[1]]!='#':
            return next_step

def solve_maze(maze_grid):
    steps = 0
    start,end = find_start_and_end(maze_grid)
    mazed_solved = False
    current_place = start
    last_visited = None  
    path_taken = [[start[0],start[1]]]

    while not mazed_solved:
        next_step = take_step(maze_grid, last_visited, current_place)
        last_visited = current_place 
        current_place = next_step
        if next_step != True:
            current_place = next_step
            path_taken.append(next_step)
            steps += 1
        else:
            path_taken.append(end)
            mazed_solved = True
    return path_taken


def is_shortcut(start_index,starting_point,path_array):
    y,x = starting_point
    directions = {  'N':{'end':[y-2,x],'wall':[y-1,x]},
                    'E':{'end':[y,x+2],'wall':[y,x+1]},
                    'S':{'end':[y+2,x],'wall':[y+1,x]},
                    'W':{'end':[y,x-2],'wall':[y,x-1]}
                }
    shortcuts = []
    for direction in directions:
        if (directions[direction]['end'] in path_array) and (directions[direction]['wall'] not in path_array):
            end_index = path_array.index(directions[direction]['end'])
            if end_index > start_index:
                shortcuts.append((end_index - start_index) - 2)
    return shortcuts if shortcuts else False


    





# Puzzle
def solve():
    path_array = solve_maze(data)
    shortcuts_over_100 = 0

    for path_index,tile in enumerate(path_array):
        shortcut = is_shortcut(path_index,tile,path_array)
        if shortcut:
            for steps_saved in shortcut:
                if steps_saved >= 100:
                    shortcuts_over_100 += 1
    print (f'There are {shortcuts_over_100} shortcuts over 100 steps')


solve()