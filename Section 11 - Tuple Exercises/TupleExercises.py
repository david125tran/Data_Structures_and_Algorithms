# (1) Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.
# Example
#     input_tuple = (1, 2, 3, 4)
#     sum_result, product_result = sum_product(input_tuple)
#     print(sum_result, product_result)  # Expected output: 10, 24

def sum_product(t):
    sum_result = 0
    product_result = 1
     
    for num in t:
        sum_result += num
        product_result *= num
     
    return sum_result, product_result
     
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24

# (2) Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
# Example
#     tuple1 = (1, 2, 3)
#     tuple2 = (4, 5, 6)
#     output_tuple = tuple_elementwise_sum(tuple1, tuple2)
#     print(output_tuple)  # Expected output: (5, 7, 9)

def tuple_elementwise_sum(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))

# (3) Insert at the Beginning
# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
# Example
#     input_tuple = (2, 3, 4)
#     value_to_insert = 1
#     output_tuple = insert_value_front(input_tuple, value_to_insert)
#     print(output_tuple)  # Expected output: (1, 2, 3, 4)

def insert_value_at_beginning(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

# (4) Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
# Example
#     input_tuple = ('Hello', 'World', 'from', 'Python')
#     output_string = concatenate_strings(input_tuple)
#     print(output_string)  # Expected output: 'Hello World from Python'

def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

# (5) Diagonal
# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
# Example
#     input_tuple = (
#         (1, 2, 3),
#         (4, 5, 6),
#         (7, 8, 9)
#     )
#     output_tuple = get_diagonal(input_tuple)
#     print(output_tuple)  # Expected output: (1, 5, 9)

def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# Use a generator expression to iterate through the indices i from 0 to the 
# length of the input tuple minus one, and select the diagonal elements by 
# indexing the inner tuples with the same index i. Create a new tuple containing 
# the selected diagonal elements and return it.

# (6) Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.
# Example
#     tuple1 = (1, 2, 3, 4, 5)
#     tuple2 = (4, 5, 6, 7, 8)
#     output_tuple = common_elements(tuple1, tuple2)
#     print(output_tuple)  # Expected output: (4, 5)

def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

# Convert both input tuples into sets using the set() constructor, 
# then use the set intersection operator "&"" to find the common elements 
# between the two sets. Convert the resulting set of common elements back
# to a tuple and return it. 

