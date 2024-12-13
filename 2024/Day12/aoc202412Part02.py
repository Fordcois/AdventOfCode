import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_of_str_arrays import file_as_list_of_string_arrays
from utilities.get_from_grid import grid_get

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_string_arrays(f'{data_set}_input.txt')

def scan_island(map_grid, target_char, y, x, visited=None):
    if visited is None:
        visited = set()
    if (y, x) in visited or grid_get(map_grid, x, y, '.') != target_char:
        return []
    visited.add((y, x))
    island_coords = [(y, x)]
    directions = [(y-1, x), (y, x+1), (y+1, x), (y, x-1)]
    for dy, dx in directions:
        additional_coords = scan_island(map_grid, target_char, dy, dx, visited)
        island_coords.extend(additional_coords)
    return island_coords

def find_all_islands(map_grid):
    islands = {}
    visited = set()
    for y in range(len(map_grid)):
        for x in range(len(map_grid[0])):
            if (y, x) in visited:
                continue
            current_char = map_grid[y][x]
            island = scan_island(map_grid, current_char, y, x, visited)
        
            if island:
                if current_char not in islands:
                    islands[current_char] = []
                islands[current_char].append(island)
    
    return islands

def count_corners(island_set):
    corner_count = 0
    for coord in island_set:
        y, x = coord[0], coord[1]

        north = (y - 1, x)
        north_east = (y - 1, x + 1)
        east = (y, x + 1)
        south_east = (y + 1, x + 1)
        south = (y + 1, x)
        south_west = (y + 1, x - 1)
        west = (y, x - 1)
        north_west = (y - 1, x - 1)
        # Outside Curve Corners
        if (north not in island_set) and (east not in island_set):
            corner_count += 1
        if (east not in island_set) and (south not in island_set):
            corner_count += 1
        if (south not in island_set) and (west not in island_set):
            corner_count += 1
        if (west not in island_set) and (north not in island_set):
            corner_count += 1

        # Inside Curve Corners
        if (north_west not in island_set) and (north in island_set) and (west in island_set):
            corner_count += 1
        if (north_east not in island_set) and (north in island_set) and (east in island_set):
            corner_count += 1
        if (south_east not in island_set) and (south in island_set) and (east in island_set):
            corner_count += 1
        if (south_west not in island_set) and (south in island_set) and (west in island_set):
            corner_count += 1
    return corner_count

def solve():
    total_cost=0
    result = find_all_islands(data)
    for char, islands in result.items():
        for island in islands:
            total_cost += len(island) * count_corners(island)

    print (f'The Final Cost would be: {total_cost}')

solve()





