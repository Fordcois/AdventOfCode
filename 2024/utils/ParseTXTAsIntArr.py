def parse_txt_return_int_arr(txtfile):
    output = []
    with open(txtfile, 'r') as file:
        for line in file:
            output.append([int(x) for x in line.strip().split()])
    return output