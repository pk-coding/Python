def reverse_lol(decimal_items):
    lol = (decimal_items & 1) << 7
    return (decimal_items >> 1) | lol

def reverse_bits_after_shifting(lol):
    bit = lol << 1
    reverse_bits = bit & 255
    if (lol > 127 ):
        reverse_bits = reverse_bits | 1
    return (reverse_bits)

def main():
    encrypted_string = input("Enter your value: ")
    characters = []
    decimal_items = []
    lol_items = []
    reverse_bits_items = []
    ORD_key = []
    ending_items = []
    Index_Value = 0
    result = []

    while encrypted_string:
        characters.append(encrypted_string[:2])
        encrypted_string = encrypted_string[2:]

    for i in characters:
        decimal = int(i, 16)
        decimal_items.append(decimal)

    for i in decimal_items:
        lol_items.append(reverse_lol(i))

    for i in lol_items:
        reverse_bits_items.append(reverse_bits_after_shifting(i))

    a = ord("a")
    ORD_key.append(a)
    decryption_first_char = int(ORD_key[0]) ^ int(lol_items[0])
    ending_items.append(decryption_first_char)

    for i in lol_items:
        if Index_Value == 0:
            Index_Value += 1
            pass
        else:
            decryption_next_chars = int(reverse_bits_items[Index_Value-1]) ^ int(i)
            ending_items.append(decryption_next_chars)
            Index_Value += 1

    for i in ending_items:
        result.append(chr(i))
        str_result = ''.join(result)
    print(str_result)

if __name__ == '__main__':
    main()