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
from utils.ParseTXTAsList import Parse_Txt_as_List

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