'''
Binary Heap:
    *A binary tree with additional properties.  
    *It is a complete binary tree.  All levels are full, except possibly the last one
    *The key stored in each node is either:
        a) Max Heap: Greater than or equal to the keys in the node's children
        b) Min Heap: Less than or equal to the keys in the node's children


Example of complete binary max heap:
         100                     
        /   \                
       19    36         
      / \   / \              
    17  3  25  1          
    / \                         
   2   7                        

Example of complete binary min heap:
          5                     
        /   \                
       10   20         
      / \   / \              
    30  40 50  60        
    / \                         
   70 80   

Binary heaps can be implemented through arrays and lists.  But arrays implement them best.

Binary Heap (From Array):
    *Left child = cell[2x]
    *Right child = cell[2x + 1]
We start at index x = 1 instead of index x = 0 for easier calculations on the array. Where
index of 1 will return the root.  

The only element you can ever extract from a heap is the root.
'''

class Heap:
    def __init__(self, size):
        self.customList = (size + 1) * [None]           
        self.heapSize = 0
        self.maxSize = size + 1                         # The size is 'size + 1' because we start at index 1 instead of 0 for easier calculations

def peakOfHeap(rootNode):
    '''Returns the root of a binary heap tree (rootNode)'''
    if not rootNode:
        return
    else:
        return rootNode.customList[1]

def sizeOfHeap(rootNode):
    '''Returns the size of a binary heap tree (rootNode)'''
    if not rootNode:
        return
    else:
        return rootNode.heapSize
    
def levelOrderTraversal(rootNode):
    '''
    Traverses a binary heap from:
    Top to Bottom from Left to Right
    '''
    if not rootNode:
        return      
    else:
        for i in range(1, rootNode.heapSize + 1):       # We traverse starting at index = 1 because we avoided using index = 0, for easier calculations
            print(rootNode.customList[i])

def heapifyTreeInsert(rootNode, index, heapType):
    '''A helper function for insertNode().  Sorts a heap tree (rootNode) at given index and heapType ('Min' or 'Max') after a node has been inserted.'''
    parentIndex = int(index/2)
    if index <= 1:                                                              # If the index <= 1, that means we don't have a rootNode yet
        return                                                                      
    if heapType == "Min":                                                       # Minimum Heap 
        if rootNode.customList[index] < rootNode.customList[parentIndex]:           # If the root key we are inserting is less than it's parent
            temp = rootNode.customList[index]                                       # We swap the root node and root node's parent's places
            rootNode.customList[index] = rootNode.customList[parentIndex]           # And update the indices
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)                          # We call the method recursively until the rootNode is in the correct spot
    elif heapType == "Max":                                                     # Maximum Heap
        if rootNode.customList[index] > rootNode.customList[parentIndex]:           # If the root key we are inserting is greater than it's parent
            temp = rootNode.customList[index]                                       # We swap the root node and root node's parent's places
            rootNode.customList[index] = rootNode.customList[parentIndex]           # And update the indices
            rootNode.customList[parentIndex] = temp
        heapifyTreeInsert(rootNode, parentIndex, heapType)                          # We call the method recursively until the rootNode is in the correct spot

def insertNode(rootNode, nodeValue, heapType):
    '''Inserts a node (rootNode) with a value (nodeValue) into a heap tree with a heapType of 'Min' or 'Max'.'''
    if rootNode.heapSize +1 == rootNode.maxSize:
        return "The Binary Heap is Full"
    rootNode.customList[rootNode.heapSize +1] = nodeValue
    rootNode.heapSize +=1                                                           # Update the self.heapSize
    heapifyTreeInsert(rootNode, index=rootNode.heapSize, heapType=heapType)
    return "The value has been successfulyl inserted"

def heapifyTreeExtract(rootNode, index, heapType):
    '''
    A helper function for extractNode().  
    Sorts a heap tree (rootNode) at given index and heapType ('Min' or 'Max') after a node has been deleted.
    '''

    leftIndex = index * 2                                                       # leftIndex = index of left child of to be deleted node (rootNode)
    rightIndex = (index * 2) + 1                                                # rightIndex = index of right child of to be deleted node (rootNode)
    swapChild = 0

    if rootNode.heapSize < leftIndex:                                           # Case 1 - The to be deleted node has no child
        return                      
    elif rootNode.heapSize == leftIndex:                                        # Case 2 - The to be deleted node has one child        
        if heapType == "Min":                                                       # Case 2A - Minimum Heap:
            if rootNode.customList[index] > rootNode.customList[leftIndex]:             # If the to be deleted node (rootNode) is greater than it's child:
                temp = rootNode.customList[index]                                           # We swap the to be deleted node (rootNode) with it's child
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return
        else:                                                                       # Case 2B - Maximum Heap:
            if rootNode.customList[index] < rootNode.customList[leftIndex]:             # If the to be deleted node (rootNode) is less than it's child:
                temp = rootNode.customList[index]                                           # We swap the to be deleted node (rootNode) with it's child
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
            return    
    else:                                                                       # Case 3 - The to be deleted node has two children
        if heapType == "Min":                                                       # Case 3A - Minimum Heap:
            if rootNode.customList[leftIndex] < rootNode.customList[rightIndex]:        # If the left child is less than the right child:
                swapChild = leftIndex                                                       # The left child's index is temporarily stored because we will soon swap the child & rootNode
            else:                                                                       # The right child is less than the left child:
                swapChild = rightIndex                                                      # The right child's index is temporarily stored because we will soon swap the child & rootNode
            if rootNode.customList[index] > rootNode.customList[swapChild]:             # If the to be deleted node (rootNode) is greater than the swapChild, we must swap their places
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
        else:                                                                       # Case 3B - Maximum Heap:
            if rootNode.customList[leftIndex] > rootNode.customList[rightIndex]:        # If the left child is more than the right child:
                swapChild = leftIndex                                                       # The left child's index is temporarily stored because we will soon swap the child & rootNode
            else:                                                                       # The right child is more than the left child:
                swapChild = rightIndex                                                      # The right child's index is temporarily stored because we will soon swap the child & rootNode
            if rootNode.customList[index] < rootNode.customList[swapChild]:             # If the to be deleted node (rootNode) is less than the swapChild, we must swap their places
                temp = rootNode.customList[index]
                rootNode.customList[index] = rootNode.customList[leftIndex]
                rootNode.customList[leftIndex] = temp
        heapifyTreeExtract(rootNode, swapChild, heapType)                           # Recursion to parse through the Binary Heap Tree all thew way up to the root

def extractNode(rootNode, heapType):
    '''
    Extracts the root of a Binary Heap Tree (rootNode) and then sorts itself out.
    This function can extract only the root.
    '''

    if rootNode.heapSize == 0:
        return 
    else:
        extractNode = rootNode.customList[1]                                        # The extractNode is our root
        rootNode.customList[1] = rootNode.customList[rootNode.heapSize]             # Our very last element from our array will temporarily become the new root
        rootNode.customList[rootNode.heapSize] = None                               # We set our very last element to Null  
        rootNode.heapSize -= 1                                                      # We update the heapSize
        heapifyTreeExtract(rootNode, 1, heapType)                                   # We call our helper function too sort the Binary Heap Tree.  The new root moves downward while swapping places and the tree organizes.
        return extractNode                                                          # We return the binary heap tree
    
def deleteEntireBHT(rootNode):
    '''Deletes an entire Binary Heap Tree'''
    rootNode.customList = None                   # The entire tree then becomes eligible for garbage collection
    return "The Binary Heap Tree has been successfully been deleted"

newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))    # Returns 0 because we have only so far initialized the heap.  
insertNode(newBinaryHeap, 4, "Max")
insertNode(newBinaryHeap, 5, "Max")
insertNode(newBinaryHeap, 2, "Max")
insertNode(newBinaryHeap, 1, "Max")
print("")
levelOrderTraversal(newBinaryHeap)   # Returns: 5 4 2 1 

#       5              
#     /   \            
#    4     2         
#   /             
#  1  

print("")
extractNode(newBinaryHeap, "Max")
levelOrderTraversal(newBinaryHeap) # Returns: 4 1 2     (5 gets removed and then the tree organizes)

#       4              
#     /   \            
#    1     2         
 
deleteEntireBHT(newBinaryHeap)
