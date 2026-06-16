import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

def cycle_letter(letter,cycles):
    alpha_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    starting_index = alpha_arr.index(letter.upper())
    new_index = (cycles+starting_index) % 26
    return alpha_arr[new_index]

def decrypt_room_name(room_str):
    phrase_and_id = room_str[:-7].split('-')
    code = ('').join(phrase_and_id[:-1])
    cycles= int(phrase_and_id[-1])

    decrypted_room_name = []
    for char in list(code):
        decrypted_room_name.append(cycle_letter(char,cycles))
    return(''.join(decrypted_room_name)),cycles

# Puzzle
def solve():
    for room in data:
        decoded_name,room_id = decrypt_room_name(room)
        if decoded_name =='NORTHPOLEOBJECTSTORAGE':
            print (F"{decoded_name} - {room_id}")

solve()