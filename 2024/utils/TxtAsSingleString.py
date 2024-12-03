def txt_as_single_string(txtfile):
    with open(txtfile, "r") as file:
        output = file.read()
    return output