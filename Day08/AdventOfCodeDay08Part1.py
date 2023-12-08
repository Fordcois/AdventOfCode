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

def part_one():
    location='AAA'
    list_of_directions=directions*1000
    for direction in list_of_directions:
        if location =='ZZZ':
            break
        else:
            location=Navigate(location,direction)
        


part_one()

print (f"You have taken {steps_taken} steps")
# You have taken 13207 steps

