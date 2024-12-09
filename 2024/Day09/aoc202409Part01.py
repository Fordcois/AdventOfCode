import sys
import os
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_string import file_as_str
# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_str(f'{data_set}_input.txt')

# Puzzle
def solve():
    visualised_list=[]
    stretched_data=[]
    stretched_free=[]

# Split into Data blocks & Free Spaces
    data_blocks = [int(record) for index,record in enumerate(data) if index%2 == 0]
    space_blocks = [int(record) for index,record in enumerate(data) if index%2 != 0]
    pointer = 0
    while pointer < len(data_blocks) or pointer < len(space_blocks):
        if pointer < len(data_blocks):
            visualised_list.extend([pointer] * data_blocks[pointer])
            stretched_data.extend([pointer] * data_blocks[pointer])
        if pointer < len(space_blocks):
            visualised_list.extend([''] * space_blocks[pointer])
            stretched_free.extend([''] * space_blocks[pointer])
        pointer += 1
    sorted_list=[]
    
    for byte in visualised_list:
        if byte == '':
            if len(stretched_data) > 0:
                sorted_list.append(stretched_data.pop(-1))
            else:
                sorted_list.append('')
        else:
            if len(stretched_data) > 0:
                sorted_list.append(stretched_data.pop(0))
            else:
                sorted_list.append('')
    
    check_sum = sum(index * data_id for index, data_id in enumerate([x for x in sorted_list if x != '']))
    print(f'The Total is {check_sum}')

solve()