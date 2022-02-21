def hex_characters(value):
    hex_chars = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
       }
    return hex_chars[value]


def dec_to_bin(decimal):
    binary = '' 
    while decimal >= 1:
        binary  += str(decimal % 2) 
        decimal //= 2
    return binary[::-1]


def bin_to_dec(binary):
    decimal = 0
    for bit in binary:
        if bit == '0':
            decimal = decimal*2 + 0
        elif bit == '1':
            decimal = decimal*2 + 1
        else:
            print("Not a correct binary number")
            exit(1)
    return decimal
        

def bin_to_hex(binary):
    hex = ''

    # group into fours
    groups = []
    # iterator
    n = 0
    for i in range(len(binary)):
        # if the group is not 4 bits
        if 0 < len(binary[n:n+4]) < 4:
            # add zeros to make it 4 bits
                groups.append(binary[n:n+4] + '0' * (4-len(binary[n:n+4])))
                break
        # iterate
        elif len(binary[n:n+4]) == 4:
            if len(binary) >= n+4:
                groups.append(binary[n:n+4])
                n += 4

    # groups to hex
    for group in groups:
        value = bin_to_dec(group)
        hex += hex_characters(value)

    return hex

def dec_to_hex(decimal):
    values = [] 
    hex = ''
    while decimal >= 1:
        values.append(str(decimal % 16)) 
        decimal //= 16
    for value in values:
        hex += hex_characters(int(value))

    return hex[::-1]


def main():
    choice = int(input("From Decimal to Binary converter [0]\nFrom Decimal to Hexadecimal converter [1]\nFrom Binary to Decimal converter [2]\nFrom Binary to Hexadecimal converter [3]\n"))
    if choice == 0:
        dec_input = int(input("Enter a number in decimal: "))
        print(dec_to_bin(dec_input))
    if choice == 1:
        dec_input = int(input("Enter a number in decimal: "))
        print(dec_to_hex(dec_input))
    if choice == 2:
        bin_input = str(input("Enter a number in binary: "))
        print(bin_to_dec(bin_input))
    if choice == 3:
        bin_input = str(input("Enter a number in binary: "))
        print(bin_to_hex(bin_input))
        


# ------------main------------
main()
# ----------------------------