#---------------- Question 1 ----------------
# What is the run time of the following:
def foo(array):
    sum = 0                                                 # O(1)
    product = 1                                             # O(1)
    for i in array:                                         # O(n)
        sum += i                                            # O(1)
    for i in array:                                         # O(n)
        product *= i                                        # O(1)
    print("Sum = "+str(sum)+", Product = "+str(product))    # O(1)

ar1 = [1,2,3,4]
foo(ar1)
# Answer: O(N)

#---------------- Question 2 ----------------
# What is the run time of the following:
def printPairs(array):
    for i in array:                         # O(n)  
        for j in array:                     # O(n)
            print(str(i)+","+str(j))        # O(1)
# Answer: O(N^2)

#---------------- Question 3 ----------------
# What is the run time of the following:
def printUnorderedPairs(array):                 
    for i in range(0,len(array)):               
        for j in range(i+1,len(array)):         
            print(array[i] + "," + array[j])    
# Answer: O(N^2)
# This one is sophisticated 

#---------------- Question 4 ----------------
# What is the run time of the following:
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

a = [1,2,3,4,5]
b= [2,6,7,8]
printUnorderedPairs(a, b)
# Answer: O(ab)

#---------------- Question 5 ----------------
# What is the run time of the following:
def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

printUnorderedPairs(a,b)
# Answer: O(ab)
 
#---------------- Question 6 ----------------
# What is the run time of the following:
def reverse(array):
    for i in range(0,int(len(array)/2)):
        other = len(array)-i-1
        temp = array[i]
        array[i] = array[other]
        array[other] = temp
    print(array)

reverse([1,2,3,4,5])
# Answer: O(N)

#---------------- Question 7 ----------------
# Which of the following are equivalent to O(N)? Why?
# 1. O(N + P), where P < N/2
# 2. O(2N)
# 3. O(N + logN)
# 4. O(N + NlogN)
# 5. O(N + M)

# Answer: 1, 2, 3.   Answer 5 is incorrect because there is no established relationship between N and M
