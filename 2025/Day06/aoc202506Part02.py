import sys
import os
import math
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Substitue test/real to switch inputs
data_set = 'real'
with open(f'{data_set}_input.txt', 'r') as file:
    data = [line[:-1] for line in file]

# Find where the colums are
def find_column_indexes(arr):
    num_rows = len(arr)
    break_columns = []
    for i in range(len(arr[0])):
        if all(arr[row][i] == ' ' for row in range(num_rows)):
            break_columns.append(i)
    return break_columns

def split_at_indexes(str, col_indexes):
    output_arr =[]
    current_str=''
    for i in range(len(str)):
        if i not in col_indexes:
            current_str += str[i]
        else:
            output_arr.append(current_str)
            current_str=''
    output_arr.append(current_str)
    return output_arr

def transpose_grid(grid):
    output_arr = []
    row_num = len(grid)
    col_num= (len(grid[0]))
    
    for c in range(col_num):
        line =[]
        for r in range(row_num):
            char = grid[r][c]
            line.append(char)
        output_arr.append(line)

    return output_arr

def get_ceph_numbers(arr):
    numbers = arr[:-1]
    digits=max([len(x) for x in numbers])
    columns = len(numbers)
    output=[]
    for x in range(digits):
        str=''
        for y in range(columns):
            str+=arr[y][x]
        output.append(int(str))
    return output

# Puzzle
def solve():
    operation = {'+':sum,'*':math.prod}
    breaks = find_column_indexes(data)
    numbers = [split_at_indexes(x,breaks) for x in data]
    arrs = transpose_grid(numbers)
    
    return sum(operation[x[-1].strip()](get_ceph_numbers(x)) for x in arrs)

print (f'The Answer is: {solve()}')