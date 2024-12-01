# Adjust Import Paths
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
# Import Utilities
from utils.ParseTXTAsList import Parse_Txt_as_List

# Substitue test/real to switch inputs
data_set = 'real'
data = Parse_Txt_as_List(f'{data_set}_input.txt')

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


