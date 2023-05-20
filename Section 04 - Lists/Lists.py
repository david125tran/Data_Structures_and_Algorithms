#---------------- Lists with Different Data Types ----------------
integers = [1, 2, 3, 4]
stringList = ['Milk', 'Cheese', 'Butter']
mixedList = [1, 1.5, 'Spam']
nestedList = [1, 2, 3, 4, 5, [1.5, 1.6], ['test']]
emptyList = []

#---------------- Accessing/Traversing a List ----------------
shoppingList = ['Milk', 'Cheese', 'Butter']
print(shoppingList[0]) # Returns 'Milk'
print(shoppingList[-1]) # Returns 'Butter' because counting backwards starts at -1

for i in range(len(shoppingList)):
    print(shoppingList[i])

#---------------- Seeing if Element is in List ----------------
print('Milk' in shoppingList) 
# Returns True if the element is in the list
# Returns Fale if the element is not in the list

#---------------- Update List ----------------
myList = [1, 2, 3, 4, 5, 6, 7]
myList[2] = 333
print(myList)

#---------------- Insert Element into List ----------------
myList = [1, 2, 3, 4, 5, 6, 7]
myList.insert(2, 103) # 2 is the index, 103 is the element you want to add
print(myList)

myList = [1, 2, 3, 4, 5, 6, 7]
myList.extend([8, 9, 10])
print(myList)

#---------------- Deletion in the List ----------------
# Slicing method
listSlice = myList[1:4] 
print(listSlice)
listSlice = myList[2:] # Iterates through to the end
print(listSlice)

# Pop method
myList = ['a', 'b', 'c', 'd', 'e']
myList.pop(1) # Where 1 is the index
print(myList) # Returns ['a', 'c', 'd', 'e']

myList = ['a', 'b', 'c', 'd', 'e']
myList.pop()
print(myList) # Returns ['a', 'b', 'c', 'd']

# Delete method
myList = ['a', 'b', 'c', 'd', 'e']
del myList[3] # Where 3 is the index
print(myList) # Returns ['a', 'b', 'c', 'e']

# Remove method
myList = ['a', 'b', 'c', 'd', 'e']
myList.remove('e')
print(myList) # Returns ['a', 'b', 'c', 'e']

#---------------- Search For Element in List ----------------
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# In operator method
if 20 in myList:
    print(f"The index is: {myList.index(20)}")
else:
    print("The value doesn't exist within the list")

# Linear Search method
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
def searchInList(list, value):
    for i in list:
        if i == value:
            return print(f"The index is: {myList.index(value)}")
    return print('The value does not exist in the list')
searchInList(myList, 20)

#---------------- List Operations/Functions ----------------
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c) # returns [1, 2, 3, 4, 5, 6]
print(a * 4) # returns [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
print(max(a)) # returns 3
print(min(a)) # returns 1
print(sum(a)) # returns 6
average = sum(a) / len(a)
print(average) # returns 2.0

#---------------- Strings and Lists ----------------
a = 'cat'
b = list(a)
print(b) # returns ['c', 'a', 't']
c = 'spam spam spam'
print(c.split()) # returns ['spam', 'spam', 'spam']
d = 'dog-dog-dog'
delimiter = '-'
print(d.split(delimiter)) # returns ['dog', 'dog', 'dog']
e = [12, 17, 3, 15, 1, 0, 5]
print(e.sort()) # returns [0, 1, 3, 5, 12, 15, 17], this change is permanent
f = [1, 2, 3]
print(f.append(4)) # returns [1, 2, 3, 4]

#---------------- Array vs. List ----------------
# Arrays:
# Arrays must have elements with all of the same data type
# Accessing an element is fast but insertion and deletion is slow because the elements are shifted 

# Lists:
# Lists can have elements with different data types
# Accessing an element is slow (because you have to traverse each element) but insertion and deletion is fast 
# If you delete an element at the end of the list, this process is fast
# If you delete an element at the beginning of the list, this process is slower because all of the elements have to shift to the left

#---------------- Questions ----------------
# -------------(1)-------------
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m): # m = [[1, 2], [3, 4]]
    v = m[0][0] # v = 1
    for row in m: 
        for element in row:
            if v < element: v = element
    return v # Returns v = 4
print(fun(data[0])) 

# -------------(2)-------------
fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:] # returns fruit_list3 = ['Apple', 'Berry', 'Cherry', 'Papaya']

    
fruit_list2[0] = 'Guava' # returns fruit_list1 = ['Guava', 'Berry', 'Cherry', 'Papaya'] 
                         # and
                         # returns fruit_list2 = ['Guava', 'Berry', 'Cherry', 'Papaya']
fruit_list3[1] = 'Kiwi' # returns fruit_list3 = ['Apple', 'Kiwi', 'Cherry', 'Papaya']

sum = 0
print(fruit_list1)
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava': # ls[0] = 'Guava', 'Guava', 'Apple'
        sum += 1 # +2
    if ls[1] == 'Kiwi': # ls[1] = 'Berry', 'Berry', 'Kiwi'
        sum += 20 # +20
  
print(sum) # Returns sum = 22

# -------------(3)-------------
a=[1,2,3,4,5]
print(a[3:0:-1]) # Returns [4, 3, 2], does not return 0 because it stops before the end

# -------------(4)-------------
#  What is the correct command to shuffle the following list?
fruit=['apple', 'banana', 'papaya', 'cherry']
import random 
random.shuffle(fruit)
print(fruit)

# -------------(5)-------------
arr = [[1, 2, 3, 4],
        [4, 5, 6, 7],
        [8, 9, 10, 11],
        [12, 13, 14, 15]]
for i in range(0, 4):
    print(arr[i].pop())
# Returns:
# 4
# 7
# 11
# 15
# The loop iterates through each row.  Because the pop() doesn't specify an index, it returns the last element of each row

# -------------(6)-------------
def f(value, values): # f(value = t = 3, values = v = [1, 2, 3])
    v = 1 
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0]) # Returns 3 44

# -------------(7)-------------
# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a) # Returns ValueError: attempt to assign sequence of size 6 to extended slice of size 5

# -------------(8)-------------
a=[1,2,3,4,5,6,7,8,9]
print(a[::2]) # Returns 1, 3, 5, 7, 9

# -------------(9)-------------
arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
# arr = [2, 3, 4, 5, 6, 6]
for i in range(0, 6): 
    print(arr[i], end = "_")
# Returns 2_3_4_5_6_6




