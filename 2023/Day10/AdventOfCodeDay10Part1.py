from inputDay10 import *
import sys

data_set=input_data
data_as_strings=data_set.split(('\n'))
map_grid=[list(x) for x in data_as_strings]

locations_visited=[]
steps_taken=0

def entered_from(Y, X):
    current_Y,current_X = [Y, X]
    last_location_visisted_Y,last_location_visisted_X= locations_visited[-1]
    if current_X == last_location_visisted_X and current_Y == (last_location_visisted_Y+1):
        return 'top'
    if current_X == last_location_visisted_X and current_Y == (last_location_visisted_Y-1):
        return 'bottom'
    if current_X == (last_location_visisted_X-1) and current_Y == last_location_visisted_Y:
        return 'right'
    if current_X == (last_location_visisted_X+1) and current_Y == last_location_visisted_Y:
        return 'left'

def find_start_coordinates():
    for Y,value in enumerate(map_grid):
        for X,value in enumerate(map_grid):
            if map_grid[Y][X] =='S':
                locations_visited.append([Y,X])
                if map_grid[Y-1][X] in '|7F':
                    step_through_the_tunnel_to(Y-1,X)
                elif map_grid[Y][X+1] in 'J7':
                    step_through_the_tunnel_to(Y,X+1)
                elif map_grid[Y][X-1] in 'LF':
                    step_through_the_tunnel_to(Y,X-1)
                elif [Y+1][X] in '|LJ':
                    step_through_the_tunnel_to(Y+1,X)

def step_through_the_tunnel_to(Y,X):
    global locations_visisted, steps_taken
    steps_taken+=1
    came_from=entered_from(Y,X)
    locations_visited.append([Y,X])
    current_square=map_grid[Y][X]

    if current_square == '|':   # | is a vertical pipe connecting north and south.
        #   If Entered from Bottom go up
        if came_from=='bottom':
            step_through_the_tunnel_to(Y-1,X)
        #   If entered from top go down
        if came_from=='top':
            step_through_the_tunnel_to(Y+1,X)
    if current_square == '-':   # - is a horizontal pipe connecting east and west.
        #   If entered from left go Right
        if came_from=='left':
            step_through_the_tunnel_to(Y,X+1)
        #   If Entered form Right Go Left
        if came_from=='right':
            step_through_the_tunnel_to(Y,X-1)
    if current_square == 'L':   # L is a 90-degree bend connecting north and east.
        # If came from the right go up
        if came_from=='right':
            step_through_the_tunnel_to(Y-1,X)
        # If came from the top go right
        if came_from=='top':
            step_through_the_tunnel_to(Y,X+1)
    if current_square == 'J':    # J is a 90-degree bend connecting north and west.
        # If came from the top go left
        if came_from=='top':
            step_through_the_tunnel_to(Y,X-1)
        # If came from left top go up
        if came_from=='left':
            step_through_the_tunnel_to(Y-1,X)
    if current_square == '7': # 7 is a 90-degree bend connecting south and west.
        # if entered from the left go down
        if came_from=='left':
            step_through_the_tunnel_to(Y+1,X)
        # if entered from the bottom go up and left
        if came_from=='bottom':
            step_through_the_tunnel_to(Y,X-1)
    if current_square == 'F': # F is a 90-degree bend connecting south and east.
        # if entered from the right go down
        if came_from =='right':
            step_through_the_tunnel_to(Y+1,X)
        # if entered from the bottom go up and right
        if came_from == 'bottom':
            step_through_the_tunnel_to(Y,X+1)
    elif current_square=='S':
        print ('We Are back at the beginning!')

sys.setrecursionlimit(100000)
find_start_coordinates()

print(f"The Mid point of the loop is: {int(steps_taken/2)}")
# The Mid point of the loop is: 6907



