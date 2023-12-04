from inputDay03 import inputdata
import re

grid= (inputdata.split(('\n')))
maximum_line_length=len(grid[0])
number_of_rows=len(grid)
part2total=0


def FindInfoNumber(x_location,y_location):
    str_number = (re.search('^\d+',grid[y_location][x_location:]))[0]
    found_number=int(str_number)
    number_length = len(str_number)
    if x_location + number_length > maximum_line_length:
        if y_location + 1 > number_of_rows:
            pass
        else:
            new_x = 0
            new_y = y_location+1
    else:
        new_x = x_location + number_length
        new_y = y_location
    return (found_number,number_length,new_x,new_y)





#  Okay So I want to iterate through a list of potential coordinates and then try them
def build_check_grid(x,y,size):
    list_of_coords_to_check=[]
# Left
    list_of_coords_to_check.append([x-1,y])
# Right
    list_of_coords_to_check.append([x+size,y])
# Bottom
    for i in range (size):
        list_of_coords_to_check.append([x+i,y-1])
#  Top
    for i in range (size):
        list_of_coords_to_check.append([x+i,y+1])
# Diagonals
    list_of_coords_to_check.append([x-1,y+1])
    list_of_coords_to_check.append([x+size,y+1])
    list_of_coords_to_check.append([x-1,y-1])
    list_of_coords_to_check.append([x+size,y-1])

    return (list_of_coords_to_check)

coords=build_check_grid(1,9,2)
# print (f'Full List of Coords is {coords}')
def check_surrounding_squares(array):
    for coord_set in array:
        X = coord_set[1]
        Y = coord_set[0]
        if X >= 0 and Y >= 0:
            # print(f'X:{X} Y:{Y} - Both are valid inputs So we check this')
            try:
                if not (grid[X][Y]).isalpha() and  not (grid[X][Y]).isnumeric() and  (grid[X][Y]) !='.':
                    return True
            except IndexError:
                pass








def find_numbers_around_gears(x,y):
    coords_to_check=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    numberchecks=[]

    for spaces in coords_to_check:
        try:
            if (grid[y+spaces[0]][x+spaces[1]]).isnumeric():
                numberchecks.append(get_details_of_number( x+spaces[1],y+spaces[0]))
        except IndexError:
            pass
    print (f'{numberchecks}')
    if len(numberchecks)>1:
        calculate_gear_ratio(numberchecks)

def find_leftmost_number(x, y):
    leftmost_coord = x  
    try:
        while x >= 0 and grid[y][x - 1].isnumeric():
            x -= 1
            leftmost_coord = x
        return leftmost_coord
    except IndexError:
        return leftmost_coord  

def find_rightmost_number(x, y):
    rightmost_coord = x 
    try:
        while x >= 0 and grid[y][x + 1].isnumeric():
            x += 1
            rightmost_coord = x
        return rightmost_coord
    except IndexError:
        return rightmost_coord
    
def get_details_of_number(x,y):
    number=''
    start=find_leftmost_number(x,y)
    end=find_rightmost_number(x,y)
    for i in range (end-start+1):
        number=number+grid[y][start+i]
    return (int(number),[y,end])


def calculate_gear_ratio(array):
    global part2total
    firstvalue=array[0]
    for captured_value in array [1:]:
        if captured_value != firstvalue:
            part2total += firstvalue[0]*captured_value[0]
            return




X = 0
Y = 0
while Y < maximum_line_length:
    X = 0  # Reset X back to 0 at the beginning of each Y iteration
    while X < number_of_rows:
        # print(f'found {grid[Y][X]} at coordinate Y:{Y} X:{X}')  
        # Print X and Y to see the coordinates being traversed
        if grid[Y][X] == '*':
            find_numbers_around_gears(X,Y)
        X += 1
    Y += 1 

print (f'The Final total for part 2 is: {part2total}')





