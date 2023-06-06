# ------------------------------ Question 1 ------------------------------
# Sum of Digits
# How to find the sum of digits of a positive integer using recursion?

# Start by identifying the recursive pattern

def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'The number must be a positive integer only!'
    if n == 0:
        return 0
    else:
        return int(n%10) + sumOfDigits(int(n//10))  # modulus + floor division

print(sumOfDigits(4))           # Returns: 4    (4 = 4)
print(sumOfDigits(124))         # Returns: 7    (1 + 2 + 4 = 7)
print(sumOfDigits(120))         # Returns: 7    (1 + 2 + 0 = 3)

# ------------------------------ Question 2 ------------------------------
# Power
# How do you calculate the power of a number using recursion?
# Example 3^n = 27.  Where n = 3.

# Identify the pattern:
# 2^4
# x^a * x^b = x^(a+b)
# x^3 * x^4 = x^(3+4)

# x^n = x * x^(n-1)

def power(base, exp):
    assert int(exp) == exp, 'The exponent must be an integer number only!'
    if exp == 0:        
        return 1        # base ^ 0 = base
    elif exp < 0:                               
        return 1/base * power(base, exp+1)
    else:
        return base * power(base, exp-1)

print(" ")
print(power(4, 2))          # Returns: 16
print(power(4, -1))          # Returns: 0.25 or 1/4
print(power(4, -2))          # Returns: 0.0625 or 1/16
#print(power(4, 2.2))       # Returns: 'The exponent must be an integer number only!'

# ------------------------------ Question 3 ------------------------------
# Greatest Common Divisor
# Find greatest common divisor of two numbers without a remainder using recursion.

# Example: 8 and 12
# 8 = 2 * 2 * 2
# 12 = 2 * 2 * 3
# Answer: 2

# Euclidean Algorithm:
# 48/18 = 2 remainder 12
# 18/12 = 1 remainder 6 
# 12/6 = 2 remainder 0 

def gcd(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

print(" ")
print(gcd(48, 18))      # Returns: 6
print(gcd(18, 12))      # Returns: 6

# ------------------------------ Question 4 ------------------------------
# Number to Binary
# How to convert a number to binary using recursion
# Step 1: Divide the number by 2
# Step 2: Get the integer quotient for the next iteration
# Step 3: Get the remainder for the binary digit
# Step 4: Repeat the steps until the quotient is equal to 0

def numberToBinary(n):
    assert int(n) == n, 'The number must be an integer only'
    if n == 0:
        return 0
    else:
        return n%2 + 10 * numberToBinary(int(n//2))

print(" ")
print(numberToBinary(10))   # Returns: 1010
print(numberToBinary(312))  # Returns: 100111000