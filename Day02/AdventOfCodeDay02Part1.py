from inputDay02 import inputdata
import re



# Split the input
inputlist = inputdata.split('\n')
total=0
# iterate through Split list into a list with Game Number as first Value
for game in inputlist:
  
    first_split = game.split(':')
    # Get the number of the game as the first value and turn it to an integer - GOT IT
    name_split=int(first_split[0].split(' ')[1])
    # Get a list of all entires
    Results=first_split[1]
    GameResults = re.split(';|,', Results)
    
    # print ('-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    # print (f'Game: {GameResults} ')
    # print ('-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
# Iterate through all the results and make them RGB:
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
    # print(f'Game: {name_split}')
    # print (f'red: {red}')
    # print (f'Green: {green}')
    # print (f'Blue: {blue}')
    results=[name_split,red,green,blue]
    print(f'Game: {results[0]} Red:{results[1]} Green:{results[2]} Blue:{results[3]}')


    # See If The games are possible against criteria:
    if results[1] <= 12 and results[2] <= 13 and results[3] <= 14:
        print (f'Game {results[0]} is possible')
        total+=results[0]

print (f'Total Would be: {total}')






    



    


    # GameNumber=split1[0]
    # print (f'List 1: {split1[0]}')
    # print (f'List 2: {split1[1]}')
# Then RGB List Values
