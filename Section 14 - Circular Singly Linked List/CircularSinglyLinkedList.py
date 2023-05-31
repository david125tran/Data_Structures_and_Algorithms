class Node:                                        
    def __init__(self, value=None):             # Create a node and assign a default value to none
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):                         # When the class is called, we create head & tail.  And initalize it to null
        self.head = None                        # Because there are no nodes in the list
        self.tail = None

    def __iter__(self):                         # This extra method makes printing out our list easier by allowing us to interate through the nodes.
        node = self.head
        while node:
            yield node
            node = node.next
            if node.next ==self.head:
                break
        
    def createCSLL (self, nodeValue):
        '''This function is called to initiate the creation of the CSLL'''
        node = Node(nodeValue)
        node.next = node    # The node's next reference gets set to itself
        self.head = node    # The head gets set to the node
        self.tail = node    # The tail gets set to the node
        return print("The CSLL has been created")
    
    # Insertion of a node in Circular Singly Linked List
    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:                   # Option 1 - Insert at beginning
                newNode.next = self.head            # The newNode's next reference becomes the old head
                self.head = newNode                 # The newNode becomes the new head
                self.tail.next = newNode            # The tail's next reference becomes the newNode
            elif location == -1:                # Option 2 - Insert at end
                newNode.next = self.tail.next       # The newNode's next reference becomes the head
                self.tail.next = newNode            # The old tail's next reference becomes the newNode
                self.tail = newNode                 # The newNode becomes the tail
            else:                               # Option 3 - Insert in middle
                tempNode = self.head                # We start at the head and then traverse to the location we want
                index = 0
                while index < location - 1:         # We iterate through until we find the location that is before the location that we want.  
                    tempNode = tempNode.next
                    index += 1                      # We traverse until we reach the location - 1
                nextNode = tempNode.next            # We save the tempNode's next reference into nextNode variable
                tempNode.next = newNode             # The tempNode's next reference will be our new node
                newNode.next = nextNode             # The newNode's next reference will be the nextNode
            return print("The node has been successfully inserted")

    # Traversal of a node in Circular Singly Linked List
    def traverseCSLL(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.head:
                    break

    # Search Circular Singly Linked List
    def searchCSLL(self, nodeValue):
        if self.head is None:
            return print("There is not any node in this CSLL")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:                             # If we find the value
                    return print(tempNode.value)                            # Return it
                tempNode = tempNode.next
                if tempNode == self.head:                                   # When we reach back to the head, terminate the loop
                    return print("The node does not exist in this CSLL")


    # Deletion of a node in Circular Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            return print("This CSLL is empty.  There is not a node to delete")
        else:
            if location == 0:                # Option 1 - Delete at beginning
                if self.head == self.tail:      # Scenario A - There is only 1 node in the CSLL.  
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:                           # Scenario B - There is more than 1 node in the CSLL
                    self.head = self.head.next          # Set the head's next reference as the head 
                    self.tail.next = self.head          # Set the tail's next reference to the new head
            elif location == -1:            # Option 2 - Delete at end
                if self.head == self.tail:      # Scenario A - There is only 1 node in the CSLL.
                    self.head.next = None               
                    self.head = None
                    self.tail = None
                else:                           # Scenario B - There are multiple nodes in the CSLL.
                    node = self.head                    # We traverse through each node starting at the head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next                # We get the node right before the tail
                    node.next = self.head               # We set the last node's next reference to the head
                    self.tail = node                    # We set the last node as the tail
            else:                           # Option 3 - Delete in the middle
                tempNode = self.head                    # We start at the head and then traverse to the location we want
                index = 0
                while index < location - 1:             # We iterate through until we find the location that is before the location that we want.  
                    tempNode = tempNode.next            # tempNode = the node before the node we want deleted
                    index += 1                          
                nextNode = tempNode.next                # nextNode = the node we want deleted 
                tempNode.next = nextNode.next           # tempNode's next reference = the node after what we want deleted
                                                        # nextNode then becomes unreferenced and eligible for garbage collection and the garbage collector deletes it

    # Delete Entire Circular Singly Linked List
    def deleteEntireCSLL(self):
        if self.head is None:
            print("The circular singly linked list does not exist")
        else:
            self.head = None
            self.tail.next = None 
            self.tail = None
    
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(1)
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(3, 1)
circularSLL.insertCSLL(2, 2)
print([node.value for node in circularSLL]) # Returns [0, 3, 2, 2]

circularSLL.traverseCSLL()

# Returns
# 0
# 3
# 2
# 2
# 1

circularSLL.searchCSLL(4) # Returns "The node does not exist in this CSLL"
circularSLL.searchCSLL(3) # Returns 3

circularSLL.deleteNode(1)
print([node.value for node in circularSLL]) # Returns [0, 2, 2]

circularSLL.deleteEntireCSLL()
print([node.value for node in circularSLL]) # Returns []