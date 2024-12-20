import sys
import os
import re
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_str(f'{data_set}_input.txt')

# Initialise computer:
numbers= re.findall(r'\d+',data)
computer={'A':int(numbers.pop(0)),'B':int(numbers.pop(0)),'C':int(numbers.pop(0)) }
commands = [int(x) for x in numbers]

def get_combo_operand(input):
    if input <= 3:
        return input
    elif input == 4:
        return computer['A']
    elif input == 5:
        return computer['B']
    elif input == 6:
        return computer['C']
    elif input == 7:
        print ('Error! 7 will not appear in Valid Programs')
        pass

def move_pointer_to(new_index= None):
    global instruction_pointer 
    if new_index == None:
        instruction_pointer += 2
    else:
        instruction_pointer = new_index

#opcode 0
def adv (operand):
    # The adv instruction (opcode 0) performs division.
    # The numerator is the value in the A register. 
    numerator = computer['A']
    combo_operand = get_combo_operand(operand)
    # The denominator is found by raising 2 to the power of the instruction's combo operand. 
    denominator = 2 ** combo_operand
    # (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
    computer['A'] = int(numerator/denominator)
    # The result of the division operation is truncated to an integer and then written to the A register
    move_pointer_to()


# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
def bxl (operand):

    a = computer['B']
    computer['B'] = a ^ operand
    move_pointer_to()


# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
def bst(operand):
    computer['B'] = get_combo_operand(operand) % 8
    move_pointer_to()

def jnz (operand):
# The jnz instruction (opcode 3) does nothing if the A register is 0.
    if computer['A'] != 0:
        move_pointer_to(operand)
    else:
        move_pointer_to()
# if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand; 
# if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.


# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
def bxc(operand):
    a = computer['B']
    b = computer['C']
    computer['B'] = a ^ b
    move_pointer_to()

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
def out (operand):
    output = get_combo_operand(operand)%8
    move_pointer_to()
    return output
# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
def bdv (operand):
    numerator = computer['A']
    denominator = 2 ** get_combo_operand(operand)
    computer['B'] = int(numerator/denominator)
    move_pointer_to()

# The cdv instruction (opcode 7) works exactly like the adv instruction except that the result is stored in the C register. (The numerator is still read from the A register.)
def cdv (operand):
    numerator = computer['A']
    denominator = 2 ** get_combo_operand(operand)
    computer['C'] = int(numerator/denominator)
    move_pointer_to()


program = {0:adv,1:bxl,2:bst,3:jnz,4:bxc,5:out,6:bdv,7:cdv}
instruction_pointer=0

# Puzzle
def solve():
    output=[]
    while instruction_pointer < len(commands):
        opcode = commands[instruction_pointer]
        operand = commands[instruction_pointer+1]
        out = program[opcode](operand)
        if out != None:
            output.append(str(out))
    print (f'Output: {",".join(output)}')


solve()