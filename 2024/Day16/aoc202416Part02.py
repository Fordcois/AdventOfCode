import sys
import os
import heapq
from collections import defaultdict

# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_of_str_arrays import file_as_list_of_string_arrays

# Substitute test/real to switch inputs
data_set = 'real'
world_map = file_as_list_of_string_arrays(f'{data_set}_input.txt')

directions = {'North': (-1, 0),'South': (1, 0),'West': (0, -1),'East': (0, 1)}

def get_neighbors(world_map, location):
    neighbors = []
    for direction, (dir_y, dir_x) in directions.items():
        new_y, new_x = location[0] + dir_y, location[1] + dir_x
        if world_map[new_y][new_x] !='#':
            neighbors.append((new_y, new_x, direction))
    return neighbors

def find_all_paths(world_map, source, target):
    best_costs = {}
    links = defaultdict(set)
    # Cost - position - direction - previous
    priority_q = [(0, source, 'East', None)]  
    while priority_q:
        cost, pos, direction, prev = heapq.heappop(priority_q)
        state = (pos,direction)
        if state in best_costs:
            if cost == best_costs[state]:
                links[state].add(prev)
            continue
        
        best_costs[state] = cost
        links[state].add(prev)

        prev = (pos, direction)

        for new_pos_y, new_pos_x, new_direction in get_neighbors(world_map, pos):  
            new_pos = (new_pos_y,new_pos_x)
            new_cost = cost + 1 
            if direction != new_direction:
                new_cost += 1000
            heapq.heappush(priority_q,(new_cost, new_pos, new_direction, prev))



    # Backwards recording every tiles
    routes, tiles = set() , set()
    def walk(cur):
        if cur and cur not in routes:
            routes.add(cur)
            tiles.add(cur[0])
            for npos in links[cur]: walk(npos)
    for direction in directions:
        walk((target, direction))
    return len(tiles)

def solve():
    start_loc = (len(world_map)-2,1)
    end_loc = (1, len(world_map) - 2)

    unique_tiles = find_all_paths(world_map, start_loc, end_loc)
    
    print(f"Total locations covered: {unique_tiles}")

solve()