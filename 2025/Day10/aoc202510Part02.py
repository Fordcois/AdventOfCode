import sys
import os
from itertools import combinations
import pulp
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'test'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def parse_input_line(line):
        split_by_space = line.split(' ')
        buttons = [[int(x) for x in button[1:-1].split(',')]for button in split_by_space[1:-1]]
        joltage = [int(x) for x in split_by_space[-1][1:-1].split(',')]
        return {'buttons':buttons,'joltage':joltage}

input = [parse_input_line(line) for line in data]

def solve():
    total_presses = 0
    for puzzle in input:
        problem = pulp.LpProblem("model", pulp.LpMinimize)
        x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(puzzle['buttons']))]
        targets = puzzle['joltage']
        for counter_index, target in enumerate(targets):
            problem += (pulp.lpSum(x[button_index]for button_index, joltage in enumerate(puzzle['buttons'])if counter_index in joltage) == target)
            problem += pulp.lpSum(x)
            problem.solve()
        total_presses += sum(pulp.value(v) for v in x)

    return total_presses

print(f'The answer is {solve()}')


