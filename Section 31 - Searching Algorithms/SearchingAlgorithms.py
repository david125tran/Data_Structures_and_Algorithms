'''
Linear Search - The easiest search.  Searches elements sequentially one by one.

Binary Search - Faster than linear search.  Half of the remaining elements can 
be eliminated at a time, instead of eliminating them one by one.  Binary search
only works on sorted arrays.
'''

def linearSearch(array, value):
    '''Searches for a value in a given array.  Returns the index of the element if found.  
    Returns -1 if the element is not found.  Searches elements sequentially one by one'''
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1
        
array1 = [26, 42, 31, 50, 99]
print(linearSearch(array1, 50))         # Returns index 3
print(linearSearch(array1, 1250))       # Returns -1

import math
def binarySearch(array, value):
    '''Searches for a value in a given array.  Returns the index of the element if found.
    Returns -1 if the element is not found.  Eliminates of the remaining elements at a 
    time.'''
    start = 0                                                       
    end = len(array) - 1
    middle = math.floor((start + end)/2)

    while not(array[middle] == value) and start <= end:
        if value < array[middle]:                           # If the value is less than the middle element:
            end = middle - 1                                    # Look at only the 1st half
        else:                                               # If the value is more than the middle element:
            start = middle + 1                                  # Look at only the 2nd half
        middle = math.floor((start + end)/2)                # Move the middle to the new half
    if array[middle] == value:                              
        return middle                                       # Return the element if found
    else:
        return -1 
    
array2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#       Start           Mid                  End              
print(binarySearch(array2, 8))          # Returns index 7
print(binarySearch(array2, 15))         # Returns -1