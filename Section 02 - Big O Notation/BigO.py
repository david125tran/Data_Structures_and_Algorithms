# ---------------- Big O Notation: Looking at Time Efficiency ----------------

# ---------------- O(1) Complexity ----------------
# Runs n = 1 times
def multiply_numbers(n):
    return n*n
# print(multiply_numbers(100))

# ---------------- O(N) Complexity ----------------
# Runs n = 5 times
def print_items(n):
    for i in range(n):
        print(i)
# print_items(5)

# ---------------- Drop Constants ----------------
# O(2N) Complexity
# O(2N) drops to O(N) because in big-O notation, we drop constants and low-order terms.
# Runs n = 10 times
def print_items(n):
    for i in range(n):
        print(i)
    for j in range (n):
        print(j)
# print_items(10)

# ---------------- O(N^2) Complexity ----------------
# Runs n = 10 * 10 times
def print_items(n):
    for i in range(n):
        for j in range (n):
            print(i, j)
# print_items(10)

# ---------------- Drop Non Dominant Terms ----------------
# O(N^2 + N) drops to O(N^2) Complexity because we drop the non dominant terms
def print_items(n):
    # O(N^2) Complexity
    for i in range(n):
        for j in range (n):
            print(i, j)
    # O(N) Complexity
    for k in range(n):
        print(k)
# print_items(10)

# ---------------- Add and Multiply Complexity ----------------

# O(a + b) Complexity
# If your algorithm is in the form "do this, then when you are all done, do that" then you add the runtimes
def print_items(a, b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)

# O(a * b) Complexity
# If your algorithm is in the form (do this for each time you do that) then you multiply the runtimes
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)
