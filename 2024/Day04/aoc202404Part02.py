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
    x_mas_found=0

    for y_index,line in enumerate(data):
        for x_index,character in enumerate(line):

            if ((x_index+2 <len(line)) and y_index+2 < len(data)) and (data[y_index+1][x_index+1] =='A'):
                top_line = data[y_index][x_index] + data[y_index][x_index+2]
                bottom_line = data[y_index+2][x_index] + data[y_index+2][x_index+2]

                # ↘↗
                if (top_line == "MS") and (bottom_line =='MS'):
                    x_mas_found += 1
                # ↘↙ 
                if (top_line == "MM") and (bottom_line =='SS'):
                    x_mas_found += 1
                # ↖↗
                if (top_line == "SS") and (bottom_line =='MM'):
                    x_mas_found += 1
                # ↖↙ 
                if (top_line == "SM") and (bottom_line =='SM'):
                    x_mas_found += 1

    print (f'Found {x_mas_found} Words')

solve()