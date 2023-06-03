# Queue is a datra structure that stores item in a FIFO manner
# A new addition to the queue gets added to the end of the queue

# Queue Implementations:
# 1. Python List
#   a. List - Queue without capacity
#   b. Circular Queue - Queue with capacity where the last element is connected to the 1st element forming a circle.
# 2. Linked list

# ---------------------- List Queue ---------------------- #

class ListQueue:
    def __init__(self):
        '''When initialized, creates an empty Queue without a maximum size'''
        self.items = []

    def __str__(self):      
        '''When we call the print statement, this method will be called'''
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        '''
        Checks to see if the queue is empty. 
        Returns True if the queue is empty.  
        Returns False if the queue is not empty.
        '''
        if self.items == []:
            return True
        else:
            return False
        
    def enQueue(self, value):
        '''Takes a value and appends it to the end of the queue'''
        self.items.append(value)
        return print("The element is inserted at the end of Queue")
    
    def dequeue(self):
        '''Pops the 1st in element in the queue if there is one'''
        if self.isEmpty():
            return print("There is not any element in the Queue")
        else:
            return self.items.pop(0)
        
    def peek(self):
        '''Returns the 1st element from the queue if there is one'''
        if self.isEmpty():
            return print("There is not any element in the Queue")
        else:
            return print(self.items[0])
        
    def delete(self):
        '''Deletes all items in the Queue'''
        self.items = None
        return print("The queue has been emptied")

print("\nQueue")
customListQueue = ListQueue()
customListQueue.enQueue(1)
customListQueue.enQueue(2)
customListQueue.enQueue(3)
print(customListQueue.isEmpty())    # Returns: False
print(customListQueue)              # Returns: 1 2 3
customListQueue.dequeue()           
print(customListQueue)              # Returns: 2 3
customListQueue.peek()              # Returns: 2
customListQueue.delete()            # Returns: "The queue has been emptied"

# ---------------------- Circular Queue ---------------------- #

class circularQueue():
    def __init__(self, maxSize):
        '''When initialized, takes a maximum size as maxSize.  And creates an empty circular Queue of maxSize elements'''
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1     # self.start represents the index of the start
        self.top = -1       # self.top represents the index of the top

    def __str__(self):
        '''When we call the print statement, this method will be called'''
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        '''
        Checks to see if the Queue is full. 
        Returns True if the queue is full.  
        Returns False if the queue is not full.
        '''
        if self.top + 1 == self.start:                          # Condition 1: The start is not at 0 and top + 1 points to the start
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:  # Condition 2: The start is at 0 and the top is the last element
            return True
        else:                                                   # Condition 3: The queue is not full
            return False
        
    def isEmpty(self):
        '''
        Checks to see if the queue is empty. 
        Returns True if the queue is empty.  
        Returns False if the queue is not empty.
        '''
        if self.top == -1:      # If the top variable is -1, we know the queue is empty
            return True
        else:
            return False
        
    def enqueue(self, value):
        '''Takes a value and appends it to the end of the queue'''
        if self.isFull():
            return print("The queue is full")
        else:
            if self.top + 1 == self.maxSize:    # If our top is already at the end of the queue AND the queue is not full, then we have now exceeded the last element.
                self.top = 0                        # We then start from the 1st element due to circularity; where self.top = 0 refers to the 1st element.  
            else:                               # else:
                self.top += 1                       # We add 1 to the self.top to point to the next element in the list
                if self.start == -1:            # If our queue is empty
                    self.start = 0                  # We need to update our start to 0 where self.start = 0 refers to the 1st element
            self.items[self.top] = value            # We then add the item to the top of the queue
            return print("The element is inserted at the end of the Queue")

    def dequeue(self):
        '''Removes the 1st in element (the start) from the queue if there is one'''
        if self.isEmpty():
            return print("The queue is empty.  There is no element to remove")
        else:
            firstElement = self.items[self.start]   # Temporarily store the value of the 1st element into firstElement variable
            start = self.start                      # Temporarily store the index of the start into start variable
            
            if self.start == self.top:              # If there is one element in the queue
                self.start = -1                         # Reset start index to -1
                self.top = -1                           # Reset top index to -1
            elif self.start + 1 == self.maxSize:    # If the start is at the end of the queue, 
                self.start = 0                          # We then move the start to the beginning of the queue due to circularity
            else:                                   # Else
                self.start += 1                         # We then move the start to the right by +1 element
            self.items[start] = None                # We replace the old start with Null
            return print(f"The element, '{firstElement}', has been removed from the queue")                   
        
    def peek(self):
        '''Returns the 1st element from the queue if there is one'''
        if self.isEmpty():
            return print("The queue is empty.  There is no element to remove")
        else:
            return print(self.items[self.start])

    def delete(self):
        '''Deletes all items in the Queue'''
        self.items = self.maxSize * [None]
        self.start = -1     # Reset the start index to -1
        self.top = -1       # Reset the top index to -1
        return print("The queue has been emptied")

print("\n\nCircular Queue")
customCircularQueue = circularQueue(3)
print(customCircularQueue.isFull())         # Returns: False
print(customCircularQueue)                  # Returns: None None None
print(customCircularQueue.isEmpty())        # Returns: True
customCircularQueue.enqueue(1)              # Returns: "The element is inserted at the end of the queue"
customCircularQueue.enqueue(2)              # Returns: "The element is inserted at the end of the queue"
customCircularQueue.enqueue(3)              # Returns: "The element is inserted at the end of the queue"
print(customCircularQueue)                  # Returns: 1 2 3
customCircularQueue.dequeue()               # Returns: "The element, '1', has been removed from the queue"
customCircularQueue.peek()                  # Returns: 2
customCircularQueue.delete()                # Returns: "The queue has been emptied"

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
            return print(f"{tempNode}")

    def peek(self):
        '''Returns the 1st element (the head) from the queue if there is one'''
        if self.isEmpty():
            return print("There is not any node in the queue")
        else:
            return print(self.linkedlist.head)

    def delete(self):
        '''Deletes all items in the Queue'''
        self.linkedlist.head = None
        self.linkedlist.tail = None
        return print("The queue has been emptied")
    
print("\n\nLinked List Queue")
customLinkedListQueue = LinkedListQueue()
customLinkedListQueue.enqueue(1)
customLinkedListQueue.enqueue(2)
customLinkedListQueue.enqueue(3)
print(customLinkedListQueue)                        # Returns: 1 -> 2 -> 3
customLinkedListQueue.dequeue()                     # Returns: 1
customLinkedListQueue.peek()                        # Returns: 2
customCircularQueue.delete()                        # Returns: The queue has been emptied

# ---------------------- Collections Module ---------------------- #
# The deque class can serve as a queue and a stack because it is a doubly linked list
from collections import deque

print("\n\nCollections Module")
customQueue = deque(maxlen=3)
print(customQueue)              # Returns: deque([], maxlen=3)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)           # If the queue is full, it deletes the 1st element 
print(customQueue)              # Returns: deque([2, 3, 4], maxlen=3)
print(customQueue.popleft())    # Returns: 2
print(customQueue.clear())      # Returns: None

# ---------------------- Queue Module ---------------------- #
import queue as q

customQueue = q.Queue(maxsize=3)

print("\n\nQueue Module")
print(customQueue.qsize())          # Returns: 0        returns count of queue
print(customQueue.empty())          # Returns: True     
print(customQueue.full())           # Returns: False
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.qsize())          # Returns: 3
print(customQueue.qsize())          # Returns: 0
print(customQueue.get())            # Returns: 1        removes the 1st element
print(customQueue.qsize())          # Returns: 2

# ---------------------- Multiprocessing Module ---------------------- #
from multiprocessing import Queue

print("\n\nMultiprocessing Module")
customQueue = Queue(maxsize=3)
customQueue.put(1)
print(customQueue.get())            # Returns: 1

