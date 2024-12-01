from inputDay02 import inputdata
import re
# Split the input into a list
inputlist = inputdata.split('\n')
total=0

for game in inputlist:
    # Split of the name of the game from the cube reveals
    first_split = game.split(':')
    # Get a list of all cube reveals in that game
    cube_reveals = re.split(';|,', first_split[1])
    # Store Games as [Game Number,Red,Blue,Green]
    result=[int(first_split[0].split(' ')[1]),0,0,0]
    for entry in cube_reveals:
        if entry.split(' ')[2] == 'red' and int(entry.split(' ')[1]) > result[1]:
            result[1] = int(entry.split(' ')[1])
        if entry.split(' ')[2] == 'green' and int(entry.split(' ')[1]) > result[2]:
            result[2] = int(entry.split(' ')[1])
        if entry.split(' ')[2] == 'blue' and int(entry.split(' ')[1]) > result[3]:
            result[3]  = int(entry.split(' ')[1])

    MinimumResult=result[1]*result[2]*result[3]
    total+=MinimumResult
print (f'Total Would be: {total}')

# Total Would be: 72596