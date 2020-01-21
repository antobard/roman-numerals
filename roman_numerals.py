# -*-coding:utf-8 -*

roman_num = [(1000, "M"), (500, "D"), (100, "C"), (50, "L"), (10, "X"),
    (5, "V"), (1, "I")]
roman_num_special = [(900, "CM"), (400, "CD"), (90, "XC"), (40, "XL"),
    (9, "IX"), (4, "IV")]

def int_to_roman(number):
    """Convert a number into roman numerals"""
    number = int(number)
    roman_string = ''

    # Concatenation of the lists of roman numerals and sort by increasing order
    all_roman_num = (roman_num + roman_num_special)
    all_roman_num.sort(reverse=True)

    # For each roman numerals if it's divisible by the number, add the symbol to the string
    for i in range(len(all_roman_num)):
        div = divmod(number, all_roman_num[i][0])
        roman_string += all_roman_num[i][1] * div[0]
        number -= all_roman_num[i][0] * div[0]

    return roman_string

def roman_to_int(string):
    """Convert a string into an integer"""
    integer = 0

    # For each roman numeral, if it's in the string, add the corresponding number
    for num in roman_num_special:
        if string.count(num[1]) > 0:
            integer += string.count(num[1]) * num[0]
            string = string.replace(num[1], "")
    for num in roman_num:
        integer += num[0] * string.count(num[1])

    return integer

def roman_converter(conversion):
    """Convert roman to integer or vice versa"""
    if type(conversion) is int:
        return int_to_roman(conversion)
    elif type(conversion) is str:
        return roman_to_int(conversion)
    else:
        print("Wrong input")