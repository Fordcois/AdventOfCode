import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def find_joltage(bank):
    int_arr = [int(x) for x in bank]
    stack = []
    skips_allowed = len(bank) - 12
    
    for number in int_arr:
        while stack and number > stack[-1] and skips_allowed > 0:
            stack.pop()
            skips_allowed -= 1
        stack.append(number)
    joltage = int(''.join([str(x) for x in stack[:12]]))
    return joltage

def solve():
    total_joltage =  (sum([find_joltage(bank) for bank in data]))
    print (f'Total joltage is: {total_joltage}')
solve()