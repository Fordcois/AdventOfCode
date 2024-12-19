import sys
import os
import heapq
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_of_str_arrays import file_as_list_of_string_arrays

# Substitue test/real to switch inputs
data_set = 'real'
world_map = file_as_list_of_string_arrays(f'{data_set}_input.txt')

# Direction vectors
directions = {'North': (-1, 0),'South': (1, 0),'West': (0, -1),'East': (0, 1)}

def get_neighbors(world_map, location):
    neighbors = []
    for direction, (dict_y, dict_x) in directions.items():
        new_y, new_x = location[0] + dict_y, location[1] + dict_x
        if world_map[new_y][new_x] != '#':
            neighbors.append((direction, (new_y, new_x)))
    return neighbors

def calculate_turn_cost(current_direction, new_direction):
    if current_direction != new_direction:
        return 1000
    return 0

def dijkstra(world_map, start, end):
    min_cost = float('inf')
    best_paths = []

    priority_q = [(0, start, 'East', [(start, 'East')])]
    visited = set()

    while priority_q:
        current_cost, current_loc, current_direction, current_path = heapq.heappop(priority_q)

        current_state = (current_loc, current_direction)
        
        # Skip if this state has been visited
        if current_state in visited:
            continue
    
        visited.add(current_state)
        
        # Reached the end
        if current_loc == end:
            # If this is a new minimum cost path
            if current_cost < min_cost:
                min_cost = current_cost
                best_paths = [current_path]
            # If this path matches the current minimum cost
            elif current_cost == min_cost:
                best_paths.append(current_path)
            break
        
        # Explore neighbors
        for new_direction, neighbor_loc in get_neighbors(world_map, current_loc):
            # Calculate turn cost

            # Total cost includes turn cost
            new_cost = current_cost + 1 
            if current_direction != new_direction:
                new_cost += 1000

            # Copy and extend the path
            new_path = current_path + [(neighbor_loc, new_direction)]
            # Push to priority queue
            heapq.heappush(priority_q, (new_cost, neighbor_loc, new_direction, new_path))
    
    return min_cost


def solve():
    start_loc = (len(world_map)-2,1)
    end_loc = (1, len(world_map) - 2)
    cost = dijkstra(world_map, start_loc, end_loc)
    print(f"Minimum cost path: {cost}")
solve()

