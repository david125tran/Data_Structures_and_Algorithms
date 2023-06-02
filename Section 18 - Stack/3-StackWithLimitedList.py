#-------------------------- Creating a Stack Using a Limited List --------------------------
class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list=[]

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        '''Check if the stack is empty'''
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        '''Check if the list is full'''
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self, value):
        '''Push a value to the end of the stack'''
        if self.isFull():
            print("The stack is full")
        else:
            self.list.append(value)
    
    def pop(self):
        '''Pop an element from the stack'''
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            self.list.pop()
        
    def peek(self):
        '''Return the last element from the stack'''
        if self.isEmpty():
            print("There is not any element in the stack")
        else:
            return print(self.list[len(self.list) - 1])   

    def delete(self):
        '''Delete the entire stack'''
        self.list = None


customStack = Stack(4)
print(customStack.isEmpty())    # Returns True
print(customStack.isFull())     # Returns False
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)              
# Returns
# 3
# 2
# 1

