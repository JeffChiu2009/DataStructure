class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None
        self.last = None

    def __repr__(self):
        """Return a string rxepresentation of this node"""
        return 'Node({})'.format(repr(self.data))


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None
        self.count = 0

        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'DoublyLinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of adll items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        return self.count

    def append(self, item):  # O(1)
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)  
        self.count += 1  

        if self.head is None:  
            self.head = new_node  
        else:
            self.tail.next = new_node  
            new_node.last = self.tail

        self.tail = new_node  

    def prepend(self, item):  # O(1)
        """Insert the given item at the head of this linked list"""
        new_node = Node(item)   
        self.count += 1  

        if self.head is None:  
            self.head = new_node  
            self.tail = self.head  
        else:  
            new_node.next = self.head  
            self.head = new_node  

    def delete(self, item):  # O(N)
        """Delete the given item from this linked list, or raise ValueError"""
        last = None
        current_node = self.head

        while current_node is not None:  # O(N)
            # The current node is the ones we are looking for
            if current_node.data == item:  
                # Our tail is our current node
                if self.tail == current_node:  
                    self.tail = last  

                if last is None:  
                    # If we are the head. We set the new head to the next value.
                    self.head = current_node.next  
                else:
                    # We aint the head so we set the last nodes head to the next node 
                    last.next = current_node.next  

                    if current_node.next is not None:
                        current_node.next.last = last

                self.count -= 1  
                return  # Stop checking. Don't return an error

            last = current_node  
            current_node = current_node.next  

        raise ValueError

    def size(self):
        """ Gets the size of the Linked List
        AVERAGE: O(1)
        """
        return self.count

    def _at_index(self, index):
        """ Helper method used to get the node at an index


        """
        next_node = self.head

        while index > -1 or next_node is not None:
            if index == 0:
                return next_node

            next_node = next_node.next
            index -= 1

        return None

    def at_index(self, index):
        """ Gets data at an index


        """
        at_index = self._at_index(index)

        if at_index is None:
            return None

        return at_index.data

    def insert(self, index, data):
        """ Inserts data at a specific index
        """
        if index == 0:
            self.prepend(data)
            return

        at_index = self._at_index(index - 1)

        if at_index is None:
            raise IndexError

        if at_index.next is None:
            self.append(data)
            return

        new_node = Node(data)

        if at_index.next is not None:
            at_index.next.last = new_node

        new_node.next = at_index.next
        at_index.next = new_node

        new_node.last = at_index

    def find(self, quality):  # O(N)
        """Return an item from this linked list satisfying the given quality"""
        current = self.head  

        while current is not None:  # O(N)
            if quality(current.data):  # We no know
                return current.data  

            current = current.next  

    def reverse(self):
        next_node = self.head.next

        previous_node = self.head

        self.tail = previous_node

        self.head.next = None

        while next_node is not None:
            current_node = next_node
            next_node = current_node.next
            previous_node.last = current_node
            current_node.next = previous_node
            previous_node = current_node
        self.head = previous_node
        self.head.last = None

    def _find(self, data):
        """ Finds a node with data or returns None if we can't find a node """
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

    def replace(self, old_data, new_data):
        """ Replaces data with new data """
        old_node = self._find(old_data)

        # If we can't find the node then we raise an error
        if old_node is None:
            raise ValueError

        old_node.data = new_data



def test_DoublyLinkedList():
    dll = DoublyLinkedList()
    print(dll)
    print('Appending items:')
    dll.append('A')
    print(dll)
    dll.append('B')
    print(dll)
    dll.append('C')
    print(dll)
    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('size: {}'.format(dll.size))
    print('length: {}'.format(dll.length()))

    print('Deleting items:')
    dll.delete('B')
    print(dll)
    dll.delete('C')
    print(dll)
    dll.delete('A')
    print(dll)
    print('head: {}'.format(dll.head))
    print('tail: {}'.format(dll.tail))
    print('size: {}'.format(dll.size))
    print('length: {}'.format(dll.length()))

    print("testing: DoublyLinkedList replace ___________________")
    dll = DoublyLinkedList(['A', 'B', 'C'])
    dll.replace('A', 'D')
    print(dll)

    dll = DoublyLinkedList(['A', 'B', 'C'])
    print(dll)
    print("testing: insert_at_index ___________________")
    print('size: {}'.format(dll.size))
    dll.insert(0, 'AA')
    print(dll)
    print("testing: insert_at_index 0, 'AA'___________________")
    dll.insert(2, 'BB')
    print("testing: insert_at_index 2, 'BB'___________________")
    print(dll)

if __name__ == '__main__':
    test_DoublyLinkedList()