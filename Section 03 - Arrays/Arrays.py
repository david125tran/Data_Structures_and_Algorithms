# ----------------------------- Creating Arrays -----------------------------
import array
my_array = array.array('i')
print(my_array)

my_array1 = array.array('i', [1, 2, 3, 4])
print(my_array1)

import numpy as np
np_array = np.array([], dtype=int)
print(np_array)
np_array = np.array([1, 2, 3, 4])
print(np_array)

# ----------------------------- Inserting Elements Into Arrays -----------------------------
# Beginning of Array:
my_array1.insert(0, 6)
print(my_array1)

# At an index of Array:
my_array1.insert(3, 11)
print(my_array1)

# End of Array:
my_array1.insert(100, 200)
print(my_array1)

# ----------------------------- Array Traversal -----------------------------
def traverseArray(array):
    for i in array:
        print(i)
traverseArray(my_array1)

from array import *
arr1 = array('i', [1, 2, 3, 4, 5, 6])

def accessElement(array, index):
    if index >= len(array):
        print('There is not any element at this index')
    else:
        print(array[index])
accessElement(arr1, 6)

# ----------------------------- Searching for an Element -----------------------------
my_array1= array('i', [1, 2, 3, 4, 5])
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "The element is not found"
print(linear_search(my_array1, 6))

# ----------------------------- Delete an Element -----------------------------
my_array1= array('i', [1, 2, 3, 4, 5])
my_array1.remove(2) # Where 2 is the index you want removed
print(my_array1)

# ----------------------------- Access individual elements through indexes -----------------------------
print(my_array1[3])

# ----------------------------- Append any value to the array using append() method -----------------------------
my_array.append(6)
print(my_array)

# ----------------------------- Insert value in an array using insert() method -----------------------------
my_array.insert(3, 11)
print(my_array)

# ----------------------------- Extend python array using extend() method -----------------------------
my_array1 = array('i', [10,11,12])
my_array.extend(my_array1)
print(my_array)

# ----------------------------- Add items from list into array using fromlist() method -----------------------------
tempList = [20,21,22]
my_array.fromlist(tempList)
print(my_array)

# ----------------------------- Remove any array element using remove() method -----------------------------
my_array.remove(11)
print(my_array)

# ----------------------------- Remove last array element using pop() method -----------------------------
my_array.pop()
print(my_array)

# ----------------------------- Fetch any element through its index using index() method -----------------------------
print(my_array.index(21))

# ----------------------------- Reverse a python array using reverse() method -----------------------------
my_array.reverse()
print(my_array)

# ----------------------------- Get array buffer information through buffer_info() method -----------------------------
print(my_array.buffer_info())

# ----------------------------- Check for number of occurrences of an element using count() method -----------------------------
my_array.append(11)
print(my_array.count(11))
print(my_array)

# ----------------------------- Convert array to a python list with same elements using tolist() method -----------------------------
print(my_array.tolist())

# ----------------------------- Slice Elements from an array -----------------------------
print(my_array[:])

# ----------------------------- Create Two Dimensional Array -----------------------------
import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# ----------------------------- Insertion Into Two Dimensional Array -----------------------------
# Adding a column
newTwoDArray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=1)
# "0" inserts the new column into the index=0
# axis=0 adds it as a row
# axis=1 adds it as a column
print(newTwoDArray)

# Adding a row
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
newTwoDArray = np.insert(twoDArray, 0, [1, 2, 3, 4], axis=0)
# "0" inserts the new column into the index=0
# axis=0 adds it as a row
# axis=1 adds it as a column
print(newTwoDArray)

# ----------------------------- Accessing an Element in Two Dimensional Array ----------------------------- 
twoDArray = np.array([
    [11, 15, 10, 6], 
    [10, 14, 11, 5], 
    [12, 17, 12, 8], 
    [15, 18, 14, 9]
    ])
print(twoDArray[0][1]) # Where "0" is the row index and "1" is the column index

# ----------------------------- Accessing an Element in Two Dimensional Array ----------------------------- 
import numpy as np
twoDArray = np.array([
    [11, 15, 10, 6], 
    [10, 14, 11, 5], 
    [12, 17, 12, 8], 
    [15, 18, 14, 9]
    ])
def accessElement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])
accessElement(twoDArray, 0, 2)

# ----------------------------- Return Number of Rows of Two Dimensional Array -----------------------------
print(len(twoDArray))

# ----------------------------- Return Number of Columns of Two Dimensional Array -----------------------------
print(len(twoDArray[0]))

# ----------------------------- Traversing a Two Dimensional Array ----------------------------- 
def traverseTDArray(array):
    for i in range(len(array)): # For each element of each Row, do this:
        for j in range(len(array[0])): # For each element of each Column, do this:
            print(array[i][j])
traverseTDArray(twoDArray)

# ----------------------------- Search a Two Dimensional Array for an Element -----------------------------
twoDArray = np.array([
    [11, 15, 10, 6], 
    [10, 14, 11, 5], 
    [12, 17, 12, 8], 
    [15, 18, 14, 9]
    ])
def searchTDArray(array, value):
    for i in range(len(array)): # For each element of each Row, do this:
        for j in range(len(array[0])): # For each element of each Column, do this:
            if array[i][j] == value:
                return f'The value is located at index [{i}][{j}]'
        return 'The element is not found'
print(searchTDArray(twoDArray, 15))

# ----------------------------- Delete a Row from a Two Dimensional Array -----------------------------
newTDArray = np.delete(twoDArray, 0, axis=0)
# axis=0 removes it as a row
# axis=1 removes it as a column
print(newTDArray)

# ----------------------------- Delete a Column from a Two Dimensional Array -----------------------------
newTDArray = np.delete(twoDArray, 0, axis=1)
# axis=0 removes it as a row
# axis=1 removes it as a column
print(newTDArray)

