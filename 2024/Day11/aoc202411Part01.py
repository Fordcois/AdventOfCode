import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_list_of_ints import file_as_list_of_ints
# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_ints(f'{data_set}_input.txt')[0]

def blink(stone_array):
    output=[]
    for stone in stone_array:
        digit_length= len(str(stone))
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if stone == 0:
            output.append(1)

    # If the stone has an even number of digits, it is replaced by two stones.
    # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
    # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        elif digit_length % 2 == 0:
            stone_as_str_list = [char for char in str(stone)]
            new_stone_one = int(''.join( stone_as_str_list[:digit_length//2]))
            new_stone_two = int(''.join( stone_as_str_list[digit_length//2:]))
            output.append(new_stone_one)
            output.append(new_stone_two)
    # If none of the other rules apply, the old stone's number multiplied by 2024 .
        else:  
            output.append(stone*2024)
    return output


# Puzzle
def solve():
    blinks=0
    stones = data

    while blinks < 25:
        stones = blink(stones)
        blinks += 1

    print (f'After {blinks} blinks you have {len(stones)} stones')



solve()