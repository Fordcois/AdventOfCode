import sys
import os
from collections import deque

# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_of_str_arrays import file_as_list_of_string_arrays
from utilities.progress_reporter import ProgressChecker

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_string_arrays(f'{data_set}_input.txt')


def find_start_and_end(maze_grid):
    start = end = None
    for y, line in enumerate(maze_grid):
        for x, char in enumerate(line):
            if char == 'S':
                start = (y, x)
            elif char == 'E':
                end = (y, x)
            if start and end:
                return start, end
    return start, end


def solve_maze(maze_grid):
    start, end = find_start_and_end(maze_grid)
    queue = deque([(start, None, 0)])  # (position, last_visited, steps)
    visited = set()
    path = []

    while queue:
        current_pos, last_visited, steps = queue.popleft()
        y, x = current_pos

        if (y, x) in visited:
            continue

        visited.add((y, x))
        path.append((y, x))

        if maze_grid[y][x] == 'E':
            return path

        directions = [(y-1, x),(y, x+1),(y+1, x),(y, x-1)]

        for next_pos in directions:
            new_y, new_x = next_pos
            if (next_pos != last_visited and 
                maze_grid[new_y][new_x] != '#' and 
                next_pos not in visited):
                queue.append((next_pos, current_pos, steps + 1))

    return path


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def get_diamond_coordinates(center_x, center_y, radius=20):
    coords = []
    for y in range(-radius, radius + 1):
        for x in range(-radius, radius + 1):
            if abs(x) + abs(y) <= radius:
                coords.append((center_y + y, center_x + x))
    return coords


def is_shortcut(start_index, starting_point, path_array):
    y, x = starting_point
    shortcuts = []
    paths_to_check = get_diamond_coordinates(x, y)

    later_paths = [p for p in paths_to_check if p in path_array and path_array.index(p) > start_index]

    for path in later_paths:
        direct_distance = manhattan_distance(starting_point, path)
        path_distance = path_array.index(path) - start_index

        steps_saved = path_distance - direct_distance
        shortcuts.append(steps_saved)

    return shortcuts if shortcuts else False


def solve():
    path_array = solve_maze(data)
    shortcut_dict = {}
    shortcuts_over_100 = 0
    progress = ProgressChecker(len(path_array))

    for path_index, tile in enumerate(path_array):
        progress.update_progress()
        shortcut = is_shortcut(path_index, tile, path_array)
        if shortcut:
            for steps_saved in shortcut:
                if steps_saved >= 100:
                    if steps_saved in shortcut_dict:
                        shortcut_dict[steps_saved] += 1
                    else:
                        shortcut_dict[steps_saved] = 1
                    shortcuts_over_100 += 1

    print(f'There are {shortcuts_over_100} shortcuts over 100 steps')


solve()