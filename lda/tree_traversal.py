#!/usr/bin/env python

'''Node class.  Does cool stuff while you watch.'''
class Node:
    '''This is a node class.'''
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# InOrder tree traversal
def printInOrder(root):

    if root: 
        
        # recurse on left child
        printInOrder(root.left)
        
        # print data val for the node
        print(root.val)

        # recurse on the right child
        printInOrder(root.right)






  
