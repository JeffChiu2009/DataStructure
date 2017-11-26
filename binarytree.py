#!python
from queue import LinkedQueue, DeQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Best and worst case running time: O(N) under what conditions?"""

        # Base case
        if self.is_leaf():
            return 0
        # Return one more than the greater of the left height and right height
        return calculate_height_recursively(node)


class BinarySearchTree(object):
    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        n; going to go through everything"""
        #  Check if root node has a value and if so calculate its height
        return self.root.height()

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        log(n): it's going to traverse based on height, which is log(n) """
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        log(n): it's going to traverse based on height, which is log(n)"""
        # Find a node with the given item, if any
        node = self._find_node(item)
        # Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        If it's empty, well, it's 1
        Otherwise, log(n); we know where we're heading"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # Create a new root node
            self.root = BinaryTreeNode(item)
            # Increase the tree size
            self.size += 1
            return
        # Grab parent of where node should be
        parent = self._find_parent_node(item)
        # Check if the given item should be inserted left of parent node
        if item < parent.data:
            parent.left = BinaryTreeNode(item)
        # Check if the given item should be inserted right of parent node
        elif item > parent.data:
            parent.right = BinaryTreeNode(item)

        self.size += 1


    def delete(self, item):
        """Delete an item from the binary search tree, or assert ValueError if item does not exit"""
        if self.root.data == item:
            self.root = None
            self.size = 0
            print("Uprooted.")

        if self.root is None:
            assert ValueError("Can not delete from an empty binary search tree")

        # Assert ValueError if the node was not found
        # if self.deleted_node is None:
        #     assert ValueError("Item does not exist in the binary search tree")

        parent = self._find_parent_node(item)
    
        if parent is None:
            return
        # Delete the item
        elif parent.left.data is item:
            deleted_node = parent.left
            if deleted_node.is_leaf():
                deleted_node = None
            elif parent.left.is_branch():
                parent.left = deleted_node.right
                parent.left.left = deleted_node.left
        elif parent.right.data is item:
            deleted_node = parent.right
            if deleted_node.is_leaf():
                deleted_node = None
            elif parent.right.is_branch():
                parent.right = deleted_node.right
                parent.right.left = deleted_node.left
        self.size -= 1
        return

    def _find_node(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found.
        Best case running time: O(1) when item is root node
        O(log(n)); the find_node goes through a certain series, so we only
        need to go a certain distance"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Descend to the node's left child
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found."""

        # Check if the NODE HAS WHAT we are looking for
        if node.data == item:
            return node
        # If current node is a leaf and we haven't found the item, return None
        if node.is_leaf():
            return None
        
        left_sub = self._find_node_recursive(item, node.left)
        right_sub = self._find_node_recursive(item, node.right)

        # recurse if the left subtree is not none
        # else return none when there is none
        if left_sub is not None:
            return left_sub
        elif right_sub is not None:
            return right_sub
        else:
            return None

    def _find_parent_node(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
         Best case running time: O(N) under what conditions?
         Worst case running time: O(N) under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # Check if the given item is less than the node's data
            elif item < node.data:
                # Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # Check if the given item is greater than the node's data
            elif item > node.data:
                # Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node."""
        # If current node is a leaf and we haven't found the item, return None
        if node is None:
            return None
        if node.data == item:
            return parent
        elif item < node.data:
            if node.left is None:
                return node
            return self._find_parent_node_recursive(item, node.left, node)
        elif item > node.data:
            if node.right is None:
                return node
            return self._find_parent_node_recursive(item, node.right, node)

    # This space intentionally left blank (please do not delete this comment)

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            items = self._traverse_in_order_recursive(self.root, items)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
         Running time: O(N) Why and under what conditions?
         Memory usage: O(d) where d is the depth of the tree, 
         (the number of levels in the tree from the root node down to the lowest node). 
         So we could say our space cost is O(d). """
        # Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # Visit this node's data with given function
        visit.append(node.data)
        # Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_in_order_recursive(node.right, visit)

        return visit


    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
         Running time: O(N) Why and under what conditions?
         Memory usage: O(N) Why and under what conditions?"""
        #  Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            items = self._traverse_pre_order_recursive(self.root, items)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.

         Running time: O(N) Why and under what conditions?
         Memory usage: O(N) Why and under what conditions?"""
        # Visit this node's data with given function
        visit.append(node.data)
        #  Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_pre_order_recursive(node.left, visit)
        #  Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_pre_order_recursive(node.right, visit)
        return visit

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(N) Why and under what conditions?
        TODO: Memory usage: O(N) Why and under what conditions?"""
        # Traverse pre-order without using recursion (stretch challenge)
        # [8, 4, 2, 1, 3, 6, 5, 7, 12, 10, 9, 11, 14, 13, 15]
        queue = DeQueue()
        queue.enqueue_front(node)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_iterative(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
         Running time: O(N) Why and under what conditions?
         Memory usage: O(N) Why and under what conditions?"""
        #  Traverse left subtree, if it exists
        if node.left is not None:
            self._traverse_post_order_recursive(node.left, visit)
        #  Traverse right subtree, if it exists
        if node.right is not None:
            self._traverse_post_order_recursive(node.right, visit)
        #  Visit this node's data with given function
        visit.append(node.data)
        return visit

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        Running time: O(n)
        Memory usage: Half of the tree. It goes down one half before another
        """
        # Traverse post-order without using recursion (stretch challenge)
        stack = DeQueue()
        # It was this, or make sure visit's len is same as the tree
        while True:
            # If the node is valid, grab right and left
            while node:
                if node.right:
                    stack.enqueue_front(node.right)
                stack.enqueue_front(node)
                node = node.left
            # If it's null, start dequeues
            else:
                node = stack.dequeue_front()
                # I don't even care at this point, just move the stack around
                # Originally, it would be left, parent, right;
                # needed left, right, node
                if node.right and node.right == stack.front():
                    stack.dequeue_front()
                    stack.enqueue_front(node)
                    node = node.right
                else:
                    # Put that in the visit. It's ALWAYS going to do this
                    # as a last case scenario
                    visit(node.data)
                    node = None

            if stack.length() == 0:
                break

            # print(stack.list, visit, "\n\n")

        return visit


    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
         Running time: O(n) Why and under what conditions?
         Memory usage: O(n) Why and under what conditions?"""
        # Create queue to store nodes not yet traversed in level-order
        """Remove and return the item at the back of this queue,"""
        queue = DeQueue()
        queue.enqueue_front(start_node)
        while queue.is_empty() == False:
            node = queue.dequeue_front()
            visit(node.data)
            if node.left != None:
                queue.enqueue_back(node.left)
            if node.right != None:
                queue.enqueue_back(node.right)


def calculate_height_recursively(node):
# https://stackoverflow.com/questions/21011423/how-to-calculate-the-height-of-a-bst-in-python
    if node is None:
        return 0
    else:
        return 1 + max(calculate_height_recursively(node.left), calculate_height_recursively(node.right))



def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    #items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()