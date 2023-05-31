class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):         # This extra method makes printing out our list easier by allowing us to interate through the nodes.
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List:
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node        # The head gets set to the new node.  
        self.tail = node        # The tail gets set to the new node
        return "The Doubly Linked List has been created"
        
    # Insert into Doubly Linked List:
    def insertDLL(self, value, location):
        if self.head is None:
            print("The node can't be inserted")
        else:
            newNode = Node(value)
            if location == 0:               # Option 1 - Insert at beginning
                newNode.prev = None             # the head does not have a previous reference in a non circular DLL
                newNode.next = self.head        # The newNode's next reference becomes the old head
                self.head = newNode             # The newNode becomes the new head
            elif location == -1:            # Option 2 - Insert at end
                newNode.next = None             # The tail does not have a next reference in a non circular DLL
                newNode.prev = self.tail        # The newNode's previous reference becomes the old tail
                self.tail.next = newNode        # The old tail's next reference becomes the newNode
                self.tail = newNode             # Then we can set the new tail as the newNode
            else:                           # Option 3 - Insert in the middle
                tempNode = self.head            # We start at the head and then traverse to the location we want
                index = 0   
                while index < location - 1:     # We iterate through until we find the location that is before the location that we want.
                    tempNode = tempNode.next    # tempNode = the node before where we want to insert
                    index += 1                  # [tempNode] <---> [newNode] 
                newNode.prev = tempNode         # The newNode's previous reference becomes the tempNode
                newNode.next = tempNode.next    # We save the tempNode's next reference into nextNode's next reference
                newNode.next.prev = newNode     # The node after newNode has it's previous reference set to newNode
                tempNode.next = newNode         # The tempNode's next reference is set to the newNode
            
    # Traversal of a Doubly Linked List
    def traverseDLL(self):
        if self.head == None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse traversal of a Doubly Linked List
    def reverseTraverseDLL(self):
        if self.head == None:
            print("There is not any element for traversal")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search for Element in Doubly Linked List
    def searchDLL(self, value):
        if self.head is None:
            return print("There is not any node in this DLL")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return print("The element was found in the DLL")
                tempNode = tempNode.next
            return print("The node does not exist in this DLL")

    # Deletion of a node in Doubly Linked List
    def deleteNode(self, location):
        if self.head is None:
            return print("This DLL is empty.  There is not a node to delete")
        else:
            if location == 0:                # Option 1 - Delete at beginning
                if self.head == self.tail:      # Scenario A - There is only 1 element in our list
                    self.head = None
                    self.tail = None
                else:                           # Scenario B - There is more than 1 element in our list
                    self.head = self.head.next      # The next element becomes the new head
                    self.head.prev = None           # The new head's previous reference is set to none
            elif location == -1:            # Option 2 - Delete at end
                if self.head == self.tail:      # Scenario A - There is only 1 element in our list
                    self.head = None
                    self.tail = None
                else:                           # Scenario B - There is more than 1 element in our list
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:                           # Option 3 - Delete in middle
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next          # curNode = the node before the node we want to delete
                    index += 1                      # [curNode] <-> [node we want to delete]
                curNode.next = curNode.next.next    # We set the curNode's next reference to the node after the node we want deleted
                curNode.next.prev = curNode         # The node that comes after curNode will then have it's previous reference set to curNode
            print("The node has successfully been deleted")

    # Delete Entire Doubly Linked List
    def deleteEntireDLL(self):
        if self.head is None:
            print("The DLL does not exist")
        else:               
            tempNode = self.head                    # We can't just set the head and tail to Null
            while tempNode:                         # We must delete the middle node's references to unlink everything to make the DLL nodes eligible for garbage collection
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)
print([node.value for node in doublyLL])    # Returns: [5]

doublyLL.insertDLL(0, 0)
doublyLL.insertDLL(2, -1)
doublyLL.insertDLL(6, 2)
print([node.value for node in doublyLL])    # Returns: [0, 5, 6, 2]

doublyLL.traverseDLL()
# Returns:
# 0
# 5
# 6
# 2

print(" ")
doublyLL.reverseTraverseDLL()
# Returns:
# 5
# 6
# 2

doublyLL.searchDLL(1) # Returns: "The node does not exist in this DLL"
doublyLL.searchDLL(2) # Returns: "The element was found in the DLL"

doublyLL.deleteNode(2)
print([node.value for node in doublyLL])    
# Returns: 
# "The node has successfully been deleted"
# [0, 5, 2]

doublyLL.deleteEntireDLL()
print([node.value for node in doublyLL])   # Returns []