import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def has_three_vowels(input):
    total_vowels = 0
    for vowel in 'aeiou':
        total_vowels += input.count(vowel)
    return total_vowels >= 3

def has_double_letter(input):
    for i in range (len(input)-1):
        if input[i] == input[i+1]:
            return True
    return False

def no_forbidden_string(input):
    for string in ['ab','cd','pq','xy']:
        if string in input:
            return False
    return True

def nice_string(input):
    if has_three_vowels(input) and has_double_letter(input) and no_forbidden_string(input):
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
# 238 nice strings