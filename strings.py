#!python

# string.ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters = string.ascii_lowercase + string.ascii_uppercase

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    # If our pattern index is equal to our pattern length then we found a match and we can return True
    # If our current text character is not our pattern character and if we were checking for a pattern, we want to
    # reset the pattern and try again
    # If we have not found our pattern then we return False

    text_index = 0
    pattern_index = 0

    text_length = len(text)
    pattern_length = len(pattern)

    while text_index < text_length:  
        if text[text_index] == pattern[pattern_index]:
            pattern_index += 1
        elif pattern_index > 0:
            pattern_index = 0
            continue
        if pattern_index + 1 > pattern_length:
            return True
        text_index += 1
    return False

def index_of(text,pattern):
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)


    text_index = 0
    pattern_index = 0

    text_length = len(text)
    pattern_length = len(pattern)

    while text_index < text_length:  
        if text[text_index] == pattern[pattern_index]:
            pattern_index += 1
        elif pattern_index > 0:
            pattern_index = 0
            continue
        if pattern_index + 1 > pattern_length:
            return pattern_index
        text_index += 1
    return False

    # len_pattern = len(pattern)    

    # no need to have a dictionary way to implement it
    substrs = {}       
    for index in range(len(text)-len_pattern+1):
        substr = text[index:index+len_pattern]
        if substr not in substrs:
            substrs[substr] = index
    return substrs.get(pattern,None)


def index_of3(text, pattern):
    # """Return the starting index of the first occurrence of pattern in text,
    # or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # refactoring codes to implement other
    # check when is not the length of the txt
    # Loop through our text characters 
    # check if the text index is less than length of text
    # if the text of index is not equal to pattern
    # check on the text and pattern index
    # ababc 5  | text: abc 3
    # O(m*n) implementation
    # test case: (find_index('aaaaaab', 'aaab'))
    if pattern == '':
        return 0
    text_index = 0
    len_pattern = len(pattern)
    # when pattern is longer than text. 
    #The empty string case is handled by default but you could also hard code it 
    # to save N time or leave it as is for cleanliness.    
    for i in range(len_pattern):
        if text[text_index + i] != pattern[i]:
            break
        if i == len_pattern - 1:
            return text_index


def index_of2(text, pattern):
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # Check if empty; if so, return 0, earliest bit
    if len(pattern) == 0:
        return 0
    pattern = list(pattern)
    pattern_len = len(pattern)

    text = list(text)
    textext_len = len(text)

    shift = 0
    while(shift <= textext_len - pattern_len):
        index = pattern_len - 1
        # Keep going until it all meets
        while index >= 0 and pattern[index] == text[shift+index]:
            index -= 1
        # If we get past index, then return where the shift is
        if index < 0:
            return shift
        else:
            if text[shift+pattern_len-1] in pattern:
                shift += pattern_len - pattern.index(text[shift+pattern_len-1]) - 1
            else:
                shift += pattern_len
    return None
def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    indexes = []

    """consider the edge cases when it's an empty string"""
    # rational behind it: why we using it

    if pattern == '':
        for i in range(len(text)):
            indexes.append(i)
        return indexes
    # check the current pattern matche, if so check more of the pattern
    # check if we look the whole pattern.
    for text_index in range(len(text) - len(pattern) + 1):
        if text[text_index : text_index + len(pattern)] == pattern:
            indexes.append(text_index)
    return indexes


    # also works for the optization code below
    # return [text_index for text_index in range(len(text) - len(pattern) + 1)
    #         if text[text_index : text_index + len(pattern)] == pattern]
def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))
    print(find_index('aaaaaab', 'aaab'))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        # print('Usage: {} text pattern'.format(script))
        # print('Searches for occurrences of pattern in text')
        # print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        # print("contains('abra cadabra', 'abra') => True")
        # print("find_index('abra cadabra', 'abra') => 0")
        # print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")
        # print(find_all_indexes('abc', ''))

if __name__ == '__main__':
    main()
    print(contains('aaaaaab', 'aaab'))