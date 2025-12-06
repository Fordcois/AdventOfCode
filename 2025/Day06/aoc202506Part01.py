import sys
import os
import math
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')
data = [ [y for y in x.split()] for x in data]

# Puzzle
def solve():

    total = 0
    row_num = len(data)
    col_num= (len(data[0]))
    operation = {'+':sum,'*':math.prod}
    
    for c in range(col_num):
        line =[]
        for r in range(row_num):
            char = data[r][c]
            if char.isdigit():
                char = int(char)
            line.append(char)
        total+=operation[line[-1]](line[:-1])
    return total

solve()
    

print (f'The Answer is: {solve()}')