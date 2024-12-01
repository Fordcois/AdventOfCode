from inputDay02 import inputdata
import re

inputlist = inputdata.split('\n')
total=0

for game in inputlist:
  
    first_split = game.split(':')

    name_split=int(first_split[0].split(' ')[1])

    Results=first_split[1]
    GameResults = re.split(';|,', Results)
    
    red=0
    green=0
    blue=0
    for entry in GameResults:

        if entry.split(' ')[2] == 'red' and int(entry.split(' ')[1]) > red:
            red = int(entry.split(' ')[1])
        if entry.split(' ')[2] == 'green' and int(entry.split(' ')[1]) > green:
            green = int(entry.split(' ')[1])
        if entry.split(' ')[2] == 'blue' and int(entry.split(' ')[1]) > blue:
            blue  = int(entry.split(' ')[1])
    results=[name_split,red,green,blue]

    if results[1] <= 12 and results[2] <= 13 and results[3] <= 14:
        total+=results[0]

print (f'Total Would be: {total}')
# Total Would be: 2061
