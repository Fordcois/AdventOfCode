import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')
instructions = [[y for y in x] for x in data]


keypad_dict={
    (0,0):'1',
    (0,1):'2',
    (0,2):'3',
    (1,0):'4',
    (1,1):'5',
    (1,2):'6',
    (2,0):'7',
    (2,1):'8',
    (2,2):'9',
}

def move_finger(starting_number,direction):
    y,x = int(starting_number[0]),int(starting_number[1])
    direction_modifier = {
        'U': (y-1,x),
        'D':( y+1,x),
        'R': (y,x+1),
        'L':( y,x-1)
    }
    attempted_button = direction_modifier[direction]
    valid_button = keypad_dict.get(attempted_button)
    if valid_button:
        return direction_modifier[direction]
    else:
        return starting_number


# Puzzle
def solve():
    button = (1,1)
    keycode=[]
    for commands in instructions:
        for command in commands:
            button = move_finger(button,command)
        keycode.append(keypad_dict[button])
    print (f"The Code is: {''.join(keycode)}")
    return


solve()