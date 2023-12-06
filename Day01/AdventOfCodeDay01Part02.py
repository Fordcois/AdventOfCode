from inputDay01 import coord_list

letter_dict= {1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}

def is_a_number(number_to_check,index, character, entry):
    if character == str(number_to_check):
        checknumber(index,number_to_check)
    try:
        if letter_dict[number_to_check] == entry[index:index + len((letter_dict[number_to_check]))]:
            checknumber(index,number_to_check)
    except IndexError:
        pass

def checknumber(index,found_number):
    global earliest_find_index, earliest_find, last_find_index, last_find
    if earliest_find_index is None or index < earliest_find_index:
        earliest_find_index = index
        earliest_find = found_number
    if last_find_index is None or index > last_find_index:
        last_find_index = index
        last_find = found_number

total_count=0

for entry in coord_list:
    
    earliest_find_index=None
    earliest_find=None
    last_find_index=None
    last_find=None

    for index, character in enumerate(entry):
        for number in range (1,10):
            is_a_number(number,index,character,entry)

    entry_total = int(f'{earliest_find}{last_find}')
    total_count+=entry_total

print(f' The Final total is: {total_count}')
# 55260





