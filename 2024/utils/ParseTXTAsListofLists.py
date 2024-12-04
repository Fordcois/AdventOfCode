def parse_Txt_as_list_of_lists(txtfile):
    output = []
    with open(txtfile, 'r') as file:
        for line in file:
            output.append(list(line.strip()))
    return output