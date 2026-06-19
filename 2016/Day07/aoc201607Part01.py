import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def is_abba(four_letter_string):
    if len(set(four_letter_string)) != 1:
        if (four_letter_string[0] == four_letter_string[3]) and (four_letter_string[1] == four_letter_string[2]):
            return True
    return False

def supports_tls(ip_string):
    lp = 0
    rp = 4
    in_brackets = False
    contains_abba = False
    abba_in_brackets=False
    while rp <= len(ip_string):
        capture = ip_string[lp:rp]
        if capture[-1] == '[' and not in_brackets:
            in_brackets = True
        if capture[-1] == ']' and in_brackets:
            in_brackets = False
        if is_abba(capture):
            if in_brackets:
                abba_in_brackets = True
            else:
                contains_abba = True
        lp, rp = lp + 1, rp + 1
    if contains_abba and( not abba_in_brackets):
        return True
    else:
        return False



# Puzzle
def solve():
    print( len([ip for ip in data if supports_tls(ip)]))

solve()