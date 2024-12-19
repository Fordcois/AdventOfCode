import sys
import os
import heapq
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings
from utilities.visualise_grid import visualize_grid
from utilities.get_from_grid import grid_get

# Substitue test/real to switch inputs
data_set = 'test'
data = file_as_list_of_strings(f'{data_set}_input.txt')

bytes = [(int(x[0]),int(x[1])) for x in [y.split(',') for y in data]]

grid_size = 71
world_map=[]
for i in range(grid_size):
    world_map.append(['.']*grid_size)


# Direction vectors
directions = {'North': (-1, 0),'South': (1, 0),'West': (0, -1),'East': (0, 1)}

def get_neighbors(world_map, location):
    """Get valid neighboring cells from the current location"""
    neighbors = []
    for direction, (dy, dx) in directions.items():
        ny, nx = location[0] + dy, location[1] + dx
        if grid_get(world_map,nx,ny,'#') != '#':
            neighbors.append((direction, (ny, nx)))
    return neighbors

def calculate_turn_cost(current_direction, new_direction):
    """Calculate the cost of turning between directions"""
    # Orthogonal turns cost 1000
    if current_direction != new_direction:
        return 1000
    return 0

def dijkstra(world_map, start, end):
    """Dijkstra's algorithm with directional movement costs, returning all best paths"""
    min_cost = float('inf')
    best_paths = []

    pq = [(0, start, 'East', [(start, 'East')])]
    visited = set()

    while pq:
        current_cost, current_loc, current_direction, current_path = heapq.heappop(pq)
        
        # Create a unique state key
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
            # Total cost includes step cost (1) and potential turn cost
            new_cost = current_cost + 1 
            # Copy and extend the path
            new_path = current_path + [(neighbor_loc, new_direction)]
            # Push to priority queue
            heapq.heappush(pq, (new_cost, neighbor_loc, new_direction, new_path))
    if best_paths:
        return len(best_paths)
    return None


def solve():
    start_loc = (len(world_map)-2,1)
    end_loc = (1, len(world_map) - 2)
    cost = dijkstra(world_map, start_loc, end_loc)
    print(f"Minimum cost path: {cost}")
solve()


# Puzzle
def solve():
    print (world_map)
    for i in range (1024):
        x,y = bytes[i]
        world_map[y][x] = '#'

    visualize_grid(world_map,True,['#'])
    start_loc = (0,0)
    end_loc = (70,70)
    cost = dijkstra(world_map, start_loc, end_loc)
    print(f"Minimum cost path: {cost}")

solve()