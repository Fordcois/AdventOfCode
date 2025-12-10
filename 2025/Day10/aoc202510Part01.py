import sys
import os
from itertools import combinations
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def convert_buttons_to_binary(arr,length):
    return (''.join(['1' if x in arr else  '0' for x in range(length) ]))

def parse_input_line(line):
            # Convert Lights to Binary Representation
        lights = ''.join(['0' if char == '.' else '1' for char in line.split(']')[0][1:]])
        split_by_space = line.split(' ')
        buttons = [convert_buttons_to_binary([int(x) for x in button[1:-1].split(',')], len(lights)) for button in split_by_space[1:-1]]
        joltage = [int(x) for x in split_by_space[-1][1:-1].split(',')]
        # print (f'''
        #        Lights: {lights}
        #        buttons: {buttons}
        #        joltage: {joltage}
        #        ''')
        return {'lights':lights,'buttons':buttons,'joltage':joltage}

input = [parse_input_line(line) for line in data]

def xor_buttons(button_combo):
    # No Buttons pressed
    if len(button_combo) == 0:
        return ''  
    result = '0' * len(button_combo[0])
    for button in button_combo:
        result = ''.join([str(int(a) ^ int(b)) for a, b in zip(result, button)])
    
    return result



def solve():
    total_presses=0
    for puzzle in input:
        combos = []
        for length in range(len(puzzle['buttons']) + 1): 
            for combo in combinations(puzzle['buttons'], length):
                combos.append(combo)
        for x in combos:
            button_presses = xor_buttons(x)
            if button_presses == puzzle['lights']:
                total_presses += len(x)
                break
    
    return total_presses

print(f'The Answer is {solve()}')


