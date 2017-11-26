#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # solution #1 is to do the the if statement to check the value
    # check if the item is not found 
    # set the current value to the current index

    # if index > len(array) - 1:
    #     return None   # not found
    # current_value = array[index]
    # if current_value == item:  
    #     return index  # found
    # return linear_search_recursive(array, item, index + 1)
    # solution #2 is to use enumeration
    # loop over all array values until item is found
    # this function expects us to return something
    # even though python does return something
    # python way of combining things together
    # index = 0
    # for index in range(len(array)):
    #     if array[index] == item:
    #     return index 
    # return None    
    # what is the condition of the item
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests
    # recursion
    # check until the empty list 
    # exhaust the entire list
    # interesting recursion code

    if index >= len(array):
        return None
    # Found item
    if array[index] == item:
        return index
    return linear_search_recursive(array[1:], item)
    # check if the index is out of the bound.
    # good idea for once, it becomes stack-overflow

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
def binary_search_iterative(array, item):
    """iteratively return the index of the item with binary search or None if not found"""
    # Sorted array that has to be the condition
    # go through several iteration until we found this
    # First, set the lower_index = 0 
    # upper_index as the length of array -1 
    lower_index = 0
    upper_index = len(array) - 1
    # iteration until it is found
    while lower_index <= upper_index:
        # calculate the middle index by sum the lower_index and upper_index and divide by 2
        middle_index = (lower_index + upper_index) // 2 # // is int division
        # check if the item is found
        if array[middle_index] == item:
            return middle_index
        elif array[middle_index] < item:
            lower_index = middle_index + 1
        elif array[middle_index] > item:
            upper_index = middle_index - 1

    # Did not find
    return None

    # you cannot put a variable at the arugument  
    # but you can put it down
def binary_search_recursive(array, item, lower_index=None, upper_index=None):
    """iteratively return the index of the item with binary search or None if not found"""
    """Best case Omega(1)"""
    """Worst case O(log(n))"""

    if lower_index is None or upper_index is None:
        lower_index = 0
        upper_index = len(array) - 1

    # None found
    if lower_index > upper_index:
        return None

    # Create middle index
    middle_index = (lower_index + upper_index) // 2

    # check out the different comparisons
    if array[middle_index] == item:
        return middle_index
    elif array[middle_index] > item:
        return binary_search_recursive(array, item, lower_index, middle_index - 1)
    elif array[middle_index] < item:
        return binary_search_recursive(array, item, middle_index + 1, upper_index)


def binary_search(array, item):
    if not array:
        return False
        
    return binary_search_ranges(array, item, 0, len(array)-1)
    
def binary_search_ranges(array, item, start, stop):
    middle = (start+stop)//2
    
    if item == array[middle]:
        return True
    elif start >= stop:
        return False
    elif item < array[middle]:
        return binary_search_ranges(array, item, start, middle-1)
    else:
        return binary_search_ranges(array, item, middle+1, stop)
