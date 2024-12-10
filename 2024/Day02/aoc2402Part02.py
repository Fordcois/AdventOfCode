# Adjust Import Paths
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_list_of_ints import file_as_list_of_ints

# Substitue test/real to switch inputs
data_set = 'test'
data = file_as_list_of_ints(f'{data_set}_input.txt')

# Puzzle
def is_safe(array):
    # Is all increasing or all decreasing
    if array not in [sorted(array),sorted(array,reverse=True)]:
        return False
    # No repeat letters
    if len([x for x in array if array.count(x)==1]) != len(array):
        return False
    # Change is by 3 or less
    return all(abs(array[i] - array[i - 1]) <= 3 for i in range(1, len(array)))

def single_bad_level(array):
    for i in range (len(array)):
        if is_safe(array[:i] + array[i+1:]): 
            return True
    return False

def solve():
    # Filter out Safe Reports
    safe_reports = [report for report in data if is_safe(report)]
    unsafe_reports = [report for report in data if not is_safe(report)]
    # Check unsafe Reports Again
    safe_reports += [recheck_report for recheck_report in unsafe_reports if single_bad_level(recheck_report)]
    print (f'Safe Reports: {len(safe_reports)}')

solve()




