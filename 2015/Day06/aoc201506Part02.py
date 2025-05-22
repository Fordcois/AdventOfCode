import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def coord_to_tuple(coord_string):
    split = coord_string.split(',')
    return ((int(split[0])),int(split[1]))

def list_of_impacted_squares(tuple_one,tuple2):
    a_y,a_x = tuple_one
    b_y,b_x = tuple2
    output=[]
    for y in range ((b_y-a_y)+1):
        for x in range ((b_x-a_x)+1):
            output.append([(a_y + y),(a_x + x)])
    return output

def get_instructions():
    cleaned_instructions = []
    for line in data:
        clean_instruction = []
        instruction = (line.split(' '))
        # If off or on
        if instruction[1] in ['on','off']:
            clean_instruction.append(instruction[1])
        else:
            clean_instruction.append(instruction[0])
        clean_instruction.append(coord_to_tuple(instruction[-3]))
        clean_instruction.append(coord_to_tuple(instruction[-1]))
        cleaned_instructions.append(clean_instruction)
    return cleaned_instructions
        
on_lights = {}

def process_instruction(instruction, start_tuple, end_tuple):
    for coord in list_of_impacted_squares(start_tuple, end_tuple):
        coord_tuple = tuple(coord)
        if instruction == 'on':
            if coord_tuple not in on_lights:
                on_lights[coord_tuple] = 1
            else:
                on_lights[coord_tuple] += 1
        elif instruction == 'off':
            
            if coord_tuple in on_lights and on_lights[coord_tuple] >= 2:
                on_lights[coord_tuple] -= 1
            else:
                if coord_tuple in on_lights:
                    del on_lights[coord_tuple]


        elif instruction == 'toggle':
            if coord_tuple not in on_lights:
                on_lights[coord_tuple] = 2
            else:
                on_lights[coord_tuple] += 2

# Puzzle
def solve():
    instructions = get_instructions()
    for line in instructions:
        process_instruction(*line)
    print (f'Total brightness is {sum(on_lights.values())}')

solve()
# Total brightness is 14687245
