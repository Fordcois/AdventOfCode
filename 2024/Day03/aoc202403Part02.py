# Adjust Import Paths
import sys
import os
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str

# Substitue test/real to switch inputs
data_set = 'test'
data = file_as_str(f'{data_set}_input.txt')

# Puzzle
def solve():
    total = 0
    matches = re.findall("mul\(([0-9]+),([0-9]+)\)|(don't\(\))|(do\(\))", data) 

    recording=True

    for match in matches:
        # Turn off recording
        if match == ('', '', "don't()", ''):
            recording = False
        # Turn on Recording
        if match == ('', '', '', 'do()'):
            recording = True
        # if Num and recording
        elif recording == True:
            total += (int(match[0]) * int(match[1]))

    print(f'The Total is: {total}')

solve()


