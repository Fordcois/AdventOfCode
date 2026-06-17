import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str
import hashlib

# Substitue test/real to switch inputs
data_set = 'test'
data = file_as_str(f'{data_set}_input.txt')

def md5_hash(input):
    return hashlib.md5(input.encode()).hexdigest() # returns '5d41402abc4b2a76b9719d911017c592'

def starts_with_five_zeros(input):
    return input[:5] == '00000'


# Puzzle
def solve():
    door_id='abc'
    index = 0
    cracked_password=[]
    while len(cracked_password) < 8:
        hash = md5_hash(f"{door_id}{index}")
        if starts_with_five_zeros(hash):
            cracked_password.append(hash[5])
            print (f'Letter Cracked - {index}')
        index += 1

    print (''.join(cracked_password))
    return

solve()