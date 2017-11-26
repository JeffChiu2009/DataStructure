#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()
        # TODO: Check if empty

    def length(self):
        """Return the number of items in this stack."""
        return self.list.size

    def push(self, item):
        """Insert the given item on the top of this stack."""

        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty.
        Running time: O(1) – Adding item at end is constant operation because
        """
        if self.is_empty():
            return
        return self.list.tail.data

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) at head except when it is downsizing the size of the memory"""
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        item = self.peek()
        self.list.delete(item)
        return item



    # def __init__(self):
    #     self.stk = []

    # def pop(self):
    #     """raises IndexError if you pop when it's empty"""
    #     return self.stk.pop()

    # def push(self, elt):
    #     self.stk.append(elt)

    # def is_empty(self):
    #     return len(self.stk) == 0

    # def peek(self):
    #     if not self.stk.is_empty():
    #         return self.stk[-1]

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
# allocating size can get an exponential size
# just appending a thing
# the timing of resizing stretches out
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)


    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Putting something on top of list is O(1)"""
        #Running time: It depends – Depends on the number of allocation
        # num reallocation depends on the inti size of the array
        # and how you resize it
        # and when to Add item at end is constant operation because
        # (doubling the size) of the array is a good strategy
        #we track the tail of the list"""
        # make sure that I pre-pend it
        self.list.insert(self.length(), item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        size = self.length()
        if size == 0:
            return None
        return self.list[(size-1)]

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Popping is just taking out the last bit; O(1)"""
        # do this when you implement it

        size = self.length()
        if size == 0:
            raise ValueError
        return self.list.pop((size-1))


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
s = Stack()
print('length, {}'.format(s.length())) #== 0
s.push('A')
print(s)
print('length, {}'.format(s.length())) #== 1
s.push('B')
print(s)
print('length, {}'.format(s.length())) #== 2
s.pop()
print('length, {}'.format(s.length())) #== 1
print(s)
s.pop()
print(s)
print('length, {}'.format(s.length())) #== 0
print(s)