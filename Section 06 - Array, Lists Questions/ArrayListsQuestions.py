#---------------- Question 1 ----------------
# Find the missing number in an integer array of 1 to 100?
# This list has a msising number
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def findMissing(list, n): # Where n is the total number
    sum1 = sum(list)   # sum1 = 4977
    sum2 = n*(n + 1)/2 # sum2 = 100*(100 + 1)/2 = 5050
    print(sum2-sum1)   # 5050 - 4977 

findMissing(mylist, 100)

#---------------- Question 2 ----------------
# Two Sum
# Write a program to find all pairs of integers whose sum is equal to a given number.
# The pairs have to be distinct, for example, not 2 and 2.  And not 3, 3.
myList = [2, 6, 3, 9, 11]
target = 9
def findPairs(list, sum):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i]+list[j]) == sum:
                print(list[i],list[j])
findPairs(list=myList, sum=target) # Returns 6 3

#---------------- Question 3 ----------------
# How to check if an array contains a number in Python
# Arrays don't have a built in search, and so this is a method to search
import numpy as np 
myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

def findNumber(array, number): # This method is a linear search
    for i in range(len(array)):
        if array[i] == number:
            print(f"The number is at index: {i}")
findNumber(myArray, 12)

#---------------- Question 4 ----------------
# Find the maximum product of two integers in an array where all integers are positive
import numpy as np 
myArray = np.array([1, 20, 30, 44, 5, 56, 7, 8, 9, 10])
def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]*array[j] > maxProduct:
                maxProduct = array[i]*array[j]
                pairs = str(array[i])+ "," + str(array[j])
    print(pairs)
    print(maxProduct)

findMaxProduct(myArray)

#---------------- Question 5 ----------------
# Implment an algorithm to determine if a list has all unique characters, using python list.
# Method 1
myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]
def isUnique(list):
  a=[]
  for i in list:
    if i in a:
        print(i)
        return False
    else:
        a.append(i)
  return True

print(isUnique(myList))

# Method 2
myList = [1, 20, 30, 44, 5, 56, 57, 8, 19, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21]
def isUnique(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] == list[j]:
                return print(f"The list is not unique, the number {list[i]} is not unique")
    print("The list is unique")
isUnique(myList)


#---------------- Question 6 ----------------
# Given two strings, write a method to see if one is a permutation of another
# If two lists are permentations, they have the same elements but in different orders
def permutation(list1, list2):
    if list1.sort() == list2.sort():
        return print("The lists are permutations of each other")
    else:
        return print("The lists are not permutations of each other")
permutation([1, 2, 3], [3, 1, 2])
permutation(['b', 'a'], ['a', 'b'])

#---------------- Question 6 ----------------
# Given an image represented by an NxN matrix write a method to rotate the image by 90 degrees

def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix) # number of rows 
    for layer in range(n // 2): 
        # The floor operator '//', means discard the remainder of division
        # n // 2 gives the number of layers of a matrix
        # For example:
        # 1*1 array = 1 // 2 = 0.5 --> 1 layer
        # 2*2 array = 2 // 2 = 1.0 --> 1 layer
        # 3*3 array = 3 // 2 = 1.5 --> 2 layer
        # 4*4 array = 4 // 2 = 2.0 --> 2 layer
        # 5*5 array = 5 // 2 = 2.5 --> 3 layer 
        # Each layer is an outer surface of the middle array number?
        first = layer 
        last = n - layer - 1 
        for i in range(first, last):
            # Temporarily save the top into a variable
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

matrix1 = [[1,2], [3,4]]
import numpy as np
matrix2 = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])

print(matrix1)
print(rotate_matrix(matrix1))
print(matrix2)
print(rotate_matrix(matrix2))

