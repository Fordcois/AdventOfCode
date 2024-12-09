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
            visualised_list.append([pointer] * data_blocks[pointer])
            stretched_data.append([pointer] * data_blocks[pointer])
        if pointer < len(space_blocks):
            visualised_list.append([''] * space_blocks[pointer])
            stretched_free.append([''] * space_blocks[pointer])
        pointer += 1
    
    visualised_list = [x for x in visualised_list if x != []]

    for program in stretched_data[::-1]:
        program_index = visualised_list.index(program)
        program_size = len(program)
        for block_index,block in enumerate(visualised_list[:program_index]):
            block_size = len(block)
            if ('' in block) and block_size >= program_size:
                space_remaining = block_size-program_size
                new_block = [''] * (block_size-space_remaining)
                visualised_list[block_index],visualised_list[program_index] = visualised_list[program_index],new_block
                if space_remaining != 0:
                    visualised_list.insert(block_index+1,[''] *space_remaining)
                break 

    sorted_list = [item for arr in visualised_list for item in arr]
    checksum = sum(i * char for i, char in enumerate(sorted_list) if char != '')
    print (f'Checksum: {checksum}')

                






        
    


solve()
