# ---------------------- Linked List Queue ---------------------- #

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        '''
        When we call the print statement on the object, this method will be called. 
        This function makes our stack iteratable so that we can print the stack
        '''
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class LinkedListQueue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        '''When we call the print statement, this method will be called'''
        values = [str(x) for x in self.linkedlist]
        return ' -> '.join(values)
    
    def enqueue(self, value):
        '''Takes a value and adds it to the end of the queue'''
        newNode = Node(value)
        if self.linkedlist.head == None:        # If the linked list is empty
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        else:                                   # Else
            self.linkedlist.tail.next = newNode         # The old tail's next reference becomes the newNode
            self.linkedlist.tail = newNode              # The newNode becomes the new tail

    def isEmpty(self):
        '''
        Checks to see if the queue is empty. 
        Returns True if the queue is empty.  
        Returns False if the queue is not empty.
        '''
        if self.linkedlist.head == None:
            return True
        else:
            return False

    def dequeue(self):
        '''Removes the 1st in element (the head) from the queue & the next element becomes the new head if there is one'''
        if self.isEmpty():
            return print("There is not any node in the queue")
        else:
            tempNode = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:        # If there is one node in the queue
                self.linkedlist.head = None                             # We set the head to null
                self.linkedlist.tail = None                             # We set the tail to null
            else:                                                   # If there is more than one node in the queue
                self.linkedlist.head = self.linkedlist.head.next        # The head's next reference shifts to the right one.  The old head becomes eligible for garbage collection
            return tempNode

    def peek(self):
        '''Returns the 1st element (the head) from the queue if there is one'''
        if self.isEmpty():
            return print("There is not any node in the queue")
        else:
            return self.linkedlist.head

    def delete(self):
        '''Deletes all items in the Queue'''
        self.linkedlist.head = None
        self.linkedlist.tail = None
        return print("The queue has been emptied")