def read_file_as_array_array(txtfile):
    with open(txtfile, 'r') as file:
        return [list(line.strip()) for line in file]