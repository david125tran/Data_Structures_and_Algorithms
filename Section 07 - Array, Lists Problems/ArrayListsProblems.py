#---------------- Question 1 ----------------
# Middle Function
# Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.
myList = [1, 2, 3, 4]
def middle(list):
    # Note: poppedElement = list.pop() will return 4
    list.pop()
    list.pop(0)
    return(list)
print(middle(myList))

#---------------- Question 2 ----------------
# 2D Lists
# Given a 2D list calculate the sum of diagonal elements.
myList2D= [[1,2,3],
           [4,5,6],
           [7,8,9]]

def sumDiagonal(list):
    sum = 0
    for i in range(0, len(list)): 
        sum += list[i][i]
    return sum
print(sumDiagonal(myList2D)) 

#---------------- Question 3 ----------------
# Best Score
# Given a list, write a function to get first, second best scores from the list.
# List may contain duplicates.
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]

def firstSecond(givenList):
    max1 = max(givenList)
    givenList.remove(max1)
    max2 = 0
    for grade in givenList:
        if grade > max2:
            max2 = grade
    return max1, max2
print(firstSecond(myList))

#---------------- Question 4 ----------------
# Missing Number
# Write a function to find the missing number in a given integer array of 1 to 100.
myList = [1, 2, 3, 4, 6]
totalCount = 6
# Method A (Best Method)
def missingNumber(myList, totalCount):
    expectedSum = totalCount * ((totalCount + 1) / 2)
    actualSum = sum(myList)
    return int(expectedSum - actualSum)
print(missingNumber(myList, totalCount))

# Method B
def missingNumber(myList, totalCount):
    myList.sort() 
    for i in range(0, len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + 1 == myList[j]:
                break # You do not want to use a return statement here.  Or else it stays at i = 0 and keeps iterating through j going up +1
            else:
                return myList[i] + 1
print(missingNumber(myList, totalCount))

#---------------- Question 5 ----------------
# Duplicate Number
# Write a function to remove the duplicate number(s) on given integer array/list.
myList = [1, 1, 2, 2, 3, 4, 5]
def removeDuplicates(myList):
    output = []
    for element in myList:
        if element not in output:
            output.append(element) 
    return output
print(removeDuplicates(myList))

#---------------- Question 6 ----------------
# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
myList = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
sum = 7
def pairSum(myList, sum):
    output = []
    for i in range(0, len(myList)):
        for j in range(i + 1, len(myList)):
            if myList[i] + myList[j] == sum:
                output.append(f'{myList[i]}+{myList[j]}')
    return output
print(pairSum(myList, sum))
# Returns ['2+5', '4+3', '3+4', '-2+9']
