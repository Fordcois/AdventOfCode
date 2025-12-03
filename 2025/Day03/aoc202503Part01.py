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
    tens,single = 0,0
    # Find first large number
    for index,number in enumerate(int_arr[:-1]):
        if number > tens:
            tens = number
            tens_index = index
    # Find the second largest number
    for number in int_arr[tens_index+1:]:
        if number > single:
            single = number

    return (tens*10) + single

def solve():
    total_joltage = sum(find_joltage(bank) for bank in data)
    print (f'Total Joltage is: {total_joltage}')
    return total_joltage

solve()