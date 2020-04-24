import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # pass
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.value > target:
            if self.left != None:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right != None:
                return self.right.contains(target)
            else:
                return False

        # pass

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value
        # pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)
        # pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)
        if self.right:
            self.right.in_order_print(self.right)
        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        node_queue = Queue()
        node_queue.enqueue(node)

        while node_queue.len() > 0:
            remove_node = node_queue.dequeue()
            print(remove_node.value)
            if remove_node.left is not None:
                node_queue.enqueue(remove_node.left)
            if remove_node.right is not None:
                node_queue.enqueue(remove_node.right)
        # pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node_stack = Stack()
        node_stack.push(node)

        while node_stack.len() > 0:
            remove_node = node_stack.pop()
            print(remove_node.value)
            
            if remove_node.left is not None:
                node_stack.push(remove_node.left)
            if remove_node.right is not None:
                node_stack.push(remove_node.right)
        # pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
