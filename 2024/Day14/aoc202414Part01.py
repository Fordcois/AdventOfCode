import sys
import os
import re
import math
# Adjust Import Paths
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# Import Utilities
from utilities.read_file_as_str_list import file_as_list_of_strings

# Substitue test/real to switch inputs
data_set = 'real'
data = file_as_list_of_strings(f'{data_set}_input.txt')

class SecurityRobot:
    def __init__(self,data_array,grid_x,grid_y):
        self.x_loc = int(data_array[0])
        self.y_loc = int(data_array[1])
        self.x_movement = int(data_array[2])
        self.y_movement = int(data_array[3])
        self.grid_x = grid_x
        self.grid_y = grid_y

    def move(self):
        potential_x = self.x_loc + self.x_movement
        potential_y = self.y_loc + self.y_movement
        # X Movement
        if  0 <= potential_x < self.grid_x: 
            self.x_loc = potential_x
        else:
            self.x_loc= potential_x % self.grid_x
        # Y Movement
        if 0 <= potential_y < self.grid_y:
            self.y_loc = potential_y
        else:
            self.y_loc= potential_y % self.grid_y
    
    def move_times(self,i):
        for i in range (i):
            self.move()

    def return_loc(self):
        return self.x_loc,self.y_loc

def locate_quad(coord_tuple,x_size,y_size):
    x_half_way = x_size//2
    y_half_way = y_size//2
    x_cord,y_cord = coord_tuple
    if (x_cord == x_half_way ) or (y_cord == y_half_way):
        return None
    else:
        if y_cord < y_half_way:
            vert='north'
        else:
            vert='south'
        if x_cord < x_half_way:
            hori='west'
        else:
            hori='east'
        return vert+hori

def solve():
    number_pattern = '-?\d+'
    map_x = 101
    map_y = 103
    quads= {'northwest':0,'northeast':0,'southwest':0,'southeast':0}
    robots = [SecurityRobot(re.findall(number_pattern,line),map_x,map_y) for line in data]
    for robot in robots:
        robot.move_times(100)
        quad = locate_quad(robot.return_loc(),map_x,map_y)
        if quad:
            quads[quad] +=1

    print (f'Sum of all bots in quadrants is: {math.prod(quads.values())}')


    
solve()
