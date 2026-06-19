import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def is_aba(three_letter_string):
    if len(set(three_letter_string)) != 1:
        return three_letter_string[0] == three_letter_string[2]
    
def matching_bab(aba):
    return (f"{aba[1]}{aba[0]}{aba[1]}")

def supports_tls(ip_string):
    lp = 0
    rp = 3
    in_brackets = False
    found_abas=[]
    found_babs=[]
    while rp <= len(ip_string):
        capture = ip_string[lp:rp]
        if capture[-1] == '[' and not in_brackets:
            in_brackets = True
        if capture[-1] == ']' and in_brackets:
            in_brackets = False
        if is_aba(capture):
            if in_brackets:
                found_babs.append(matching_bab(capture))
            else:
                found_abas.append(capture)
        lp, rp = lp + 1, rp + 1
    if len([x for x in found_abas if x in found_babs]) > 0:
        return True
    return False



# Puzzle
def solve():
    print( len([ip for ip in data if supports_tls(ip)]))

solve()