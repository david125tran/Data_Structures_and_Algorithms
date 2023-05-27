# A tuple is an immutable sequence of Python objects
# Tuples are also comparable and hashable

#---------------- Create a tuple ----------------
newTuple = ('a', 'b', 'c', 'd', 'e')

#---------------- Create a tuple with one element ----------------
newTuple = ('a',)
# When creating  a single element tuple, you need a comma, ',' at the end of the element or else Python will create a string instead of a tuple

#---------------- Create an empty tuple ----------------
newTuple = tuple()

#---------------- Accessing elements of tuple ----------------
newTuple = ('a', 'b', 'c', 'd', 'e')
print(newTuple[1]) # Returns 'b'
print(newTuple[-1]) # Returns 'e'
print(newTuple[1:3]) # Returns ('b', 'c'), the last index is not included

#---------------- Traversing a tuple ----------------
for i in newTuple:
    print(i)

#---------------- Search for an element in a tuple ----------------
newTuple = ('a', 'b', 'c', 'd', 'e')
print('b' in newTuple) # Returns True
print(newTuple.index('e')) # Returns 4
# print(newTuple.index('f')) # Returns error and code breaks

def searchTuple(p_tuple, element):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == element:
            return f"The {element} is found at {i} index"
    return "The element is not found"

print(searchTuple(newTuple, 'a'))

#---------------- Tuple operations/functions ----------------
myTuple = (1,4,3,2,5)
myTuple1 = (1,2,6,9,8,7)
print(myTuple + myTuple1) # Returns (1, 4, 3, 2, 5, 1, 2, 6, 9, 8, 7)
print(myTuple * 4) # Returns (1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5, 1, 4, 3, 2, 5)
print(4 in myTuple) # Returns True
print(14 in myTuple) # Returns False
print(myTuple.count(2)) # Returns 1
print(myTuple.count(12)) # Returns 0
print(myTuple.index(4)) # Returns 1
# print(myTuple.index(14)) # Returns error and breaks code
print(len(myTuple)) # Returns 5
print(max(myTuple)) # Returns 5

#---------------- Convert list to tuple ----------------
list = [1, 2 ,3]
myTuple2 = tuple(list)

#---------------- Methods that can NOT be used for tuples ----------------
# append()
# insert()
# remove()
# pop()
# clear()
# sort()
# reverse()


