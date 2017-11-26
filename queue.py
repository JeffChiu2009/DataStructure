from linkedlist import LinkedList

class LinkedQueue(object):
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.size == 0

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        # Running time: O(1) – Constant time to add to a item to the tail"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Running time: O(1) In most cases, just adding an item in the front
        # append method it's from the head, it's efficiient
        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) In all cases, - since it's head  """
        # we remove from the head (most efficient cases)
        # it's a better strategy to do that
        if self.is_empty():
            raise ValueError("Cannot dequeue, queue is empty.")
        item = self.list.head.data
        self.list.delete(item)
        return item

# Implement ArrayQueue below, then change the assignment at the bottom
# to use this Queue implementation to verify it passes all tests
class ArrayQueue(object):
    # I did it through the append to the last
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list == list()

    def length(self):
        """Return the number of items in this queue."""
        return len(self.list)

    def enqueue(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) – Average running time. (In most cases at the resizing method,) 
         just adding to the end of the list which is a constant time operation."""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""

        if self.is_empty():
            return None
        return self.list[0]

    def dequeue(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(n) – Item is being removed from front of the array,
        that means all subsequent items have to be shifted left one index."""
        if self.is_empty():
            raise ValueError("Cannot dequeue, queue is empty.")
        return self.list.pop(0)



class DeQueue(object):
    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue_back(item)

    def __repr__(self):
        """Return a string representation of this queue."""
        return 'Queue({} items, front={})'.format(self.length(), self.front())

    def is_empty(self):
        """Return True if this queue is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this queue."""
        return self.list.size

    def enqueue_back(self, item):
        """Insert the given item at the back of this queue.
        Running time: O(1) - just does prepend, which is O(1)"""
        self.list.prepend(item)

    def enqueue_front(self, item):
        """Insert the given item at the front of this queue.
        Running time: O(1) - just does append, which is O(1)"""
        self.list.append(item)

    def front(self):
        """Return the item at the front of this queue without removing it,
        or None if this queue is empty."""
        # Running time: O(1) – Average running time. In most cases, just adding

        if self.is_empty():
            return None
        return self.list.tail.data

    def back(self):
        """Return the item at the back of this queue without removing it,
        or None if this queue is empty."""
        #  Running time: O(1) - since it's head. 

        if self.is_empty():
            return None
        return self.list.head.data

    def dequeue_front(self):
        """Remove and return the item at the front of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) - since tail, it happens easily
        If this is a singly-linked list, it would take O(n)"""
        if self.is_empty():
            raise ValueError
        output = self.list.tail.data
        self.list.delete(self.list.tail.data)
        return output
    def dequeue_back(self):
        """Remove and return the item at the back of this queue,
        or raise ValueError if this queue is empty.
        Running time: O(1) - since this is the head."""
        if self.is_empty():
            raise ValueError
        output = self.list.head.data
        self.list.delete(self.list.head.data)
        return output

#Queue = DeQueue
Queue = LinkedQueue
q = Queue()
print(q.list)
q.enqueue('E')
print(q.list)
q.enqueue('A')
q.enqueue('T')
print(q.list)
q.dequeue()
print(q.list)



# Queue = ArrayQueue
