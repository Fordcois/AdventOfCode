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
    visited_homes=[(0,0)]
    Actor = 'Santa'
    Actors = {
        'Santa':{'X_position':0,'Y_position':0},
        'Robot':{'X_position':0,'Y_position':0},
        'Switch_actor_from':{'Santa':'Robot','Robot':'Santa'}
            }
    
    for char in data:
        if char == '>':
            Actors[Actor]['X_position'] += 1
        elif char == '<':
            Actors[Actor]['X_position'] -= 1
        elif char == '^':
            Actors[Actor]['Y_position'] +=1
        elif char == 'v':
            Actors[Actor]['Y_position'] -= 1
        if (Actors[Actor]['X_position'],Actors[Actor]['Y_position']) not in visited_homes:
            visited_homes.append((Actors[Actor]['X_position'],Actors[Actor]['Y_position']))
        # Switch Actor
        Actor = Actors['Switch_actor_from'][Actor]

    print (f'Presents at {len(visited_homes)} unique homes')
    return len(visited_homes)

solve()
# Presents at 2572 unique homes