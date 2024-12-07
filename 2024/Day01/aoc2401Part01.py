# Adjust Import Paths
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'test'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def solve():
    total_difference = 0
    list_a = []
    list_b = []
    for line in data:
        line_numbers = [int(x) for x in line.split('   ')]
        list_a.append(line_numbers[0])
        list_b.append(line_numbers[1])

    list_a.sort()
    list_b.sort()

    for i in range (len(list_a)):
        total_difference += abs(list_a[i]-list_b[i])
    
    print (f'Total Difference is: {total_difference}')

solve()


