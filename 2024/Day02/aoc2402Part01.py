# Adjust Import Paths
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
# Import Utilities
from utils.ParseTXTAsIntArr import parse_txt_return_int_arr

# Substitue test/real to switch inputs
data_set = 'real'
data = parse_txt_return_int_arr(f'{data_set}_input.txt')
# Puzzle

def is_safe(array):
    # Is all Increasing or all Decreasing
    if array not in [sorted(array),sorted(array,reverse=True)]:
        return False
    # No Repeat Letters
    if len([x for x in array if array.count(x)==1]) != len(array):
        return False
    # Change is by 3 or less
    return all(abs(array[i] - array[i - 1]) <= 3 for i in range(1, len(array)))

def solve():
    safe_reports = [report for report in data if is_safe(report)]
    print (f'Safe Reports: {len(safe_reports)}')
        
    
solve()



