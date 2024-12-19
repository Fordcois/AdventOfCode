import sys
import os
import re
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

towels_list=[]
patterns=[]
# Parse Data
for line in data:
    if ',' in line:
        for towel in line.split(','):
            towels_list.append(towel.strip())
    elif line != '':
        patterns.append(line)

def solve():
    re_pattern = f"^({'|'.join(towels_list)})*$"
    possible_patterns = 0
    
    for pattern in patterns:
        if re.fullmatch(re_pattern,pattern):
            possible_patterns += 1
    
    print (f'{possible_patterns} Possible Paterns')

solve()

