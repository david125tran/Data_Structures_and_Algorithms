#-------------------------- Creating a Stack Using an Unlimited List --------------------------
class Stack:
    def __init__(self):
        self.list = []

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
        
    def push(self, value):
        '''Push a value to the end of the stack'''
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

customStack = Stack()
print(customStack.isEmpty())    # Returns True

customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)              # Returns 
                                # 3
                                # 2
                                # 1
print("\n")
customStack.pop()
print(customStack)              # Returns 
                                # 2
                                # 3
print("\n")
customStack.peek()              # Returns 3

customStack.delete()