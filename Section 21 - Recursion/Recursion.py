# Recursion - A way of solving a problem by having a function calling itself. 
# You perform the same operation multiple times with different inputs with a way for it to exit the infinite loop.
# Recursive thinking can help break down big problems into smaller ones and easier to use.
# When to use recursion?  
#   a) When you can divide the problem into sub problems.
#   b) When we are fine with extra overhead (time and space) that comes with it
#   c) When we need a quick working solution instead of an efficient one
#   d) When we traverse a tree
#   e) When we use memoization in recursion (advanced topic)
# Recursion is used in many algorithms

# ------------------------------ Altering Recursion Limit ------------------------------
import sys
sys.setrecursionlimit(1000) 

# ------------------------------ Example ------------------------------
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only!'    # Throw an error if the number is not a positive integer
    if n in [0, 1]:                 # Create an exit
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))             # Returns 6
#print(factorial(-13))          # Returns error: 'The number must be a positive integer only!'

# ------------------------------ Fibonacci Example ------------------------------
# Fibonacci sequence is a sequence of numbers in which each number is the sum of the
# two preceeding ones and the sequence starts from 0 and 1
# Ex.   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...

#                         5  =    2   +    3       
# Follows the pattern:  f(n) = f(n-1) + f(n-2)

def fibonacci(n):
    '''Returns the (n)th number of the fibonnaci sequence starting at 0'''
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only!' 
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(" ")
print(fibonacci(6))         # Returns 8
print(fibonacci(0))         # Returns 0
print(fibonacci(1))         # Returns 0
# print(fibonacci(-1.5))    # Returns error: 'The number must be a positive integer only!'