import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

# Split Instructions into a tuple
instructions = [((instruction[0],int(instruction[1:]))) for instruction in data]

# Turn Function
def turn_dial(dial_value,direction):
    if direction == 'L':
        if dial_value == 0:
            return 99
        else: 
            return dial_value - 1
    if direction == 'R':
        if dial_value == 99:
            return 0
        else:
            return dial_value + 1
# Puzzle
def solve():
    dial = 50
    times_at_zero = 0
    for instruction in instructions:
        turn_dir = instruction[0]
        turn_num = instruction[1]
        for i in range (turn_num):
            dial = turn_dial(dial,turn_dir)
        if dial == 0:
                times_at_zero += 1
    print (f'The Real password is {times_at_zero}')

solve()