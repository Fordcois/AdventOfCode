def file_as_list_of_strings(txtfile):
    with open(txtfile, 'r') as file:
        return [line.strip() for line in file]