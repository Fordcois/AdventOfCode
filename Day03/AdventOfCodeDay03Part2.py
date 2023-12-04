from inputDay03 import inputdata

grid= (inputdata.split(('\n')))
maximum_line_length=len(grid[0])
number_of_rows=len(grid)
part2total=0

def find_numbers_around_gears(x,y):
    coords_to_check=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    numberchecks=[]
    for spaces in coords_to_check:
        try:
            if (grid[y+spaces[0]][x+spaces[1]]).isnumeric():
                numberchecks.append(get_details_of_number( x+spaces[1],y+spaces[0]))
        except IndexError:
            pass
    if len(numberchecks)>1:
        calculate_gear_ratio(numberchecks)

def find_edge_coord(x, y, direction):
    edge_coord = x
    try:
        while True:
            if direction == 'left':
                if x >= 0 and grid[y][x - 1].isnumeric():
                    x -= 1
                    edge_coord  = x
                else:
                    break
            elif direction == 'right':
                if x < len(grid[y]) - 1 and grid[y][x + 1].isnumeric():
                    x += 1
                    edge_coord  = x
                else:
                    break
        return edge_coord 
    except IndexError:
        return edge_coord 
    
def get_details_of_number(x,y):
    number=''
    start=find_edge_coord(x,y,'left')
    end=find_edge_coord(x,y,'right')
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

X,Y = 0,0
while Y < maximum_line_length:
    X = 0 
    while X < number_of_rows:
        if grid[Y][X] == '*':
            find_numbers_around_gears(X,Y)
        X += 1
    Y += 1 

print (f'The Final total for part 2 is: {part2total}')





