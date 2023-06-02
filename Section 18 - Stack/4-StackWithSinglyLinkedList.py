#-------------------------- Creating a Stack Using a Singly Linked List --------------------------

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        '''This function makes our Linked List iteratable so that we can print it'''
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        '''
        When we call the print statement, this method will be called. 
        This function makes our stack iteratable so that we can print the stack
        '''
        values = [str(x.value) for x in self.LinkedList]    # Convert the nodes to strings
        return '-> '.join(values)                            

    def isEmpty(self):
        '''Check if the stack is empty'''
        if self.LinkedList.head == None:
            return True
        else:
            return False
        
    def push(self, value):
        '''Push an element (the head) to the top of the stack'''
        node = Node(value)
        node.next = self.LinkedList.head        # Assign the node's next reference to the old head
        self.LinkedList.head = node             # Assign this node as the new head

    def pop(self):
        '''Pop the last element (the head) from the stack'''
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            nodeValue = self.LinkedList.head.value              # Save the head's value
            self.LinkedList.head = self.LinkedList.head.next    # Assign the head's next reference as the new head
            return nodeValue                                    # Print the head's value that got popped

    def peek(self):
        '''Return the last element (the head) from the stack'''
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            nodeValue = self.LinkedList.head.value              # Retrieve the head's node value
            return nodeValue
        
    def delete(self):
        '''Delete the stack/Singly Linked List'''
        self.LinkedList.head = None

        
customStack = Stack()
print(customStack.isEmpty())    # Returns: True
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)              # Returns: 3-> 2-> 1
print(customStack.pop())        # Returns: 3
print(customStack)              # Returns: 2-> 1
print(customStack.peek())       # Returns: 2

