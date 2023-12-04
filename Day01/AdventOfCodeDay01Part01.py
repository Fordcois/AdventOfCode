from inputDay01 import coord_list
# Takes The String and splits it into a list by linebreaks
total_number=0

for entry in coord_list:
    instance_total=[]
    # Find First Number - iterates through the number and stops as soon as it finds a number
    for letter in entry:
        if letter.isdigit():
            instance_total.append(letter)
            break
    # Find Last Number - Goes through the above starting the list backwards
    for letter in entry[::-1]:
        if letter.isdigit():
            instance_total.append(letter)
            break
    # Capture First Digit and last digit, convert them to a complete number then add that number to the total
    if len(instance_total) == 1:
        revealed_value=int(instance_total[0]+instance_total[0])
    elif len(instance_total) == 2:
        revealed_value=int(instance_total[0]+instance_total[1])
        
    total_number+=revealed_value
    # print(revealed_value)

print(total_number)
    


