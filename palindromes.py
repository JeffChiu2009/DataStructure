import string
    # Hint: Use these string constants to ignore capitalization and/or punctuation

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing"""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # assert isinstance(text, str)
    assert isinstance(text, str)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)

    #very wasteful implementation
# def is_palindrome(text):
#     """returns True if the text is a palindrome, with punctuation omitted"""
#     # brute force way of solving palindrome
#     text = ''.join([index for index in text.lower() if index in string.ascii_letters])
#     return text == text[::-1]
#     return True


def ascii_letters(text):
    #This method return true if all characters in the string are alphabetic
    # (if the string is an uppercase or lowercase letter from A to Z)
    # otherwise it will return False (the string contains any non-letter character)  
    string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string.ascii_letters = string.ascii_lowercase + string.ascii_uppercase
    for index in text:
        if index in string.ascii_letters:
            return True
    return False

def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests    
    # First, set up the first_index and
    # last_index as the length of array -1  
    # Inside each iteration, compared the 2 pointers, and see if it's a palindrome    
    # to handle the different casing and punctuation: 
    # Called the helper function checks if index is ascii_letters or alphabetic
    first_index = 0
    last_index = len(text) - 1

    # checking the valid condition for the range
    while(first_index <= last_index):

        left = text[first_index]
        right = text[last_index]
        while not ascii_letters(left):
            first_index += 1
            if first_index > len(text) - 1:
                return True
        # check if the first pointer is not alphabetic or ascii_letters
        while not ascii_letters(right):
            last_index -= 1
            if last_index < 0:
                return True

        # if the pointer are not the same, return false
        if(left.lower() != right.lower()):
            return False
        first_index += 1
        last_index -= 1
    return True

def is_palindrome_recursive(text, first_index=None, last_index=None):
    # TODO: implement the is_palindrome function recursively here
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests
    # First, we have the first_index and last_index as None 
    # set the index for the 2 pointer
    # Inside the recursion, compared the 2 pointers, which check if it's a palindrome 
    # return fales   
    # to handle the different casing and punctuation: 
    # Called the helper function checks if index is ascii_letters or alphabetic
    if first_index is None or last_index is None:
        first_index = 0
        last_index = len(text) - 1
    # Base Cases
    if first_index >= last_index:
        return True
    # Check letters
    left = text[first_index]
    right = text[last_index]
    update_left = first_index + 1
    update_right = last_index - 1
    # check if the left pointer is not alphabetic or ascii_letters
    # if not, update the left pointer
    if not ascii_letters(left):
        return is_palindrome_recursive(text, update_left, last_index)
    # check if the right pointer is not alphabetic or ascii_letters
    # If not, update the right pointer
    if not ascii_letters(right):
        return is_palindrome_recursive(text, first_index, update_right)

    # Check if the left and right pointers are not the same
    # Not same, return false
    if(left.lower() != right.lower()):
        return False

    return is_palindrome_recursive(text, update_left, update_right)

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            str_not = 'a' if is_pal else 'not a'
            print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # uncomment to test the ascii_letter function
    # print(ascii_letters("a"))
    # print(ascii_letters(" "))
    main()