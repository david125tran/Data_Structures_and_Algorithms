'''
Sorting - Arranging data in a particular format.  Either ascending or descending. 

Types:
    *Bubble Sort
    *Selection Sort
    *Insertion Sort
    *Bucket Sort
    *Merge Sort
    *Quick Sort
    *Heap Sort

Which type to select?  Look at:
    *Stability
    *Space efficiency
    *Time efficiency

Categories:
    *Space Used
        *In place - Sorting algorithms which doesn't require extra space for sorting.
        *Out of place - Sorting algorithms which requires extra space for sorting. Ex. Merge sort.
    *Stability
        *Stable - Maintains the relative order of the items with equal sort keys.
        *Unstable - Doesn't maintain the relative order of the items with equal sort keys.

Example of Stability:
    *Unsorted array:     3, 5, 2, 1, 5', 10
    *Stable sort:        1, 2, 3, 5, 5', 10
    *Unstable sort:      1, 2, 3, 5', 5, 10

Sorting Terminologies:
    *Increasing Order - Successive elements are greater than previous ones.
        Ex.: 1, 3, 5, 7, 9, 11
    *Decreasing Order - Successive elements are less than previous ones.
        Ex.: 11, 9, 7, 5, 2, 1
    *Non Increasing Order - Successive elements are less than or equal to previous ones.
        Ex.: 11, 9, 7, 5, 5, 3, 1       (Contains duplicate values)
    *Non Decreasing Order - Successive elements are greater than or equal to previous ones.
        Ex.: 1, 3, 5, 7, 7, 9, 11       (Contains duplicate values)


Bubble Sort (aka Sinking Sort):
    *We repeatedly compare each pair of adjacent items and swap them if they aren't in order
    *We go from left to right sorting elements until we reach the end.  And then we circle 
    back to the start to keep sorting again.
    *Easy to implement
    *Space is a concern 
    *When to use: When the input is already sorted.  
    *When to avoid: When the average time complexity is poor.

Selection Sort:
    *We repeatedly find the minimum element and move it to the sorted part of the array to sort
    out an array.
    *Easy to use
    *When to use: When we have insufficient memory
    *When to avoid: When time is a concern

Insertion Sort:
    *Divides the given array into two parts.  Takes 1st element from the unsorted array & finds
    its correct position in the sorted array.  Repeats until the unsorted array is empty.
    *Easy to implement
    *When to use: When we have sufficient memory.  When we have continuous inflow of numbers & 
    want to keep them sorted
    *When to avoid: When time is a concern

Bucket Sort:
    *Create buckets & distribute elements of array into buckets
    *Sort buckets individually
    *Merge buckets after sorting
    *Number of buckets = round(squareRoot(number of elements))
    *Approriate bucket = cell((value * number of buckets) / maxValue)
    *Cell starts at index = 1
    *For example: bucket 1, bucket 2, bucket 3.  We do not start at bucket 0
    *When to use: When input is uniformily distributed over a range (the differences between the
    numbers is not drastic). Example of not uniform distribution: 1, 2, 4, 91, 93, 95. 
    Example of uniform distribution: 1, 2, 4, 5, 3, 8, 7, 9
    *When to avoid: When space is a concern.

Merge Sort:
    *Is a divide and conquer algorithm
    *Divide the input array into two halves & keep halving recursively until they can't be halved further
    *Merge halves by sorting them
    *When to use: When you need a stable sort & when the average expected time is O(NLogN)
    *When to avoid: When space is a concern 

Quick Sort:
    *Is a divide and conquer algorithm
    *Divides an array into smaller arrays recursively and then sorts the subarrays recursively.  

Heap Sort:
    *Step 1: Insert data into binary heap tree
    *Step 2: Extract data from the binary heap tree
    *It is best suited with arrays.  It doesn't work with linked lists

'''

def bubbleSort(customList):
    '''
    Takes a list (customList) & compares adjacent items starting from the beginning.  
    And then swaps items if they aren't sorted.
    '''
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):    # We will compare adjacent pairs.  Everytime, we must decrease the loops by 1
            if customList[j] > customList[j + 1]:                                       # If the current element is greater than the next element
                customList[j], customList[j + 1] = customList[j + 1], customList[j]         # We switch the pairs
    return customList

def selectionSort(customList):
    '''
    Takes a list (customList), repeatedly finds the minimum element, & then moves it
    to the sorted part of the array to sort out an array. 
    '''
    for i in range(len(customList)):    # i = index of left element
        min_index = i
        for j in range(i + 1, len(customList)):     # j = index of element to right of element of index i
            if customList[min_index] > customList[j]:       # if left > right
                min_index = j                                       # we make declare the right index as the index that has the smaller element
        customList[i], customList[min_index] = customList[min_index], customList[i]     # We swap places 
    return customList

def insertionSort(customList):
    '''
    Takes a list (customList) and sorts it by (1) dividing an array into 2 parts, (2) taking the
    1st element from the unsorted array & finding its correct position in the sorted array, and 
    then (3) repeating until the unsorted array is empty.
    '''
    for i in range(1, len(customList)):
        key = customList[i]                     # Temporarily store right element into key variable
        j = i - 1                               # We make the j index the index of the left element
        while j >= 0 and key < customList[j]:   # While we are still in the list and right element < left element:
            customList[j + 1] = customList[j]       # We swap the right element & left element  
            j -= 1                                  # Decrease j by 1
        customList[j + 1] = key                     # The smallest element to the left of element with index = i gets pushed into the list starting at the beginning
    return customList

import math
def bucketSort(customList):
    '''
    Takes a list (customList) and sorts it by (1) creating buckets, (2) distributing elements into the buckets,
    (3) sorting the buckets individually, and then (4) merging the buckets after sorting.
    '''
    numberOfBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    buckets = []
    
    # Append buckets into array
    for i in range(numberOfBuckets):
        buckets.append([])

    # Add each element from customList into the appropriate bucket where each bucket remains unsorted
    for j in customList:
        index_b = math.ceil(j * numberOfBuckets/maxValue)
        buckets[index_b - 1].append(j)

    # Sort each element from each bucket
    for i in range(numberOfBuckets):
        buckets[i] = insertionSort(buckets[i])

    # We merge each sorted bucket into customList
    k = 0
    for i in range(numberOfBuckets):
        for j in range(len(buckets[i])):
            customList[k] = buckets[i][j]
            k += 1
    return customList

def merge(customList, left, middle, right):
    '''
    A helper function for mergeSort().  Merges & sorts a customList given the left, middle, and right index.
    '''
    n1 = middle - left + 1      # n1 = number of elements in left subarray
    n2 = right - middle         # n2 = number of elements in right subarray

    L = [0] * (n1)              # Temporary left array
    R = [0] * (n2)              # Temporary right array

    for i in range(0, n1):                      # Copy the left elements to left array
        L[i] = customList[left + i]                 # The 0s in the L array get replaced with left elements in customList

    for j in range(0, n2):                      # Copy the right elements to right array
        R[j] = customList[middle + 1 + j]           # The 0s in the R array get replaced with right elements in customList

    i = 0       # i = initial index of left subarray
    j = 0       # j = initial index of right subarray
    k = left    # k = initial index of merged subarray

    # -------------Merge the subarrays, inserting the smallest elements at a time -------------
    while i < n1 and j < n2:            
        if L[i] <= R[j]:                    # If left element <= right element:
            customList[k] = L[i]                # Add the left element to customList at index k
            i += 1                              # Iterate to next element of left subarray
        else:                               # If the right element < left element:
            customList[k] = R[j]                # Add the right element to customList at index k
            j += 1                              # Iterate to next element of right subarray
        k += 1                              # Iterate to next element in customlist

    # -------------Merge any remaining elements from left subarray, if there are any -------------
    while i < n1:                       
        customList[k] = L[i]
        i += 1
        k += 1

    # -------------Merge any remaining elements from right subarray, if there are any -------------
    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

def mergeSort(customList, left, right):
    '''
    Takes a list (customList) and sorts it by dividing the list into two halves & 
    then keeps halving recursively until they can't be halved further.  And then calls 
    on merge() to merge and sort the halves back into a sorted list.  Takes left and right
    indexs of customList.  
    '''
    if left < right:
        middle = (left + (right - 1)) // 2          # //: divide with integral result (discard remainder)
        mergeSort(customList, left=left, right=middle)
        mergeSort(customList, left=(middle + 1), right=right)
        merge(customList, left, middle, right)
    return customList

def swap(my_list, index1, index2):
    '''A helper function for pivot().  Takes a list (my_list) and swaps two elements places located at index1 and index2'''
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def pivot(my_list, pivot_index, end_index):
    '''
    A helper function for quickSort().
    Takes a list (my_list), a pivot_index, and end_index.  
    Makes the 1st element located at index=0 the pivot number.
    Places elements lower than the pivot number to the left of the pivot number.
    Places elements greater than the pivot number to the right of the pivot number. 
    '''
    # The pivot number is the 1st element and located at index = 0
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):     # Start at pivot_index + 1 because the pivot number is at index = 0
        if my_list[i] < my_list[pivot_index]:               # If the element is less than the pivot number
            swap_index += 1                                     # Iterate the swap index to the next element
            swap(my_list, swap_index, i)                        # Swap the two elements places.
    swap(my_list, pivot_index, swap_index)              # Move the pivot number between the two segrated halves.  
    # [lower elements], [pivot number], [higher elements]
    return swap_index

def quickSortHelper(my_list, left, right):
    '''A helper function for quickSort().'''
    if left < right:                                    # Create a break for recursion
        pivot_index = pivot(my_list, left, right)
        quickSortHelper(my_list, left, pivot_index - 1)       
        quickSortHelper(my_list, pivot_index + 1, right)
    return my_list

def quickSort(myList):
    '''Takes a list (myList) and organizes it given a left and right index.'''
    return quickSortHelper(myList, 0, len(myList) - 1)

def heapify(customList, n, i):
    '''A helper function for heapSort().  Takes a list (customList) with n number of elements and a root (i)'''
    smallest = i                # We start with i being our root
    left = (2 * i) + 1          # Left child index
    right = (2 * i) + 2         # Right child index

    if left < n and customList[left] < customList[smallest]:        # If the left child is smaller than the root
        smallest = left                                                 # The smallest number is the left child
    
    if right < n and customList[right] < customList[smallest]:      # If the right child is smaller than the root
        smallest = right                                                # The smallest number is the right child

    if smallest != i:                                                               # If the smallest number is not the root number
        customList[i], customList[smallest] = customList[smallest], customList[i]       # We swap the smaller number with the root
        heapify(customList, n, smallest)                                                # Call the function recursively on the affected subtree

def heapSort(customList):
    '''Takes a list (customList) and sorts it using a binary heap tree.'''
    n = len(customList)
    for i in range(int(n/2) -1, -1, -1):                                # We start at the last parent with index of (int(n/2) - 1).  
        heapify(customList, n, i)

    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0) 
    customList.reverse()
    return(customList)

cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]

print(bubbleSort(cList))        # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(selectionSort(cList))     # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(insertionSort(cList))     # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bucketSort(cList))        # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(mergeSort(cList, 0, 8))   # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(quickSort(cList))         # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(heapSort(cList))          # Returns: [1, 2, 3, 4, 5, 6, 7, 8, 9]


