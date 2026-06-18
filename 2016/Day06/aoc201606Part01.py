import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings
import string

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

column_letter_counts={}

password_length = len(data[0])

for i in range(password_length):
    column_letter_counts[str(i)]={}
    for char in string.ascii_lowercase:  
        column_letter_counts[str(i)][char]=0




# Puzzle
def solve():
    solved_password=[]
    for word in data:
        for index,char in enumerate(word):
            column_letter_counts[str(index)][char] += 1
    for i in range(password_length):
        solved_password.append(
max(column_letter_counts[str(i)], key=column_letter_counts[str(i)].get)
        )
    print(''.join(solved_password))

    return

solve()