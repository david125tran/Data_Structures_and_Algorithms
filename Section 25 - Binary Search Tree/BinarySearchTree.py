'''
Binary Search Tree
    *In the left subtree the value of a node is less than or equal to its parent node's value
    *In the right subtree the value of a node is greater than its parent node's value
    *Performs faster when inserting and deleting nodes because traversing it is faster 

          RootNode
           /     \
          /       \
         /         \
Left subtree    Right subtree
'''

import LinkedListQueue as queue

class BSTNode:
    def __init__(self, data):
        '''
        Creates a new node for a binary search tree.
        To create a new BST, call the BSTNode class to create a new node and pass in data=None.
        '''
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    '''Inserts a new node (nodeValue) into a binary search tree that has a root node (rootNode)'''
    if rootNode.data == None:                               # If 
        rootNode.data = nodeValue                               # The root node's data is empty, we make the new node the root node
    elif nodeValue <= rootNode.data:                        # Elif
        if rootNode.leftChild is None:                          # If the data is less than or equal to the root and there is not a left child
            rootNode.leftChild = BSTNode(nodeValue)             # It becomes a left child
        else:                                               # Else
            insertNode(rootNode.leftChild, nodeValue)           # There is a left child already, so we call the insertNode() function recursively on the left child
    else:                                                   # Else
        if rootNode.rightChild is None:                         # If the data is greater than the root and there is not a right child
            rootNode.rightChild = BSTNode(nodeValue)            # It becomes a right child
        else:                                               # Else
            insertNode(rootNode.rightChild, nodeValue)          # There is a right child already, so we call the insertNode() function recursively on the right child
    return "The node has been successfully inserted"

def preOrderTraversal(rootNode):
    '''
    Traverses a binary search tree from:
    Root -> Left subtree -> Right subtree
    '''
    if not rootNode:
        return                                  # Creates an exit for the recursion
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    '''
    Traverses a binary search tree from:
    Left subtree -> Root -> Right subtree
    '''
    if not rootNode:
        return                                  # Creates an exit for the recursion
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    '''
    Traverses a binary search tree from:
    Left subtree -> Right subtree -> Root
    '''
    if not rootNode:
        return                                  # Creates an exit for the recursion
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    '''
    Traverses a binary search tree from:
    Top to Bottom from Left to Right
    Using a linked list
    '''
    if not rootNode:
        return      
    else:
        customQueue = queue.LinkedListQueue()       # Uses our LinkedListQueue
        customQueue.enqueue(rootNode)                   # Adds the root to the LLQ
        while not(customQueue.isEmpty()):                   # Keep looping while there are nodes
            root = customQueue.dequeue()                        # Removes the root from the LLQ
            print(root.value.data)                              # Print that root's data 
            if root.value.leftChild is not None:            # If there is a left child:
                customQueue.enqueue(root.value.leftChild)         # Print the left child's data
            if root.value.rightChild is not None:           # if there is a right child:
                customQueue.enqueue(root.value.rightChild)        # Print that child's data

def searchNode(rootNode, nodeValue):
    '''Searches a binary search tree (rootNode) for a value (nodeValue)'''
    if rootNode == None:                                                # If the BST is empty
        return "The node value does not exist in the BST"
    else:
        if rootNode.data == nodeValue:                              # If the value is found in the current node's data
            return "Found"                                                  # Look no further, exit
        elif nodeValue < rootNode.data:                             # Elif the nodeValue is less than the current node's data, check the left child
            if not rootNode.leftChild:                                      # If there is not a left child, the value can't exist
                return "Not Found"                                          # Exit
            elif rootNode.leftChild.data == nodeValue:                  # Elif the value is found in the left node's data
                return "Found"                                              # Look no further, exit
            else:                                                       # Else
                return searchNode(rootNode.leftChild, nodeValue)            # Enter into the left child subtree
        else:                                                       # If the nodeValue is mpre than the current node's data, check the right child
            if not rootNode.rightChild:                                     # If there is not a right child, the value can't exist
                return "Not Found"                                          # Exit
            elif rootNode.rightChild.data == nodeValue:                 # Elif the value is found in the left node's data
                return "Found"                                              # Look no further, exit
            else:                                                       # Else
                return searchNode(rootNode.rightChild, nodeValue)           # Enter into the right child subtree

def minValueNode(bstNode):
    '''Takes a node (bstNode) from a binary search tree and then returns the minimum node from the branch of the node passed in'''
    current = bstNode
    while (current.leftChild is not None): # The minimum value exists at the lowest left child.  Keep looping until you find the lowest level left child.
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    '''Takes a binary search tree (rootNode) and a node value that you want to delete (nodeValue)'''
    # ----- Condition 1: There is not a rootNode to delete ----- #
    if rootNode is None:
        return rootNode
    # ----- Condition 2: Traverse Left Child: The value we want to delete is less than the rootNode's data ----- #
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    # ----- Condition 3: Traverse Right Child: The value we want to delete is less than the rootNode's data ----- #
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    # ----- Condition 4: We find the node we want to delete ----- #
    else:
        # ----- Condition 4-1: The node we want deleted has 0 to 1 children ----- #
        if rootNode.leftChild is None:
            temp = rootNode.rightChild      
            rootNode = None                 # We delete the root node
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild       # We delete the root node
            rootNode = None
            return temp
        # ----- Condition 4-1: The node we want deleted has two childs ----- #
        # The minimum value node in the subtree will replace the node that we want to delete.  And then we delete that minimum value node in the right subtree
        temp = minValueNode(rootNode.rightChild)    # We temporarily store the minimum node in the right subtree into a variable
        rootNode.data = temp.data                   # We set the root node to the minimum node in the right subtree 
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)    # We delete the minimum node in the right subtree
    return rootNode

def deleteBST(rootNode):
    '''Takes a binary search tree (rootNode) and deletes it'''
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BST has been successfully deleted"



newBST = BSTNode(None)
print(insertNode(newBST, 70))
print(insertNode(newBST, 50))
print(insertNode(newBST, 90))
print(insertNode(newBST, 30))
print(insertNode(newBST, 60))
print(insertNode(newBST, 80))
print(insertNode(newBST, 100))
print(insertNode(newBST, 20))
print(insertNode(newBST, 40))

#        70
#      /    \
#     50     90 
#    /  \   /  \
#   30  60 80  100
#  /  \         
# 20  40

print(" ")
preOrderTraversal(newBST)   # Returns 70, 50, 30, 20, 40, 60, 90, 80, 100
print(" ")
inOrderTraversal(newBST)    # Returns 20, 30, 40, 50, 60, 70, 80, 90, 100
print(" ")
postOrderTraversal(newBST)  # Returns 20, 40, 30, 60, 50, 80, 100, 90, 70
print(" ")
levelOrderTraversal(newBST) # Returns 70, 50, 90, 30, 60, 80, 100, 20, 40
print(" ")
print(searchNode(newBST, 110))  # Returns Not Found
print(searchNode(newBST, 60))   # Returns Found
print(" ")
deleteNode(newBST, 50)
#        70
#      /    \
#     50     90 
#    /  \   /  \
#   30  60 80  100
#  /  \         
# 20  40

# Turns into:

#        80
#      /    \
#     50     90 
#    /  \      \
#   30  60      100
#  /  \         
# 20  40

deleteBST(newBST)