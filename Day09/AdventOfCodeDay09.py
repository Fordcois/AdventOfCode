from inputDay09 import *
inputdata=input_data
data_as_strings= [y.split(' ') for y in [x for x in inputdata.split(('\n'))]]

def find_differences(array):
    intlist = [int(x) for x in array]
    array_of_differences = []
    for i in range(len(intlist) - 1):
        array_of_differences.append(intlist[i + 1] - intlist[i])
    return array_of_differences

def part_one(array):
    starting_line = [int(x) for x in array]
    # Reverse Line - Remove for Part One/Part Two Solution
    starting_line.reverse()
    StepsTaken=0
    latest_difference=(find_differences(starting_line))
    array_of_differences=[]
    array_of_differences.append(latest_difference)
    while not all(element == 0 for element in array_of_differences[-1]):
        StepsTaken+=1
        array_of_differences.append(latest_difference)
        latest_difference=find_differences(latest_difference)
    
    array_of_differences[0]=starting_line

    for i in range (StepsTaken):
        index=StepsTaken-i
        array_of_differences[index-1].append(array_of_differences[index-1][-1]+array_of_differences[index][-1])
    return array_of_differences[0][-1]
    

total=0
for data in data_as_strings:
    total+=part_one(data)

print (f"Your Total is: {total}")

# Part 1 - Your Total is: 2101499000
# Part 2 - Your Total is: 1089




