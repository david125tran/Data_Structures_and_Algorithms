#----------------------Question 1----------------------
# Three in One
# Describe how you could use a single Python list to implement three stacks

class Multistack:
    def __init__(self, stacksize):
        '''Takes a stacksize (how long you want your stack to be).  Ex. stacksize=4 means 3 stacks of 4 elements'''
        self.numberstacks = 3
        self.customList = [0] * (stacksize * self.numberstacks)
        self.size = [0] * self.numberstacks
        self.stacksize = stacksize

    def __str__(self):
        '''When we call the print statement, this method will be called'''
        values = [str(x) for x in self.customList]
        return ' , '.join(values)

    def isFull(self, stacknum):
        if self.size[stacknum] == self.stacksize:
            return True
        else:
            return False
        
    def isEmpty(self, stacknum):
        if self.size[stacknum] == 0:
            return True
        else:
            return False
        
    def indexOfTop(self, stacknum):
        '''Returns the index of the element in the customList'''
        offset = stacknum * self.stacksize
        return offset + self.size[stacknum] - 1
    
    def push(self, item, stacknum):
        '''Takes an item and places it into a stack'''
        if self.isFull(stacknum):
            return print("The stack is full")
        else:
            self.size[stacknum] += 1
            self.customList[self.indexOfTop(stacknum)] = item       # Adds the new item to the customList

    def pop(self, stacknum):
        '''Takes the top item from a stacknum and removes'''
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.customList[self.indexOfTop(stacknum)]      # Temporarily save the store the value as a variable
            self.customList[self.indexOfTop(stacknum)] = 0          # Replaces the top item with 0
            self.size[stacknum] -= 1
            return value
        
    def peek(self, stacknum):
        '''Shows the top item from a stacknum'''
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.customList[self.indexOfTop(stacknum)]
            return value


customStack = Multistack(4)     # This creates 3 stacks of length 4
print(customStack.isFull(0))    # Returns: False
print(customStack.isEmpty(1))   # Returns: True

customStack.push(1, 0)          # [1 , 0 , 0, 0]  [0 , 0, 0 , 0]  [0, 0 , 0 , 0]
customStack.push(2, 0)          # [1 , 2 , 0, 0]  [0 , 0, 0 , 0]  [0, 0 , 0 , 0]
customStack.push(3, 2)          # [1 , 2 , 0, 0]  [0 , 0, 0 , 0]  [3, 0 , 0 , 0]
customStack.push(33, 0)         # [1 , 2 , 33, 0]  [0 , 0, 0 , 0]  [3, 0 , 0 , 0]
customStack.push(44, 0)         # [1 , 2 , 33, 44]  [0 , 0, 0 , 0]  [3, 0 , 0 , 0]
customStack.push(55, 0)         # Returns: The stack is full

print(customStack.peek(0))      # Returns: 44
print(customStack.peek(1))      # Returns: The stack is empty
print(customStack.peek(2))      # Returns: 3
print(customStack.pop(0))       # Returns: 44

# Stack turns into:               [1 , 2 , 33, 0]  [0 , 0, 0 , 0]  [3, 0 , 0 , 0]
print(customStack)

#----------------------Question 2----------------------
# Stack Minimum
# How would you design a stack which, in addition to push and pop, has a function min which returns the minium element?  
class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ', ' + str(self.next)
        return string
    
class Stack():
    '''
    This class makes 2 distinct linked lists running parallel to each other starting at self.top and self.minNode.  
    These 2 linked lists have the same length.  The self.top LL runs like a normal LL.  with each new node being
    linked to the last.  However, the self.minNode keeps creating a new node with the lowest value node.

    For example, if we push 4, 5, 3, 2, 6:

    self.top will look like:            6 -> 2 -> 3 -> 5 -> 4
    self.minNode will look like:        2 -> 2 -> 2 -> 2 -> 6
    '''
    def __init__(self):
        self.top = None
        self.minNode = None

    def min(self):
        '''Returns the lowest value node from the stack if there is one'''
        if not self.minNode:                # If there is not a minimum node, return None
            return None                     # Else,
        return self.minNode.value           # Return the minium node
    
    def push(self, item):
        '''Pushs an item into two different linked lists of the same length.  Pushes into self.minNode and self.top linked list'''
        if self.minNode and (self.minNode.value < item):                            # If there is a self.minNode and the new item is greater than the last minimum node
            self.minNode = Node(value=self.minNode.value, next=self.minNode)            # We make a new node with the same minimum value and make it's next reference the last minimum node
        else:                                                                       # Else
            self.minNode = Node(value=item, next=self.minNode)                          # We make a new node with a value of the new item and make it's next reference the last minium node
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if not self.top:                    # If self.top = None, it returns None
            return None
        self.minNode = self.minNode.next    # Set the self.minNode node to the previous self.minNode node
        item = self.top.value               # Retrieve the top item from self.top linked list
        self.top = self.top.next            # Set the self.top node to the previous self.top node
        return item
    
print(" ")
customStack = Stack()
customStack.push(11)
customStack.push(12)
customStack.push(6)
customStack.push(15)
# self.top LL:          15 -> 6 -> 12 -> 11
# self.minNode LL:      6-> 6-> 11-> 11
print(customStack.min())                    # Returns: 6
print(customStack.pop())                    # Returns: 15
# self.top LL:          6 -> 12 -> 11
# self.minNode LL:      6-> 11-> 11
print(customStack.pop())                    # Returns: 6
# self.top LL:          12 -> 11
# self.minNode LL:      11 -> 11
print(customStack.min())                    # Returns: 11
print(customStack.pop())                    # Returns: 11
# self.top LL:          11
# self.minNode LL:      11

#----------------------Question 3----------------------
# Stack of Plates
# Imagine a literal stack of plates.  If the stack gets too high, it might topple.  Therefore, in real life,
# We would start a new stack when the previous stack exceeds some threshold.  Implement a data structure 
# setOfStacks that mimics this.  setOfStacks should be composed of several stacks and should create a new stack
# once the previous one exceeds capacity, setOfStacks.push() and setOfStacks.pop() should behave identically
# to a single stack.

class PlateStack():
    def __init__(self, capacity):
        '''
        Takes a capicty of number of plates a stack can hold.  
        Extra plates gets added into a new stack where self.stacks 
        represents the # of stacks of plates
        '''
        self.capacity = capacity
        self.stacks = []

    def __str__(self):
        return str(self.stacks)
    
    def push(self, item):
        '''
        Takes an item, and pushes it to the last plate stack if the
        last plate stack is not at capacity.  If it is, it creates
        a new plate stack.
        '''
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:     # If there is at least 1 stack and the last stack is not at capacity:
            self.stacks[-1].append(item)                                            # Append the last item to the last stack
        else:                                                                   # Else
            self.stacks.append([item])                                              # Append the last item as a new list.  Item must be covered by brackets, [] or else the code can break later on

    def pop(self):
        '''Returns the last plate in the last stack if there is a plate stack'''
        while len(self.stacks) > 0 and (len(self.stacks[-1])) == 0:             # If there is at least 1 stack and the last stack has an empty list, [] (Which may have been created from previously popping plate stacks)
            self.stacks.pop()                                                       # We must remove this empty list, [].  
        if len(self.stacks) == 0:                                               # If there are no plates
            return None                                                             # Return None
        else:                                                                   # Else
            return self.stacks[-1].pop()                                            # Return the last plate in the last stack

    def pop_at(self, stackNumber):
        '''Returns the last plate of a specified stack id, stackNumber, if there is a plate in the plate stack'''
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        else:
            return None
        
print(" ")
customStack = PlateStack(2)
print(customStack.pop())        # Returns: None
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)
print(customStack)              # Returns: [[2, 1], [4, 3]]
# Stack 0: [2] -> [1]
# Stack 1: [4] -> [3]

print(customStack.pop())        # Returns: 4
print(customStack.pop_at(0))    # Returns: 2          <- The top stack for stack 0
print(customStack)              # Returns: [[1], [3]]
print(customStack.pop_at(0))    # Returns: 1 
print(customStack)              # Returns: [[], [3]]

#----------------------Question 4----------------------
# Queue via Stacks
# Implement Queue class which implements a queue using two stacks
# Queues work by FIFO and Stacks work by LIFO

class Stack():
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
    
class QueueViaStack():
    def __init__(self):
        '''Creates a Queue that is created from two stacks.'''
        self.inStack = Stack()
        self.outStack = Stack()

    def enqueue(self, item):
        '''Pushes an item into the inStack'''
        self.inStack.push(item)

    def dequeue(self):
        '''
        Pushes elements from inStack to outStack in a LIFO manner. 
        Once all elements are transferred to outStack, the top element is popped out.
        All elements are then returned from outStack to inStack in a LIFO manner.
        '''
        while len(self.inStack):                        # While the inStack has an element:
            self.outStack.push(self.inStack.pop())          # Push all item from inStack to outStack in a LIFO manner
        result = self.outStack.pop()                    # Temporarily save the top element of outStack or most lowest/1st element from inStack as result variable
        while len(self.outStack):                       # While outStack has an element:
            self.inStack.push(self.outStack.pop())          # Push all items from outStack back into inStack EXCEPT for the result element that was popped off
        return result                                   # Return the result
    
print(" ")
customQueue = QueueViaStack()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
    #   [=3=]       [   ]
    #   [=2=]       [   ]
    #   [=1=]       [   ]
    #   inStack     outStack
print(customQueue.dequeue())        # Returns: 1
    #   [=3=]       [   ]
    #   [=2=]       [   ]
    #   inStack     outStack
customQueue.enqueue(4)
    #   [=4=]       [   ]
    #   [=3=]       [   ]
    #   [=2=]       [   ]
    #   inStack     outStack
print(customQueue.dequeue())        # Returns: 2
    #   [=4=]       [   ]
    #   [=3=]       [   ]
    #   inStack     outStack
print(customQueue.dequeue())        # Returns: 3
print(customQueue.dequeue())        # Returns: 4
print(customQueue.dequeue())        # Returns: None

#----------------------Question 5----------------------
# Animal Shelter
# An animal shelter, which holds only dogs and cats, operates on a strictly "FIFO" basis.
# People must adopt either the oldest (based on time of arrival) of all animals at the 
# shelter, or they can select whether they would prepfer a dog or a cat (and will receive 
# the oldest animal of that type).  They cannot select which specific animal they want.  
# Create the data structures to maintain this system and implment operations such as 
# enqueue, dequeueAny, deququeDog, and dequeueCat.

class AnimalShelter():
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueCat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop()
            return cat
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop()
            return dog
        
    def dequeueAny(self):
        if len(self.cats) == 0:
            result = self.dog.pop(0)
        else:
            result = self.cat.pop(0)
        return result
    
print(" ")
customQueue = AnimalShelter()
customQueue.enqueue('Cat1', 'Cat')
customQueue.enqueue('Cat2', 'Cat')
customQueue.enqueue('Dog1', 'Dog')
customQueue.enqueue('Cat3', 'Cat')
customQueue.enqueue('Dog2', 'Dog')
print(customQueue.dequeueCat())     # Returns: Cat3
print(customQueue.dequeueDog())     # Returns: Dog2