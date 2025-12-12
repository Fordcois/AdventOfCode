import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

sizes = []
presents =[]
for i in range(0,29,5):
    line1,line2,line3 = data[i+1],data[i+2],data[i+3]
    presents.append([line1,line2,line3])
    sizes.append((line1 + line2 + line3).count('#'))

grid_data = data[30:]

def solve():
    possible = 0
    impossible = 0

    for row in grid_data:
        split_line = row.split(':')
        x_size,y_size =  int(split_line[0][:2]),int(split_line[0][3:])
        area = x_size*y_size
        requirements = [int(x) for x in split_line[1].split(' ')[1:]]
        minimum_space = sum([requirements[i]*sizes[i] for i in range(6)])
        
        # Easy fit
        if sum(requirements) * 9 <= area:
            possible += 1
            pass
        # Impossible
        if minimum_space > area:
            impossible += 1
        
    if impossible+possible == len(grid_data):
        return possible

print (f'The answer is {solve()}')