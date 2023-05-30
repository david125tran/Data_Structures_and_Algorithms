# Linked list is a form of a sequential collection and it does not have to be in order.
# A linked list is made up of independent nodes that may contain any type of data and
# each node has a reference to the next node in the link. 

# ------------------------ Types of Linked Lists ------------------------
# Singly linked list
# Circular singly linked list
# Doubly linked list
# Circular doubly linked list

# ------------------------ Creation of Linked Lists ------------------------
# Create head and tail, initalize with null
# Create a blank node and assign a value to it and reference to null
# Link head and tail with the node

class Node:                                        
    def __init__(self, value=None):             # Create a node and assign a value 
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):                         # When the class is called, we create head & tail.  And initalize it to null
        self.head = None                        # Because there are no nodes in the list
        self.tail = None

    def __iter__(self):                         # This extra method makes printing out our list easier by allowing us to interate through the nodes.
        node = self.head
        while node:
            yield node
            node = node.next 
    
    # Insert into Singly Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)                   # Initialize a new node and assign a value to it
        if self.head is None:                   # If there is not a node, we make a head node that is also the tail
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:                   # Option 1 - Insert at beginning of linked list
                newNode.next = self.head                # We create a new node that has no next reference.  The next reference gets set to the current head.
                self.head = newNode                     # The new node then becomes the new head.  
            elif location == -1:                 # Option 2 - Insert at end of linked list
                newNode.next = None                     # We create a new node with no next reference (because it will be the tail)
                self.tail.next = newNode                # The current tail's next reference be comes our new node
                self.tail = newNode                     # The tail becomes the new node
            else:                               # Option 3 - Insert at middle of linked list
                tempNode = self.head                    # We start at the head and then traverse to the location we want
                index = 0
                while index < location - 1:             # We iterate through until we find the location that is before the location that we want.  
                    tempNode = tempNode.next
                    index += 1                          # We traverse until we reach the location - 1
                nextNode = tempNode.next                # We save the tempNode's next reference into nextNode variable
                tempNode.next = newNode                 # The tempNode's next reference will be our new node
                newNode.next = nextNode                 # The newNode's next reference will be the nextNode
                if tempNode == self.tail:               # If we insert between the 2nd to last node and the tail, we must update the tail
                    self.tail = newNode                 # The new node now becomes to tail

    # Traverse Singly Linked List
    def traverseSLL(self):
        if self.head is None:                                   # If there is no head, there is no singly linked list
            print("The singly linked list does not exist")
        else:                                                   # If there is a head, we traverse through the list starting at the head
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    # Search Singly Linked List
    def searchSLL(self, nodeValue):
        if self.head is None:                                   # If there is no head, there is no singly linked list
            print("The singly linked list does not exist")                      
        else:                                                   # If there is a head, we traverse through the list starting at the head
            node = self.head
            while node is not None:
                if node.value == nodeValue:                     # If the value exists, return it
                    print(node.value)
                node = node.next
            return "The value does not exist in this list"      # If the value is not found, the value does not existin the SLL

    # Delete a node in Singly Linked List
    def deleteNode(self, location):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            if location == 0:                           # Option 1 - Deletion of the head
                if self.head == self.tail:                      # If the SLL is one node long, the SLL is deleted
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next                  # The head's next reference becomes the new head
            elif location == -1:                         # Option 2 - Deletion of the tail
                if self.head == self.tail:                      # If the SLL is one node long, the SLL is deleted
                    self.head = None
                    self.tail = None
                else:
                    node = self.head                            # If the SLL is not one node long, we start at the head
                    while node is not None:                     # and traverse through each node 
                        if node.next == self.tail:              # If we get to the tail, we break because the tail does not have a next reference
                            break
                        node = node.next                        # We iterate through until we obtain the node before the tail (2nd to last node)
                    node.next = None                            # The last node's next reference is set to null
                    self.tail = node                            # And the last node becomes the tail
            else:                                       # Option 3 - Deletion in the middle
                previousNode = self.head
                index = 0
                while index < location - 1:                     # We iterate through until we find the location that is before the location that we want. 
                    previousNode  = previousNode.next
                    index += 1                                  # We traverse until we reach the location - 1
                toBeDeletedNode = previousNode.next                        
                previousNode.next = toBeDeletedNode.next        # We make the previousNode's next reference to be the deleted node's next reference.   
                                                                # The deleted node is no longer referenced         

    # Delete entire Singly Linked List
    def deleteEntireSLL(self):
        if self.head is None:
            print("The singly linked list does not exist")
        else:
            self.head = None
            self.tail = None


            

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, -1) # Adds to end of list
singlyLinkedList.insertSLL(4, -1) # Adds to end of list
singlyLinkedList.insertSLL(0, 0) # Adds to beginning of list
print([node.value for node in singlyLinkedList]) # Returns [0, 1, 2, 3, 4]

singlyLinkedList.traverseSLL()
# Returns
# 0
# 1
# 2 
# 3
# 4

singlyLinkedList.searchSLL(3) # Returns 3

singlyLinkedList.deleteNode(2)
print([node.value for node in singlyLinkedList]) # Returns [0, 1, 3, 4]

singlyLinkedList.deleteEntireSLL()
print([node.value for node in singlyLinkedList]) # Returns []