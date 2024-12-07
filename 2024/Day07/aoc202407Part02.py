# Adjust Import Paths
import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
# Import Utilities
from utils.ParseTXTAsList import Parse_Txt_as_List
import itertools


# Substitue test/real to switch inputs
data_set = 'test'
data = Parse_Txt_as_List(f'{data_set}_input.txt')

# Clean Data 
formatted_data = [(int(split_line[0]), [int(x) for x in split_line[1].strip().split()]) for split_line in (line.split(':') for line in data)]

def add (a,b):
    return a+b

def multiply (a,b):
    return a*b

def concatenate(a,b):
    return (int(str(a)+(str(b))))


# Take number list and list of operators and intersect them:
def calculate_math(numbers,operators):

    output=numbers[0]
    number_index=1
    operator_index=0
    while number_index < len(numbers):
        if operators[operator_index] == '+':
            output = add(output,numbers[number_index])
        if operators[operator_index] == '*':
            output = multiply(output,numbers[number_index])
        if operators[operator_index] == '||':
            output = concatenate(output,numbers[number_index])
        number_index+=1
        operator_index+=1
    return output



# Puzzle
def solve():
    calibration_sum=0

    for line in formatted_data:
        target = line[0]
        number_list = line[1]
        variations = list(itertools.product(['+', '*','||'], repeat=len(number_list)-1))
        for variation in variations:
            if calculate_math(number_list,variation) == target:
                calibration_sum+=target
                break
    print (f'Calibration Number is: {calibration_sum}')


solve()
