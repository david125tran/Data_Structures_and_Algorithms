# A tree is a nonlinear data structure with hierarchial relationships 
# in which data items are connected using references in a hierarchial
# manner

# Starting from the root node, each node contains zero or more nodes 
# connected to it as children.

# Why a Tree?
#     *Quicker an easier access
#     *Store hierarchial data, like folder structure, organization structure, XML/HTML data

# Different Type of trees:
#     *Binary search tree
#     *AVL 
#     *Red black tree
#     *Trie 

# Root node - The top node without a parent
# Edge - A link between a parent & child
# Leaf - A node which does not have children
# Sibling - Children of the same parent 
# Ancestor - Parent, grandparent, great grandparent of a node
# Depth of node - A length of th epath from the root to the node
# Height of node - A length of the path from the node to the deepest node
# Depth of tree - Depth of root node
# Height of tree - Height of root node

class TreeNode:
    def __init__(self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)

print(tree)

# Returns:

# Drinks
#  Cold
#   Cola
#   Fanta
#  Hot
#   Tea
#   Coffee

# Binary tree - Are the data structures in which each node has at 
# most two children, often referred to as the left and right children.

# Binary trees can be created with: (1) Linked Lists and (2) Arrays

# Binary Tree Representation
#     *Left child = cell[2x]
#     *Right child = cell[2x + 1]
# Where "x" is the parent's cell location
# The cells start at index 1 or N1 (not 0 or N0) for ease of calculation

# Traversal Types:
#     *PreOrder:      Root -> Left subtree -> Right subtree
#     *InOrder:       Left subtree -> Root -> Right subtree
#     *PostOrder:     Left subtree -> Right subtree -> Root
#     *LevelOrder:    Level by Level followed by Left to Right

# --------------------------- Creating a Binary Tree ---------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

newBinaryTree = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBinaryTree.leftChild = leftChild
newBinaryTree.rightChild = rightChild

tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
leftChild.leftChild = tea
leftChild.rightChild = coffee

# --------------------------- Binary Trees Traversal with Stacks ---------------------------

def preOrderTraversal(rootNode):
    '''
    Traverses a binary tree from:
    Root -> Left subtree -> Right subtree
    '''
    if not rootNode:    # Creates an exit for the recursion
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBinaryTree)        # Drinks -> Hot -> Tea -> Coffee -> Cold

#           Drinks
#         /       \
#       Hot       Cold
#      /  \       
#    Tea Coffee 

def inOrderTraversal(rootNode):
    '''
    Traverses a binary tree from:
    Left subtree -> Root -> Right subtree
    '''
    if not rootNode:    # Creates an exit for the recursion
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(newBinaryTree)         # Tea -> Hot -> Coffee -> Drinks -> Cold

#           Drinks
#         /       \
#       Hot       Cold
#      /  \       
#    Tea Coffee 

def postOrderTraversal(rootNode):
    '''
    Traverses a binary tree from:
    Left subtree -> Right subtree -> Root
    '''
    if not rootNode:    # Creates an exit for the recursion 
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(newBinaryTree)   # Tea -> Coffee -> Hot -> Cold -> Drinks

#           Drinks
#         /       \
#       Hot       Cold
#      /  \       
#    Tea Coffee 

# --------------------------- Binary Trees Traversal with Linked Lists ---------------------------

# Level Order Traversal uses a queue to traverse whereas all other traversals use a stack.  
# Because of this, the Level Order Traversal has higher performance.  
import LinkedListQueue as queue

def levelOrderTraversal(rootNode):
    '''
    Traverses a binary tree from:
    Top to Bottom from Left to Right
    using a Linked List
    '''
    if not rootNode:    # Creates an exit for the recursion 
        return
    else:
        customQueue = queue.LinkedListQueue()     # Uses our LinkedListQueue
        customQueue.enqueue(rootNode)                           # Adds the root to the LLQ
        while not(customQueue.isEmpty()):                       # Keep looping while there are nodes
            root = customQueue.dequeue()                            # Removes the root from the LLQ
            print(root.value.data)                                  # Print that root's data 
            # Check for a left child
            if (root.value.leftChild is not None):                  # If there is a left child:
                customQueue.enqueue(root.value.leftChild)               # Adds the child to the LLQ as the new root
            # Check for a right child                               
            if (root.value.rightChild is not None):                 # If there is a right child:
                customQueue.enqueue(root.value.rightChild)              # Adds the child to the LLQ as the new root

levelOrderTraversal(newBinaryTree)      # Drinks -> Hot -> Cold -> Tea -> Coffee

#           Drinks
#         /       \
#       Hot       Cold
#      /  \       
#    Tea Coffee 

# --------------------------- Search Binary Tree (with Traversal with Linked Lists) ---------------------------

def searchBinaryTree(rootNode, nodeValue):
    '''Searches a binary tree, rootNode for a value, nodeValue'''
    if not rootNode:
        return "The binary tree does not exist"
    else:
        customQueue = queue.LinkedListQueue()
        customQueue.enqueue(rootNode)                   # Adds the root to the LLQ
        while not (customQueue.isEmpty()):              # Keep looping while there are nodes
            root = customQueue.dequeue()                            # Removes the root from the LLQ
            if root.value.data == nodeValue:                        # Checks for a match
                return "Success, the nodeValue exists within the Binary Tree"
            # Check for a left child
            if (root.value.leftChild is not None):                  # If there is a left child:
                customQueue.enqueue(root.value.leftChild)               # Adds the child to the LLQ as the new root
            # Check for a right child                               
            if (root.value.rightChild is not None):                 # If there is a right child:
                customQueue.enqueue(root.value.rightChild)              # Adds the child to the LLQ as the new root
        return "Not Found!"

print(searchBinaryTree(newBinaryTree, "Tea"))   # Returns: Success, the nodeValue exists within the Binary Tree
print(searchBinaryTree(newBinaryTree, "Milk"))  # Returns: Not Found!

# --------------------------- Insert Node into Binary Tree (with Traversal with Linked Lists) ---------------------------

def insertNodeBinaryTree(rootNode, newNode):
    '''Inserts a new node (newNode) into a binary tree (rootNode)'''
    if not rootNode:                # If there is not a root node
        rootNode = newNode              # The new node becomes the root node
    else:
        customQueue = queue.LinkedListQueue()               
        customQueue.enqueue(rootNode)                   # Adds the root to the LLQ
        while not(customQueue.isEmpty()):                           # Keep looping while there are nodes
            root = customQueue.dequeue()                            # Removes the root from the LLQ
            # Check for a left child
            if (root.value.leftChild is not None):                  # If there is a left child:
                customQueue.enqueue(root.value.leftChild)               # Adds the child to the LLQ as the new root
            else:                                                   # Else
                root.value.leftChild = newNode                          # Adds the new node
                return "Succesfully inserted"
            # Check for a right child                               
            if (root.value.rightChild is not None):                 # If there is a right child:
                customQueue.enqueue(root.value.rightChild)              # Adds the child to the LLQ as the new root
            else:                                                   # Else
                root.value.rightChild = newNode                         # Adds the new node
                return "Succesfully inserted"

newNode = TreeNode("Cola")
print(insertNodeBinaryTree(newBinaryTree, newNode))     # Returns: "Succesfully inserted"
#           Drinks
#         /       \
#       Hot       Cold
#      /  \       /
#    Tea Coffee Cola

# --------------------------- Get The Deepest Node From Binary Tree (with Traversal with Linked Lists) ---------------------------

def getDeepestNode(rootNode):
    '''Returns the deepest level node from a binary tree (rootNode)'''
    if not rootNode:
        return
    else:
        customQueue = queue.LinkedListQueue()
        customQueue.enqueue(rootNode)                   # Adds the root to the LLQ
        while not(customQueue.isEmpty()):                           # Keep looping while there are nodes
            root = customQueue.dequeue()                            # Removes the root from the LLQ
            # Check for a left child
            if (root.value.leftChild is not None):                  # If there is a left child:
                customQueue.enqueue(root.value.leftChild)               # Adds the child to the LLQ as the new root
            # Check for a right child                               
            if (root.value.rightChild is not None):                 # If there is a right child:
                customQueue.enqueue(root.value.rightChild)              # Adds the child to the LLQ as the new root
        deepestNode = root.value                               # The last node remaining is the deepest our tree goes
        return deepestNode

deepestNode = getDeepestNode(newBinaryTree)
print(deepestNode.data)     # Returns: Cola

# --------------------------- Delete The Deepest Node From Binary Tree (with Traversal with Linked Lists) ---------------------------

def deleteDeepestNode(rootNode, dNode):
    '''Deletes the deepest node (dNode) from a binary tree (rootNode)'''
    if not rootNode:
        return
    else:
        customQueue = queue.LinkedListQueue()
        customQueue.enqueue(rootNode)                   # Adds the root to the LLQ
        while not(customQueue.isEmpty()):               # Keep looping while there are nodes
            root = customQueue.dequeue()                    # Removes the root from the LLQ
            if root.value is dNode:                             # If the deepest node is the root
                root.value = None                                   # Set the root value to none
                return
            # Check for a right child                               
            if root.value.rightChild:                           # If there is a right child
                if root.value.rightChild is dNode:                  # If the rigth child is the deepest node
                    root.value.rightChild = None                    # Set the right child's value to none
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)      # Adds the child to the LLQ as the new root
            # Check for a left child                               
            if root.value.leftChild:                            # If there is a left child
                if root.value.leftChild is dNode:                   # If the left child is the deepest node
                    root.value.leftChild = None                     # Set the left child's value to none
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)       # Adds the child to the LLQ as the new root

deleteDeepestNode(newBinaryTree, deepestNode)
levelOrderTraversal(newBinaryTree)

#           Drinks
#         /       \
#       Hot       Cold
#      /  \       
#    Tea Coffee 

# --------------------------- Delete a Node From Binary Tree (with Traversal with Linked Lists) ---------------------------

def deleteNodeBinaryTree(rootNode, node):
    '''
    Deletes a node that you want to delete from a binary tree (rootNode). 
    And replaces that node with the deepest node in the tree while also 
    deleting that deepest node.
    '''
    if not rootNode:
        return
    else:
        customQueue = queue.LinkedListQueue()
        customQueue.enqueue(rootNode)                   # Adds the root to the LLQ
        while not(customQueue.isEmpty()):               # Keep looping while there are nodes
            root = customQueue.dequeue()                    # Removes the root from the LLQ
            if root.value.data == node:                     # If the root matches the node
                dNode = getDeepestNode(rootNode)                # Get the deepest node of that branch
                root.value.data = dNode.data                    # Sets the node to the deepest node
                deleteDeepestNode(rootNode, dNode)              # Deletes the deepest node
                return "The node has been succesfully deleted"
            # Check for a left child
            if (root.value.leftChild is not None):                  # If there is a left child:
                customQueue.enqueue(root.value.leftChild)               # Adds the child to the LLQ as the new root
            # Check for a right child                               
            if (root.value.rightChild is not None):                 # If there is a right child:
                customQueue.enqueue(root.value.rightChild)              # Adds the child to the LLQ as the new root
        return "Failed to delete"
    
print(" ")
deleteNodeBinaryTree(newBinaryTree, 'Hot')
levelOrderTraversal(newBinaryTree)

#           Drinks
#         /       \
#       Coffee      Cold
#      /         
#    Tea  

def deleteEntireBinaryTree(rootNode):
    '''
    Deletes an entire binary tree (rootNode)
    '''
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary tree has been successfully deleted"

deleteEntireBinaryTree(newBinaryTree)

# --------------------------- Create Binary Trees with List ---------------------------
class ListBinaryTree:
    def __init__(self, size):
        '''Creates a binary tree using Python list with a maximum size (size).'''
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        '''
        Inserts a node with value into the ListBinaryTree. Insertion follows the pattern: 
        Left child = cell[2x], Right child = cell[2x + 1], Where "x" is the parent's cell location.
        The cells start at index 1 or N1 (not 0 or N0) for ease of calculation
        '''
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The binary tree is full"
        self.customList[self.lastUsedIndex + 1] = value     # Add the value 
        self.lastUsedIndex +=1                              # Increase the index
        return "The value has been successfully inserted"

    def searchNode(self, nodeValue):
        '''Searches for a node value (nodeValue) within the ListBinaryTree'''
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success"
        return "Not Found!"
    
    def preOrderTraversal(self, index):
        '''
        Traverses a list binary tree from:
        Root -> Left subtree -> Right subtree
        '''
        if index > self.lastUsedIndex:      # Exit for recursion
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2)         # Recursion into the left child
        self.preOrderTraversal(index*2 + 1)     # Recursion into the right child 

    def inOrderTraversal(self, index):
        '''
        Traverses a list binary tree from:
        Left subtree -> Root -> Right subtree
        '''
        if index > self.lastUsedIndex:      # Exit for recursion
            return
        self.inOrderTraversal(index*2)         # Recursion into the left child
        print(self.customList[index])
        self.inOrderTraversal(index*2 + 1)     # Recursion into the right child 

    def postOrderTraversal(self, index):
        '''
        Traverses a list binary tree from:
        Left subtree -> Right subtree -> Root
        ''' 
        if index > self.lastUsedIndex:      # Exit for recursion
            return
        self.postOrderTraversal(index*2)         # Recursion into the left child
        self.postOrderTraversal(index*2 + 1)     # Recursion into the right child 
        print(self.customList[index])

    def levelOrderTraversal(self, index):
        '''
        Traverses a list binary tree from:
        Top to Bottom from Left to Right
        '''
        for i in range(index, self.lastUsedIndex + 1):   # Add 1 because we start our index at 1
            print(self.customList[i])
        
    def deleteNode(self, value):
        '''
        Deletes a node at index and replaces it with the deepest level node. 
        And then the deepest level node is deleted.
        '''
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]    # Replace the node with the deepest node
                self.customList[self.lastUsedIndex] = None                  # Replace the deepest node with null
                self.lastUsedIndex -= 1                                     # Lower the index, -1
                return "The node has been successfully deleted"

    def deleteEntireListBinaryTree(self):
        '''Deletes the entire list binary tree'''
        self.customList = None                                              # There is no need to reset lastUsedIndex to 0 because you can't
        return "The List Binary Tree has been deleted"                      # perform any operations on the tree until you initialize a new one

newBinaryTree = ListBinaryTree(8)
print(newBinaryTree.insertNode("Drinks"))
print(newBinaryTree.insertNode("Hot"))
print(newBinaryTree.insertNode("Cold"))
print(newBinaryTree.searchNode("Hot"))      # Returns: Success
print(newBinaryTree.searchNode("Milk"))     # Returns: Not Found!
#     Drinks
#     /    \
#   Hot    Cold
newBinaryTree.preOrderTraversal(1)          # Drinks -> Hot -> Cold 
newBinaryTree.inOrderTraversal(1)           # Hot -> Drinks -> Cold
newBinaryTree.postOrderTraversal(1)         # Hot -> Cold -> Drinks
newBinaryTree.levelOrderTraversal(1)        # Drinks -> Hot -> Cold
newBinaryTree.deleteNode("Hot")
#     Drinks
#     /    
#   Cold    
print(newBinaryTree.deleteEntireListBinaryTree())
