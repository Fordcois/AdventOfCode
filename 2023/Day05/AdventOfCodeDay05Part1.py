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

find_lowest_location(seeds)
# The lowest location Number is: 227653707


