# Adjust Import Paths
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_array_array import read_file_as_array_array

# Substitue test/real to switch inputs
data_set = 'test'
data = read_file_as_array_array(f'{data_set}_input.txt')

# Puzzle
def solve():
    target_word ='MAS'
    words_found = 0

    for y_index,line in enumerate(data):
        for x_index,character in enumerate(line):
            if data[y_index][x_index]=='X':
                
                right_in_bounds = (x_index+3) < len(line)
                left_in_bounds = (x_index-3) >= 0
                top_in_bounds = (y_index - 3) >= 0
                bottom_in_bounds = (y_index + 3) < len(data)

                # Horizontal - →
                if right_in_bounds:
                    if (data[y_index][x_index+1])+(data[y_index][x_index+2])+(data[y_index][x_index+3]) == target_word:
                        words_found+=1

                # Horizontal - ←
                if left_in_bounds:
                    if (data[y_index][x_index-1])+(data[y_index][x_index-2])+(data[y_index][x_index-3]) == target_word:
                        words_found+=1

                # Vertical - ↑
                if top_in_bounds:
                    if (data[y_index-1][x_index])+(data[y_index-2][x_index])+(data[y_index-3][x_index]) == target_word:
                        words_found+=1

                # Vertical - ↓
                if bottom_in_bounds:
                    if (data[y_index+1][x_index])+(data[y_index+2][x_index])+(data[y_index+3][x_index]) == target_word:
                        words_found+=1
                
                # Horizontal - ↖
                if left_in_bounds and top_in_bounds:
                    if (data[y_index-1][x_index-1])+(data[y_index-2][x_index-2])+(data[y_index-3][x_index-3]) == target_word:
                        words_found+=1

                # Horizontal - ↗
                if right_in_bounds and top_in_bounds:
                    if (data[y_index-1][x_index+1])+(data[y_index-2][x_index+2])+(data[y_index-3][x_index+3]) == target_word:
                        words_found+=1
                
                # Horizontal - ↙
                if left_in_bounds and bottom_in_bounds:
                    if (data[y_index+1][x_index-1])+(data[y_index+2][x_index-2])+(data[y_index+3][x_index-3]) == target_word:
                        words_found+=1
            
                # Horizontal - ↘
                if right_in_bounds and bottom_in_bounds:
                    if (data[y_index+1][x_index+1])+(data[y_index+2][x_index+2])+(data[y_index+3][x_index+3]) == target_word:
                        words_found+=1

    print (f'Found {words_found} Words')


solve()