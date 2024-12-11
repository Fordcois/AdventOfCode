import sys
import os
import functools
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_list_of_ints import file_as_list_of_ints
# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_ints(f'{data_set}_input.txt')[0]

@functools.lru_cache(maxsize=None)
def single_blink_stone(value):
    text = str(value)
    num_of_digits = len(text)
    
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    if value == 0:
        return (1, None)

    # If the stone has an even number of digits, it is split into two stones.
    # The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. 
    elif num_of_digits % 2 == 0:
        mid_point = num_of_digits // 2
        left_stone = int(text[:mid_point])
        right_stone = int(text[mid_point:])
        return (left_stone, right_stone)
    
    else:
    # If none of the other rules apply, the old stone's number multiplied by 2024.
        return (value * 2024, None)

@functools.lru_cache(maxsize=None)
def count_stone_blinks(stone, depth):
    left_stone, right_stone = single_blink_stone(stone)


    if depth == 1:
        if right_stone is None:
            return 1
        else:
            return 2

    else:
        # Down to the next level and add the results if there are two stones
        output = count_stone_blinks(left_stone, depth - 1)
        if right_stone is not None:
            output += count_stone_blinks(right_stone, depth - 1)
        
        return output

def solve():
    blink_count=75
    total_stones = 0
    for stone in data:
        total_stones += count_stone_blinks(stone, blink_count)

    print(f'After {blink_count} blinks, you have {total_stones} stones')


solve()
