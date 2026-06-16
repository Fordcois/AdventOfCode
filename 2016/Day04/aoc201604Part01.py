import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')



def is_valid_room(room_str):
    char_counts={}
    checksum = room_str[-6:-1]
    phrase_and_id = room_str[:-7].split('-')
    room_id = phrase_and_id[-1]
    code = ('').join(phrase_and_id[:-1])


    for char in code:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1

    phrase = (''.join(sorted(char_counts, key=lambda c: (-char_counts[c], c))))[:5]
    if checksum == phrase:
        return int(room_id)
    return 0
# Puzzle
def solve():
    room_id_totals = 0
    for code in data:
        room_id_totals += is_valid_room(code)
        

    print (f"Answer is {room_id_totals}")

solve()