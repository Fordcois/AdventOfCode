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

machines={}

regex_pattern= '[0-9]+'
for i in range(0,len(data),4):
    ButtonA = re.findall(regex_pattern,data[i])
    ButtonB = re.findall(regex_pattern,data[i+1])
    prize = re.findall(regex_pattern,data[i+2])
    machines[i] = {
        "A": {"x": int(ButtonA[0]), "y": int(ButtonA[1])},
        "B": {"x": int(ButtonB[0]), "y": int(ButtonB[1])},
        "prize": {"x": int(prize[0]), "y": int(prize[1])} 
    }

def win_prize(machine_num):
    p_x,p_y = machines[machine_num]['prize']['x']+10000000000000,machines[machine_num]['prize']['y']+10000000000000
    a_x,a_y = machines[machine_num]['A']['x'],machines[machine_num]['A']['y']
    b_x,b_y = machines[machine_num]['B']['x'],machines[machine_num]['B']['y']

    A = (p_x*b_y - p_y*b_x) / (a_x*b_y - a_y*b_x)
    B = (a_x*p_y - a_y*p_x) / (a_x*b_y - a_y*b_x)
    
    def is_int(number):
        return number % 1 == 0
    
    if is_int(A) and is_int(B):
        tokens_spent = int((A*3)+B)
    else:
        tokens_spent = 0

    return tokens_spent



            
def solve():
    tokens_spent=0
    for machine in machines:
        tokens_spent += win_prize(machine)
    print (f'You can win all the prizes with {tokens_spent} tokens')


solve()

