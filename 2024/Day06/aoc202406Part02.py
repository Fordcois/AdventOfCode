# Adjust Import Paths
import sys
import os
import copy
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
# Import Utilities
from utils.ParseTXTAsListofLists import parse_Txt_as_list_of_lists

# Substitue test/real to switch inputs
data_set = 'real'
map = parse_Txt_as_list_of_lists(f'{data_set}_input.txt')

def visualise_grid(map, guardlocation, facing, visited_locations):
    guard = {'North':'↑', 'East':'→', 'South':'↓', 'West':'←'}
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if [y,x] == guardlocation:
                print(f"\033[32m{guard[facing]}\033[0m", end="") 
            elif [y,x] in visited_locations:
                print("\033[34m.\033[0m", end="")  
            elif char == '#':
                print("\033[31m#\033[0m", end="")  
            else:
                print(char, end="")
        print()
    print()

def find_guard_start(location):
    for y, line in enumerate(location):
        for x, char in enumerate(line):
            if char == '^':
                location[y][x]='.'
                return [y,x]
            
guard_starting_location=find_guard_start(map)
            
movement = {'North':[-1,0],'East':[0,1],'South':[+1,0],'West':[0,-1]}
turn = {'North':'East','East':'South','South':'West','West':'North'}


def find_visited_locations(map_array):
    guard_location = guard_starting_location
    visited_locations=[guard_location]
    guard_on_location = True
    guard_facing='North'
    while guard_on_location:
        potential_nextstep_coords = [guard_location[0]+movement[guard_facing][0], guard_location[1]+movement[guard_facing][1]]           
        if (0 <= potential_nextstep_coords[0] <= len(map[0])-1) and (0 <= potential_nextstep_coords[1] <= len(map)-1):
            infront_of_guard = map_array[potential_nextstep_coords[0]][potential_nextstep_coords[1]]
            if infront_of_guard == '.':
                guard_location = potential_nextstep_coords
                if potential_nextstep_coords not in visited_locations:
                    visited_locations.append(potential_nextstep_coords)
            elif infront_of_guard == '#':
                guard_facing = turn[guard_facing]
        else:
            return visited_locations

def map_is_loop(guard_start,map_array):
    guard_location=guard_start
    guard_on_location = True
    guard_facing='North'
    visited_locations_and_view=[guard_location,guard_facing]
    while guard_on_location:
        if [guard_location,guard_facing] in visited_locations_and_view:
            return True
        else:
            visited_locations_and_view.append([guard_location,guard_facing])
        potential_nextstep_coords = [guard_location[0]+movement[guard_facing][0], guard_location[1]+movement[guard_facing][1]]
        if (0 <= potential_nextstep_coords[0] <= len(map[0])-1) and (0 <= potential_nextstep_coords[1] <= len(map)-1):      
            infront_of_guard = map_array[potential_nextstep_coords[0]][potential_nextstep_coords[1]]
            if infront_of_guard == '.':
                guard_location = potential_nextstep_coords
            elif infront_of_guard == '#':
                guard_facing = turn[guard_facing]
        else:
            guard_on_location = False
            return False



        
def solve():

    guards_path=find_visited_locations(map)
    # checked=0
    # amount_to_check=len(guards_path)
    loops_possibilties_found=0
    for path_tile in guards_path[1:]:
        # checked += 1
        # print(f'{(checked / amount_to_check) * 100:.2f}% - {checked}/{amount_to_check}')
        map[path_tile[0]][path_tile[1]]='#'
        if map_is_loop(guard_starting_location,map):
            loops_possibilties_found += 1
        map[path_tile[0]][path_tile[1]]='.'
        
    print (f'You can place an object in {loops_possibilties_found} places to cause a loop')

solve()