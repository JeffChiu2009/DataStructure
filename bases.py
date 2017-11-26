#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits = '0123456789'
# string.hexdigits = '0123456789abcdefABCDEF'
# string.ascii_lowercase ='abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters = ascii_lowercase + ascii_uppercase
# # string.printable is 
# digits + ascii_letters + punctuation + whitespace


def letter_from_num(num):
    """ Convert letter from number:
    input: int -- integer representation of number (in base 10)
    return: strings of letters """
    letters  ='abcdefghijklmnopqrstuvwxyz'
    return letters[num - 10]

def digit_from_letter(letter):
    """ 
    input: any letter 
    return: int -- number representation of number (in base 10)
    handles digits from hexadecimal (base 16)
    handles digits from any base (2 up to 36)
    math function that calculate the number based on math conversion
    this calculate from the 36 letters -97 + 1
    """
    num = ord(letter) - 97 + 10
    return num

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: result is int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    # TODO: Decode digits from hexadecimal (base 16)
    # TODO: Decode digits from any base (2 up to 36)
    # it checks if the digit is digit else it's a letter.
    # create a helper function that handles hexadecimal digit_from_letter
    # we multify the number
    result = 0
    # Loop through the enumeration 
    # index and digit
    # create a helper function that handles hexadecimal digit_from_letter
    for index, digit in enumerate(digits):
        if digit.isdigit(): 
            digit_to_add = int(digit) 
        else: 
            digit_to_add = digit_from_letter(digit)
        # add them together on the result with the digital_to_add to the result
        result += digit_to_add
        if index is not len(digits) - 1: 
            result *= base 
        else: 
            1
    # Return the result decimal digit
    return result

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    # TODO: Encode number in hexadecimal (base 16)
    # TODO: Encode number in any base (2 up to 36)
    # it checks if the digit is digit else it's a letter.
    # create a helper function that handles hexadecimal digit_from_letter
    # we multify the number
    # new base num
    new_base_number = ''
    # encode helps me to make sure that we will work 
    while number != 0:
        remainder = number % base
        number = number // base
        if (remainder >= 10 and base > 10):
            remainder = letter_from_num(remainder) 
        else: 
            remainder
        new_base_number += str(remainder)
    # Reverse
    new_base_number = new_base_number[::-1]
    return new_base_number


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    if base1 == 10:
        new_base_number = encode(int(decimal_digit), base2)
    else:
        decimal_digit = decode(digits, base1)
        new_base_number = encode(decimal_digit, base2)
    # Return
    return new_base_number



def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    print(decode('123456', 8)) 
    print(decode('123456', 9))  
    print(decode('123456', 10)) 
    print(decode('123456', 12)) 
    print(decode('123456', 15)) 
    print(decode('123456', 20)) 
    print(decode('123456', 25)) 
    print(decode('123456', 30))
    print(decode('123456', 35)) 
    print(decode('123456', 36))    
    # print(encode(10,2))