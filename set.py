#!python


from linkedlist import Node, LinkedList
from hashtable import HashTable




class Set(object):
    def __init__(self, elements=None):
        # intilaize the size of the set, starts with intial size of 10 
        if elements is None:
            initial_size = 10
        else:
            initial_size = len(elements)
        #     
        self.data = HashTable(initial_size)
        for item in elements:
            if self.data.contains(item):
                continue
            else:
                self.data.set(item, None)

    def __str__(self):
        return str(self.data.keys())

    def set_contents(self):
        """Get the contents of the set [key inside a HashTable]"""
        return self.data.keys()

    def size(self):
        """Find size of the set"""
        return self.data.size

    def contains(self, element):
        """return a boolean contained inside of the set [key inside a HashTable]"""
        """Best case running time for contains is O(1) near beginning of set
        Worst case running time for contains O(n) near end of set """
        return self.data.contains(element)

    def add(self, element):
        """Add the element of the set"""
        # O (1)
        """Best case running time: O(1) near beginning of list of keys
        Worst case running time: O(n) near end of list of keys """
        if self.contains(element):
            return
        else:
            self.data.set(element, None)

    def remove(self, element):
        # Raise value error if not available
        if self.contains(element):
            self.data.delete(element)
        else:
            raise ValueError("Element not in set")

    def union(self, second_set):
        """Return a new  set, that is a union of first_set and second_set"""
        # O(n) since it goes through every item and has contains"""
        # create a new set that has the set conents
        result_set = self.set_contents()

        for item in second_set.set_contents():
            if self.contains(item):
                continue
            else:
                result_set.append(item)
        return Set(result_set)

    def intersection(self, second_set):
        """Return a new set, that is intersection of this set and second_set."""
        """O(n) since it goes through every item and has contains"""
        # create an empty set
        result_set = []
        for item in second_set.set_contents():
            # check if the set contains the item 
            if self.contains(item):
                result_set.append(item)
            # else:
            #     return ValueError("Set is empty")
        return Set(result_set)

    def is_subset(self, second_set):
        """Return True if second set is a subset of this set,else False"""
        # O(n); goes through every item and has contains
        # Compariing the size of the 2 set  
        # to make sure if set is in the second set
        # for bucket in self.buckets:
            # for element in bucket.iterate():
            #     if not other.contains(element)
        if self.size() <= second_set.size():
            for item in self.set_contents():
                if second_set.contains(item):
                    continue
                else:
                    return False
            return True
        else:
            return False

# set_set_test = Set()
set_test = Set([1, 2, 3, 4, 5,6,7,8,9,10])
set_test2 = Set([ 11,12])
test_intersection = set_test.intersection(set_test2)
print(test_intersection)
set_test2 = Set([6, 7, 8,9,10])

print(set_test)
print(set_test2)

set_test.add(1)
print(set_test)
print(set_test.intersection(set_test2))
print(set_test.union(set_test2))

print(set_test.is_subset(set_test2))

set_test = Set([1, 2, 3])
set_test2 = Set([1, 2, 3, 4, 5, 6, 7, 8])
print(set_test.is_subset(set_test2))

set_test = Set([1, 2, 3])
set_test2 = Set([1, 2, 3])
print(set_test.is_subset(set_test2))

set_test = Set([1, 2, 3, 4])
set_test2 = Set([1, 2, 3])
print(set_test.is_subset(set_test2))

set_test = Set([1, 2, 3, 4, 5])
set_test2 = Set([4, 5, 6, 7, 8])
print(set_test.is_subset(set_test2))

