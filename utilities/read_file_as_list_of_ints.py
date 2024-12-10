def file_as_list_of_ints(txtfile):
    output = []
    with open(txtfile, 'r') as file:
        for line in file:
            output.append([int(x) for x in line.strip().split()])
    return output