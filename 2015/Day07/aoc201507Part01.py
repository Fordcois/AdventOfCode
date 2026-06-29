import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

circuits={}
wire_values={}

def compute_outputs(input,operation_type):
    left = input[0]
    right = input[-1]

    if operation_type=='AND':
        return left & right
    if operation_type=='LSHIFT':
        return left << right
    if operation_type =='NOT':
        return (~left) & 0xFFFF
    if operation_type =='OR':
        return left | right
    if operation_type == 'RSHIFT':
        return left >> right
    if operation_type == 'SET':
        return left
    
def split_inputs(input, split_on):
    splits = [x.strip() for x in input.split(split_on)]
    if splits[0] == '':
        return [splits[1]]  
    else:
        return splits 

def parse_instructions():
    parsed_instructions = [[y.strip() for y in x.split('->')] for x in data]

    for wire in parsed_instructions:
        instruction,output = wire        
        if 'AND' in instruction:
            inputs = split_inputs(instruction,'AND')
            function='AND'
        elif 'LSHIFT' in instruction:
            inputs = split_inputs(instruction,'LSHIFT')
            function = 'LSHIFT'
        elif 'NOT' in instruction:
            inputs= split_inputs(instruction,'NOT')
            function = 'NOT'
        elif 'OR' in instruction:
            inputs= split_inputs(instruction,'OR')
            function = 'OR'
        elif 'RSHIFT' in instruction:
            inputs= split_inputs(instruction,'RSHIFT')
            function = 'RSHIFT'
        else:
            inputs=[instruction]
            function = 'SET'
        circuits[output]={
            'inputs':inputs,
            'function':function
        }

def get_answer(output):
    if output in wire_values:
        return wire_values[output]

    inputs, function = circuits[output].values()
    resolved_inputs = []

    for inp in inputs:
        if inp.isnumeric():
            value = int(inp)
        else:
            value = get_answer(inp)
            print(f"{inp} -> {value}")
        resolved_inputs.append(value)

    result = compute_outputs(resolved_inputs, function)
    print (f"result: {result}")
    wire_values[output] = result
    return result 


# Puzzle
def solve():
    parse_instructions()
    get_answer('a')
    return

solve()