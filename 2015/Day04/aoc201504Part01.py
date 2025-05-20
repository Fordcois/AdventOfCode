import sys
import os
import hashlib
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str

data_set = 'real'
data = file_as_str(f'{data_set}_input.txt')

def solve():
    i=1
    while True:
        codeword = data + (str(i))
        hash_obj = hashlib.md5(codeword.encode())
        hash_hex = hash_obj.hexdigest()
        if (hash_hex[:5]) == '00000':
            print (f' Hash Found at {i}')
            return True
        else:
            i += 1

solve()
#  Hash Found at 117946