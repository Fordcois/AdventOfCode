# Adjust Import Paths
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
# Import Utilities
from utils.TxtAsSingleString import txt_as_single_string
import re

# Substitue test/real to switch inputs
data_set = 'real'
data = txt_as_single_string(f'{data_set}_input.txt')


# Puzzle
def solve():
    total = 0
    matches = re.findall("mul\(([0-9]+)\,([0-9]+)\)", data) 
    for match in matches:
        total += int(match[0]) * int(match[1])
    print (f'The Total is: {total}')

solve()