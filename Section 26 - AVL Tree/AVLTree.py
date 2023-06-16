'''
An AVL tree is a self-balancing Binary Search Tree (BST) where the difference between
heights of left and right subtrees cannot be more than one for all nodes.  If at any 
time heights of left and right subtrees differ by 2 or more, then rebalancing is done
to restore AVL property, this process is called rotation.

AVL trees have better performance & are faster due to less time complexity than binary
search tree.

Inserting a Node Into AVL Tree:
    *Case 1: Rotation is not required
    *Case 2: Rotation is required

To figure out which node is disbalanced, see if a node has heights differing 
by 2 or more.  If you find a disbalanced node, rotation is required.

Rotation Conditions:
    *Left Left:     Right rotation
    *Left Right:    Left rotation (on disbalancedNode.leftChild) followed by Right rotation (on disbalancedNode)
    *Right Right:   Left rotation
    *Right Left:    Right rotation (on disbalancedNode.rightChild) followed by Left rotation (on disbalancedNode)

Deleting a Node Into AVL Tree:
    *Case 1: Rotation is not required
        * The node to be deleted has 1 child
        * The node to be deleted has 2 children
    *Case 2: Rotation is required    

Rotation conditions caused from deleting a node follow the same conditions as inserting a node.  
'''

import LinkedListQueue as queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrderTraversal(rootNode):
    '''
    Traverses a binary search tree from:
    Root -> Left subtree -> Right subtree
    '''
    if not rootNode:                            # If you get null, you are at the bottom of the tree
        return                                  # Creates an exit for the recursion
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    '''
    Traverses a binary search tree from:
    Left subtree -> Root -> Right subtree
    '''
    if not rootNode:                            # If you get null, you are at the bottom of the tree
        return                                  # Creates an exit for the recursion
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    '''
    Traverses a binary search tree from:
    Left subtree -> Right subtree -> Root
    '''
    if not rootNode:                            # If you get null, you are at the bottom of the tree
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
    if not rootNode:                            # If you get null, you are at the bottom of the tree
        return                                  # Creates an exit for the recursion
    else:
        customQueue = queue.LinkedListQueue()       # Uses our LinkedListQueue
        customQueue.enqueue(rootNode)                   # Adds the root to the LLQ
        while not(customQueue.isEmpty()):                   # Keep looping while there are nodes
            root = customQueue.dequeue()                        # Removes the root from the LLQ
            print(root.value.data)                              # Print that root's data 
            if root.value.leftChild is not None:            # If there is a left child:
                customQueue.enqueue(root.value.leftChild)         # Recursion into the left child's data
            if root.value.rightChild is not None:           # if there is a right child:
                customQueue.enqueue(root.value.rightChild)        # Recursion into that right child's data

def searchNode(rootNode, nodeValue):
    '''Searches a binary search tree (rootNode) for a value (nodeValue)'''
    if rootNode == None:                                        # If the BST is empty
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
                return searchNode(rootNode.leftChild, nodeValue)            # Recursion: Enter into the left child subtree 
        else:                                                       # If the nodeValue is mpre than the current node's data, check the right child
            if not rootNode.rightChild:                                     # If there is not a right child, the value can't exist
                return "Not Found"                                          # Exit
            elif rootNode.rightChild.data == nodeValue:                 # Elif the value is found in the left node's data
                return "Found"                                              # Look no further, exit
            else:                                                       # Else
                return searchNode(rootNode.rightChild, nodeValue)           # Recursion: Enter into the right child subtree

def getHeight(rootNode):
    '''Returns the height of a given node (rootNode)'''
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalancedNode):
    '''Rotates a node (disbalancedNode) right.'''

    #          A                      A
    #        /   \                  /   \
    #       B     C         -->    B     C
    #      / \   / \              / \   / \
    #     D   E F   G            H   E F   G
    #    /                      / \   
    #   H                      I   D      
    #  /
    # I

    newRoot = disbalancedNode.leftChild                                                                                 # The disbalanced node's (old root's) left child becomes the new root
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild                                                    # The right child of the left child of the disbalanced node (old root) becomes the new left child of the new root
    newRoot.rightChild = disbalancedNode                                                                                # The new root's right child becomes the disbalanced child (old root)
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))       # Update the height.  We add 1 because we are obtaining the children's height when we are really looking for the parent's height
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))                               # Update the height.  We add 1 because we are obtaining the children's height when we are really looking for the parent's height
    return newRoot                                                                                                      # Return the updated AVL tree

def leftRotate(disbalancedNode):
    '''Rotates a node (disbalancedNode) left.'''

    #          A                      A
    #        /   \                  /   \
    #       B     C         -->    B     C
    #      / \   / \              / \   / \
    #     D   E F   G            D   E F   G
    #    /                      /    
    #   H                      I         
    #    \                    /
    #     I                  H
    
    newRoot = disbalancedNode.rightChild                                                                                # The disbalanced node's (old root's) right child becomes the new root
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild                                                   # The left child of the right child of the disbalanced node (old root) becomes the new right child of the new root
    newRoot.leftChild = disbalancedNode                                                                                 # The new root's left child becomes the disbalanced child (old root)
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))       # Update the height.  We add 1 because we are obtaining the children's height when we are really looking for the parent's height
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))                               # Update the height.  We add 1 because we are obtaining the children's height when we are really looking for the parent's height
    return newRoot                                                                                                      # Return the updated AVL tree

def getBalance(rootNode):
    '''Gets the balance of an AVL tree'''
    if not rootNode:                                                            
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    '''
    Inserts a node with a node value (nodeValue) into an AVL tree with a root node (rootNode).  
    Also rotates if rotation is required after insertion.
    '''
    
    # ---------------- Part 1: Node Insertion ---------------- #
    if not rootNode:                                                                            # Create an exit for the recursion 
        return AVLNode(nodeValue)                                                                   # If, null is received, we return the nodeValue to create a child.
    elif nodeValue < rootNode.data:                                                             # Elif, the new node's value is less than the root node
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)                              # We call the method recursively (to get to the bottom of the tree) pushing the node left and eventually the node is added
    else:                                                                                       # Else, the new node must be a more than the root node
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)                            # We call the method recursively (to get to the bottom of the tree) pushing the node right and eventually the node is added

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))    # Update the height.  We add 1 because we are obtaining the children's height when we are really looking for the parent's (rootNode's) height

    # ---------------- Part 2: Tree Rotation (If Required) ---------------- #
    balance = getBalance(rootNode)         
    # Check to see if we have a disbalanced node (balance > 1 or balance < -1)
    # If we do have a disbalanced node, we must rotate
    if balance > 1 and nodeValue < rootNode.leftChild.data:         # Left Left Condition
        return rightRotate(rootNode)                                    # Right rotation (on disbalancedNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:         # Left Right Condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)             # Left rotation (on disbalancedNode.leftChild)
        return rightRotate(rootNode)                                    # followed by Right rotation (on disbalancedNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:       # Right Left Condition
        return leftRotate(rootNode)                                     # Left rotation (on disbalancedNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:       # Right Right Condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)          # Right rotation (on disbalancedNode.rightChild)
        leftRotate(rootNode)                                            # followed by Left rotation (on disbalancedNode)
    return rootNode                                                 # Returns the updated AVL tree

def getMinValueNode(rootNode):
    '''Returns the minimum value node of a AVL tree'''
    if rootNode is None or rootNode.leftChild is None:              # Creates an exit for the recursion
        return rootNode
    return getMinValueNode(rootNode.leftChild)                      # Call the function recursively to get the minimum value of the AVL tree

def deleteNode(rootNode, nodeValue):        
    '''
    Deletes a node with a node value (nodeValue) from an AVL tree with a root node (rootNode).  
    Also rotates if rotation is required after deletion.
    '''

    # ---------------- Part 1: Node Deletion ---------------- #
    if not rootNode:                                                        # Create an exit for the recursion 
        return rootNode
    elif nodeValue < rootNode.data:                                         # If the nodeValue is less than the parent's data, go left
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)          # We call the function recursively on the left side
    elif nodeValue > rootNode.data:                                         # If the nodeValue is more than the parent's data, go right
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)        # We call the function recursively on the right side
    else:                                                                   # Else, we find the node of interest
        if rootNode.leftChild is None:                                          # If the node we want to delete has no left child
            temp = rootNode.rightChild                                              # We temporarily store right child data into temp
            rootNode = None                                                         # We delete the rootNode
            return temp                                                             # We return the right child's data to replace the rootNode
        elif rootNode.rightChild is None:                                       # If the node we want to delete has a left child but no right child:
            temp = rootNode.leftChild                                               # We temporarily store left child data into temp
            rootNode = None                                                         # We delete the rootNode
            return temp                                                             # We return the left child's data to replace the rootNode
        else:                                                                   # In case we have two children:
            temp = getMinValueNode(rootNode.rightChild)                             # We temporarily store the root node's right child's minimum value node into temp
            rootNode.data = temp.data                                               # We replace root node with that minimum value
            rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)        # We delete that minium value node from the bottom of the tree

    # ---------------- Part 2: Tree Rotation (If Required) ---------------- #
    balance = getBalance(rootNode)         
    # Check to see if we have a disbalanced node (balance > 1 or balance < -1)
    # If we do have a disbalanced node, we must rotate
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:                     # Left Left Condition
        return rightRotate(rootNode)                                                # Right rotation (on disbalancedNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:                   # Right Left Condition
        return leftRotate(rootNode)                                                 # Left rotation (on disbalancedNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:                      # Left Right Condition
        rootNode.leftChild = leftRotate(rootNode.leftChild)                         # Left rotation (on disbalancedNode.leftChild)
        return rightRotate(rootNode)                                                # followed by Right rotation (on disbalancedNode)
    if balance < -1 and getBalance(rootNode.rightChild) < 0:                    # Right Right Condition
        rootNode.rightChild = rightRotate(rootNode.rightChild)                      # Right rotation (on disbalancedNode.rightChild)
        leftRotate(rootNode)                                                        # followed by Left rotation (on disbalancedNode)
    return rootNode                                                             # Returns the updated AVL tree

def deleteAVL(rootNode):
    '''Deletes an entire AVL tree'''
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None                              # The entire AVL tree then becomes eligible for garbage collection
    return "The AVL has been successfully been deleted"

newAVL = AVLNode(5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 15)     # Our node gets added and we have a right right condition disbalance.  Our tree then gets roatated to balance.
newAVL = insertNode(newAVL, 20)
levelOrderTraversal(newAVL)

#        10
#       / \
#      5   15
#            \
#             20

print("")
newAVL = deleteNode(newAVL, 15)
levelOrderTraversal(newAVL)
deleteAVL(newAVL)
levelOrderTraversal(newAVL) # Returns None
