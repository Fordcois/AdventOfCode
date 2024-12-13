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
    a_presses=[]
    b_presses=[]
    for i in range(1,101):
        a_presses.append((machines[machine_num]["A"]["x"]*i,machines[machine_num]["A"]["y"]*i))
        b_presses.append((machines[machine_num]["B"]["x"]*i,machines[machine_num]["B"]["y"]*i))
        
    for num_of_a_presses in range(len(a_presses)):
        for num_of_b_presses in range (len(b_presses)):
            
            result = tuple(x + y for x, y in zip(a_presses[num_of_a_presses],b_presses[num_of_b_presses]))
            if result == (machines[machine_num]["prize"]["x"],machines[machine_num]["prize"]["y"]):
                tokens_spent= ((num_of_a_presses +1) *3) + (num_of_b_presses+1)
                # print (f'You can win this machine {machine_num} with {tokens_spent} tokens')
                return tokens_spent
    return 0
            
def solve():
    tokens_spent=0
    for machine in machines:
        tokens_spent += win_prize(machine)
    print (f'You can win all the prizes with {tokens_spent} tokens')


solve()