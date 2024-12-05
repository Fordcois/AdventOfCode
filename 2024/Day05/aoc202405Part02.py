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
        
def find_fixed_middle_number(manual):
    relevant_rules = [rule for rule in instructions if (rule[0] in manual) and (rule[1] in manual)]
    for single_number in manual:
        numbers_to_go_before = [rule[0] for rule in relevant_rules if rule[1]==single_number]
        if len(numbers_to_go_before) == int(len(manual)/2):
            return single_number
    return


def solve():
    incorrect_manuals = [manual for manual in update_manuals if check_manual(manual)==False]
    total = sum([find_fixed_middle_number(x) for x in incorrect_manuals])
    print (f'The Total Number is: {total}')


solve()