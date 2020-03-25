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
        # create a new instance of BinarySearchTree w/ the new value 
        # if there's no Queue, then initialize one 
        # initialize variable current as the queue head
        # if new value is less than current.value, current becomes current.left
        # if new val < current.value & current.left==None, then current.left==BinarySearchTree(val) & break
        # if the new value is greater than current.value, current becomes current.right
        # if new val > current.value & current.right==None, then current.right==BinarySearchTree(val) & break

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # initialize var current as queue head
        # if target==current.value, return 1
        # if current==None, return 0
        # if target < current.value, current becomes current.left 
        # if target > current.value, current becomes current.left 
        # return True if total > than 0 else False 

    # Return the maximum value found in the tree
    def get_max(self):
        # start at the root 
        # intialize var current as head/root
        # while current is not None
        # current = current.right
        # if current is None, return no max/NA, or maybe just return (do nothing)
        # else return current.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # initialize current as head 
        # base case is None, so
        # if current is None, stop/do nothing/maybe return None 
        # call the function recursively in the return statement 


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
