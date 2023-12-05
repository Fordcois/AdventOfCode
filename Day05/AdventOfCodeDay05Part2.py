from inputDay05 import *

conversion={}
split_into_paragraphs= input_data.split('\n\n')
seeds = [int(x) for x in (split_into_paragraphs[0].split(':')[1]).strip().split(' ')]

for paragraph in split_into_paragraphs[1:]:
    ranges=[]
    map=paragraph.split('\n')
    for line in map[1:]:
        split_ints = [int(x) for x in line.split(' ')]
        ranges.append(split_ints)
    conversion[map[0].split(' ')[0]] = ranges

def convert (conversion_string,source_number):
    for list in conversion[conversion_string]:
        destination_range_start=list[0]
        source_range_start=list[1]
        range=list[2]
        if  source_range_start <= source_number< source_range_start+range:
            difference=source_number-source_range_start
            return (destination_range_start+difference)
    return source_number

def convert_through_all(start_number):
    Number=start_number
    for key in conversion:
        Number=convert(key,Number)
    return (Number)

def find_lowest_location(array):
    lowest_location=None
    for number in array:
        location=convert_through_all(number)
        # Would Appreciate guidance on a better way to do this!
        if  lowest_location == None:
            lowest_location=location
        elif location < lowest_location:
            lowest_location=location
    print (f'The lowest location Number is: {lowest_location}')

def deconvert (conversion_string,source_number):
    for list in conversion[conversion_string]:
        destination_range_start=list[1]
        source_range_start=list[0]
        range=list[2]
        if  source_range_start <= source_number< source_range_start+range:
            difference=source_number-source_range_start
            return (destination_range_start+difference)
    return source_number

dictKeys=[x for x in reversed(conversion.keys())]
def deconvert_through_all(start_number):
    Number=start_number
    for transformation in dictKeys:
        Number=deconvert(transformation,Number)
    return (Number)


def is_lowest(number_to_check,array):
    index=0
    while index != len(array):
        start_of_range=array[index]
        end_of_range = start_of_range+(array[index+1]-1)
        if start_of_range <= number_to_check < end_of_range:
            return True
        index+=2

def reverse_solve(location_number):
    while location_number != (location_number-1):
        seed_number= deconvert_through_all(location_number)
        if is_lowest(seed_number,seeds) == True:
            print (f'{location_number} is the lowest!')
            break
        location_number+=1
#part 1
find_lowest_location(seeds)
# part 2
reverse_solve(0)