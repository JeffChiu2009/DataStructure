#!python

from itertools import islice, tee

def pairwise(iterable):
# helper function for doing various conversion
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.prev = None  # double linked list

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))

    def setHead(self,head):
        self.head = head

        # return the next data in the node 
    def getNext(self):
        return self.next 

    def setNext(self,next):
        self.next = next

    def setData(self,data):
        self.data = data
class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        self.head = None
        self.tail = None
        self.size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list"""
        # stick my stuff inside linkedList
        # 
        return 'LinkedList({})'.format(self.as_list())

    def setHead(self,head):
        self.head = head

    def getNext(self):
        return self.next 

    def setNext(self,next):
        self.next = next
     
    def _internal_iter(self):
        #iterable function
        #Refactoring the code 
        # remove while not found and current is not None:
        # and make an internal iterable function
        node = self.head
        while node is not None:
            yield node
            node = node.next

# Most of my functions if given a previous node, should be O(1). 
# The biggest exceptions to these are _internal_iter and _get_index.
    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        #"""Worst case O(n)"""
        result = [] 
        node = self.head  
        while node is not None:  
            result.append(node.data)  #
            node = node.next  
        return result 

    # def __getitem__(self, arg):
    #     """Get the item at the index, or raise KeyError if not an int"""
    #     """Best case Omega(1)"""
    #     """Worst case O(n)"""
    #     if type(arg) is not int:
    #         raise TypeError

    #     # If argument is over list size, raise ValueError
    #     if arg >= self.length() or arg < -self.length():
    #         raise IndexError

    #     # Use modulus operator, so index can use negatives
    #     counter = arg % self.length()
    #     currentIndex = 0

    #     if counter == self.length():
    #         return self.last()

    #     current = self.head
    #     while current is not None:
    #         if counter == currentIndex:
    #             return current.data
    #         currentIndex += 1
    #         current = current.next
    def as_list(self):
        """Return a list of all items in this linked list"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        items = []
        current = self.head
        while current is not None:
            items.append(current.data)
            current = current.next
        return items

    def _get_index(self, index):
        """ Gets data at an index"""
        if type(index) is not int:
            raise TypeError
        length = len(self) + 1
        if not (-length <= index < length):
            raise IndexError('')
        index %= length
        if index == (length - 1):
            return self._tail
        return next(islice(self._internal_iter(), index, None))

    def is_empty(self):
        """Return True if this linked list is empty, or False otherwise"""
        """Best case Omega(1)"""
        """Worst case O(1)"""
        return self.head is None

    def length(self):
        """Return the length of this linked list"""
        """Best case Omega(1)"""
        """Worst case O(1)"""
        return self.size

    # def append(self, item):
    #     self.insert(len(self), item)

    # def prepend(self, item):
    #     self.insert(0, item)

    # uncomment for longer implementation
    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        """Best case Omega(1)"""
        """Worst case O(1)"""
        new_node = Node(item)
        # Insert before head node
        new_node.next = self.head
        # Update head node
        self.head = new_node
        # Check if list was empty
        if self.tail is None:
            self.tail = new_node
        # Update length
        self.size += 1


    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        #method for inserting a new node at the end of a Linked List   
        """Best case Omega(1)"""
        """Worst case O(1)"""

        #If head is empty(empty list), make head new node, 
        # else find last node and make new node as its next

        # if not self.head:
        #     self.setHead(Node(item))
        #     self.head.setData(item)
        #     return self.head
        # cur = self.head
        # while cur.getNext():
        #     cur = cur.getNext()
        # nextNode = Node(item)
        # nextNode.setData(item)
        # cur.setNext(nextNode)
        # self.head
        # self.size += 1

        # old implementation
        new_node = Node(item)
        # set the head to the newNode
        if self.head is None:
            self.head = new_node
        # Otherwise insert after tail node
        else:
            self.tail.next = new_node
        # Update tail node
        self.tail = new_node
        # Update length
        self.size += 1


    def size(self):
        """ Gets the size of the Linked List
        AVERAGE: O(1) """
        return self.count

    # def delete_at_index(self, index):
    #     """Delete the item at the given index from this linked list, or raise ValueError"""

    #     if type(index) is not int:
    #         raise TypeError

    #     # If argument is over list size, raise ValueError
    #     if index >= self.length() or index < -self.length():
    #         raise IndexError

    #     # Use modulus operator, so index can use negatives
    #     counter = index % self.length()
    #     currentIndex = 0

    #     current = self.head
    #     previous = None
    #     found = False

    #     # Find the given item
    #     while not found and current is not None:
    #         if currentIndex == counter:
    #             found = True
    #         else:
    #             previous = current
    #             current = current.next
    #             currentIndex += 1
    #     if found:
    #         if current is not self.head and current is not self.tail:
    #             previous.next = current.next
    #             current.next = None
    #         if current is self.head:
    #             self.head = current.next
    #         if current is self.tail:
    #             if previous is not None:
    #                 previous.next = None
    #             self.tail = previous
    #         # Update length
    #         self.size -= 1
    #     else:
    #         raise ValueError('Item not found: {}'.format(item))

    def __delitem__(self, index, item):
    # """Delete the item at the given index from this linked list, or raise ValueError"""

        prev = self._get_index(index)
        curr = prev.next
        prev.next = curr.next
        self.size -=1
        if prev.next is None:
            self.tail = prev
        return curr.data


    def _find_node(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next
    ###My implementation###


    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1) if it's head or no value,  
        Worst case running time: O(n) if it's in the tail [TODO]"""
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        counter = self.head
        for i in range(index):
            counter = counter.next
        return counter.data
        # if not (0 <= index <= self.size):
        #     raise ValueError('List index out of range: {}'.format(index))
        # counter = self.head
        # for i in range(index):
        #     counter = counter.next
        # return counter.data

    def insert(self, index, item):
        """ Inserts data at a specific index
        BEST: O(1)
        WORST: O(i -1)
        """
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        node = Node(item)
        prev = self.get_at_index(index)

        if index == 0:
            self.prepend(item)
        elif index == self.size:
             self.append(item)
        else:
            new_node = Node(item)
            node = self.head
            previous = None
            for i in range(index):
                previous = node
                node = node.next
            previous.next = new_node
            new_node.next = node
            self.size += 1

        # node.next = prev.next
        # prev.next = node
        # if node.next is None:
        #     self._tail = node
        # self._size += 1

    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: O(1), depends on the order of the index, if the index it's head or tail,  
        Worst case running time: O(i -1) if not head or tail, then it's case  """
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # curr_node and next_node
        # prev_node with the doubly LL
        # refactoring the code if i in the index for range in
        if index == 0:
            self.prepend(item)
        elif index == self.size:
            self.append(item)
        else:
            new_node = Node(item)
            node = self.head
            previous = None
            for i in range(index):
                previous = node
                node = node.next
            previous.next = new_node
            new_node.next = node
            self.size += 1

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        current = self.head
        previous = None
        found = False
        # Find the given item
        while not found and current is not None:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        # Delete if found
        if found:
            if current is not self.head and current is not self.tail:
                previous.next = current.next
                current.next = None
            if current is self.head:
                self.head = current.next
            if current is self.tail:
                if previous is not None:
                    previous.next = None
                self.tail = previous
            # Update length
            self.size -= 1
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


    # def delete(self, value):
    #     for prev, curr in pairwise(self._internal_iter()):
    #         if curr.data == value:
    #             prev.next = curr.next
    #             self.size -=1
    #             if prev.next is None:
    #                 self.tail = prev
    #             return
    #     raise ValueError('Item not found: {}'.format(value))


    # def replace(self, value, item):
    #     """Replace the given old_item in this linked list with given new_item
    #     using the same node, or raise ValueError if old_item is not found.
    #     Best case running time: O(1) under head and tail
    #     Worst case running time: O(n) under the head """
    #     for node in islice(self._internal_iter(), 1, None):
    #         if node.data == value:
    #             node.data = item
    #             return
    #     raise ValueError('Item not found: {}'.format(value))

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found."""
        if old_item == new_item:
            raise ValueError('Item not found: {}'.format(old_item))
        node = self.head
        while node is not None:
            if node.data == old_item:
                node.data = new_item
                return
            node = node.next
        raise ValueError('Item not found: {}'.format(old_item))
    # he did not run the test, and I did not run the test
    def find(self, condition):
        """Return an item in this linked list satisfying the given condition"""
        """Best case Omega(1)"""
        """Worst case O(n)"""
        current = self.head  # Start at the head node
        while current is not None:
            if condition(current.data):
                return current.data
            current = current.next  # Skip to the next node
        return 


def test_linked_list():
    ll = LinkedList()
    print(ll)
    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('testing: Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print("testing: Linked List replace ___________________")
    ll = LinkedList(['A', 'B', 'C'])
    ll.replace('A', 'D')
    print(ll)

    ll = LinkedList(['A', 'B', 'C'])
    print(ll)
    print("testing: insert_at_index ___________________")
    print('size: {}'.format(ll.size))
    ll.insert(0, 'AA')
    print(ll)
    print("testing: insert_at_index 0, 'AA'___________________")
    ll.insert(2, 'BB')
    print("testing: insert_at_index 2, 'BB'___________________")
    print(ll)

if __name__ == '__main__':
    test_linked_list()