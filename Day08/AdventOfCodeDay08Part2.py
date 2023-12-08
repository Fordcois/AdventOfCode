import math
import functools
from inputDay08 import *
data_set=input_data
list_of_data=data_set.split('\n')

directions=list_of_data[0]
steps_taken=0
map_dict={}

for map_entry in list_of_data[2:]:
    hub=map_entry[:3]
    left_direction=map_entry[7:10]
    right_direction=map_entry[12:15]
    map_dict[hub] = {"L":left_direction,"R":right_direction}

def Navigate(starting_location,direction):
    global steps_taken
    steps_taken +=1
    return map_dict[starting_location][direction]

def part_one(starting_location):
    global steps_taken
    steps_taken=0
    location=starting_location
    current_direction=0
    while current_direction < len(directions):
        if location[2] =='Z':
            return steps_taken
        else:
            location=Navigate(location,directions[current_direction])
        if current_direction == (len(directions))-1:
            current_direction=0
        else:
            current_direction+=1

def part_two():
    input_list=[part_one(x) for x in map_dict if x[2]=='A']
    lcm_result = functools.reduce(lambda x, y: x * y // math.gcd(x, y), input_list)
    print (f"It would Take the ghosts {lcm_result} steps")

part_two()
# It Would Take the ghosts 12324145107121 steps