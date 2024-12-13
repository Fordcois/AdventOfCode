def file_as_list_of_string_arrays(txtfile):
    output_array=[]
    with open(txtfile, 'r') as file:
        for line in file:
            output_array.append([char for char in line.strip()])

    return output_array