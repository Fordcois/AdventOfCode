# Adjust Import Paths
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'test'
data = file_as_list_of_strings(f'{data_set}_input.txt')

# Puzzle
instructions=[[int(char) for char in line.split('|')] for line in data if '|' in line]
update_manuals=[[int(char) for char in line.split(',')] for line in data if ',' in line]

def check_manual(manual):
    for page in manual:
        instructions_to_check = [x for x in instructions if x[0] == page]
        page_index = manual.index(page)
        later_pages = manual[:page_index]
        
        for instruction in instructions_to_check:
            if later_pages.count(instruction[1]) > 0:
                return False
    return True
        
def get_middle_number(arr):
    return arr[(int(len(arr)/2))]

def solve():
    correct_manuals = [manual for manual in update_manuals if check_manual(manual)]
    print (f'The Total Number is: {sum( [get_middle_number(array) for array in correct_manuals] )}')

solve()