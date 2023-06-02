# Stack - Is a data structure that stores items in a last-in/first-out manner

#-------------------------- Stack Operations Using Lists --------------------------
# append method
stack = []
stack.append(1)
stack.append(2)
stack.append(3)             # The elements get stacked on top of each other
print(stack)                # Returns: [1, 2, 3]

# pop method
top_stack = stack.pop()     # Returns the top element 
print(top_stack)            # Returns 3
print(stack)                # Returns: [1, 2]

#-------------------------- Stack Operations Using Lists vs Linked List --------------------------
# Using Lists:
# Easy to implement
# Speed problems when it grows
# Random access is possible

# Using Linked Lists:
# Harder to implement
# Fast performance - Because the elements in the list are not located contigiously/next to each other in memory
# Random access is not possible

