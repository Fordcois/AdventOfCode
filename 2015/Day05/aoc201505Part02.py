import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def pair_without_overlap(input):
    for i in range(len(input) - 1):
        pair = input[i:i+2]
        if pair in input[:i] or pair in input[i+2:]:
            return True
    return False

def repeat_with_letter_inbetween(input):
    for i in range (len(input)-2):
        if input[i] == input[i+2]:
            return True
    return False

def nice_string(input):
    if pair_without_overlap(input) and repeat_with_letter_inbetween(input):
        return True
    else :
        return False

# Puzzle
def solve():
    nice_count = 0
    for string in data:
        if nice_string(string):
            nice_count += 1
    print (f'{nice_count} nice strings')

solve()
# 69 nice strings



