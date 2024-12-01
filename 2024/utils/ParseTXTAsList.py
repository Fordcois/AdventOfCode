def Parse_Txt_as_List(txtfile):
    output = []
    with open(txtfile, 'r') as file:
        for line in file:
            output.append(line.strip())
    return output