class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
        
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):         # This extra method makes printing out our list easier by allowing us to interate through the nodes.
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.head:   # When we circle around back to the head, break the loop
                break

    # Creation of Circular Doubly Linked List
    def createCDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return print("The CDLL has been created")

    # Insertion of Element into Circular Doubly Linked List
    def insertCDLL(self, value, location):
        if self.head is None:
            print("The node can't be inserted")
        else:
            newNode = Node(value)
            if location == 0:               # Option 1 - Insert at beginning
                newNode.next = self.head    
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode        
            elif location == -1:            # Option 2 - Insert at end
                newNode.prev = self.tail
                newNode.next = self.head
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:                           # Option 3 - Insert in middle
                tempNode = self.head            # We start at the head and then traverse to the location we want
                index = 0   
                while index < location - 1:     # We iterate through until we find the location that is before the location that we want.
                    tempNode = tempNode.next    # tempNode = the node before where we want to insert
                    index += 1                  # [tempNode] <---> [newNode] 
                newNode.prev = tempNode         # The newNode's previous reference becomes the tempNode
                newNode.next = tempNode.next    # We save the tempNode's next reference into nextNode's next reference
                newNode.next.prev = newNode     # The node after newNode has it's previous reference set to newNode
                tempNode.next = newNode         # The tempNode's next reference is set to the newNode
            return print("The node has been succesfully inserted")

    # Traverse Circular Doubly Linked List
    def traverseCDLL(self):
        if self.head == None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.head:
                    break

    # Reverse Traversal of Circular Doubly Linked LIst
    def reverseTraverseCDLL(self):
        if self.head == None:
            print("There is not any element for traversal")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
                if tempNode == self.tail:
                    break
    
    # Search for a Node in Circular Doubly Linked List:
    def searchCDLL(self, nodeValue):
        if self.head is None:
            return print("There is not any node in this DLL")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return print("The node exist within the CDLL")
                if tempNode == self.tail:
                    return print("The node does not exist within the CDLL")
                tempNode = tempNode.next

    # Deletion of a node in Circular Doubly Linked List:
    def deleteCDLL(self, location):
        if self.head is None:
            return print("This CDLL is empty.  There is not a node to delete")
        else:
            if location == 0:                # Option 1 - Delete at beginning
                if self.head == self.tail:      # Scenario A - There is only 1 element in our list
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:                           # Scenario B - There are multiple elements in our list
                    self.head = self.head.next 
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:            # Option 2 - Delete at end
                if self.head == self.tail:      # Scenario A - There is only 1 element in our list
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:                           # Scenario B - There are multiple elements in our list
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:                           # Option 3 - Delete at middle
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next          # curNode = the node before the node we want to delete
                    index += 1                      # [curNode] <-> [node we want to delete]
                curNode.next = curNode.next.next    # We set the curNode's next reference to the node after the node we want deleted
                curNode.next.prev = curNode         # The node that comes after curNode will then have it's previous reference set to curNode
            print("The node has successfully been deleted")

    # Delete entire Circular Doubly Linked List
    def deleteEntireCDLL(self):
        if self.head is None:
            print("The CDLL does not exist")
        else:               
            self.tail.next = None                   # We kill the tail's next reference so that we can loop through the CDLL without looping infinitely 
            tempNode = self.head                    # We can't just set the head and tail to Null
            while tempNode:                         # We must delete the middle node's references to unlink everything to make the DLL nodes eligible for garbage collection
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
        print("The CDLL has been succesfully deleted")

circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
print([node.value for node in circularDLL])
# Returns:
# "The CDLL has been created"
# [5]

circularDLL.insertCDLL(0, 0)
circularDLL.insertCDLL(1, 1)
circularDLL.insertCDLL(2, 2)
print([node.value for node in circularDLL])     # Returns: [0, 1, 2, 5]

circularDLL.traverseCDLL()
# Returns
# 0
# 1
# 2
# 5

circularDLL.reverseTraverseCDLL()
# Returns
# 5
# 2
# 1
# 0

circularDLL.searchCDLL(5)   # Returns: "The node exist within the CDLL"
circularDLL.searchCDLL(0)   # Returns: "The node exist within the CDLL"
circularDLL.searchCDLL(11)  # Returns: "The node does not exist within the CDLL"

circularDLL.deleteCDLL(-1)  # Returns: "The node has successfully been deleted"
circularDLL.deleteCDLL(1)   # Returns: "The node has successfully been deleted"
print([node.value for node in circularDLL])     # Returns: [0, 2]

circularDLL.deleteEntireCDLL()  # Returns: "The CDLL has been succesfully deleted"