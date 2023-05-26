#---------------- Create an Empty Dictionary ----------------
myDict = dict()
mySecondDict = {}

#---------------- Access Value from Dictionary's Key:Value Pair ----------------
engToSp = {"one": "uno",
           "two": "dos",
           "three": "tres"
           }
print(engToSp['one']) # returns "uno"

#---------------- Update an Element to Dictionary ----------------
myDict = {'name': 'Eddy', 
          'age': 26}
myDict['age'] = 27

#---------------- Add an Element to Dictionary ----------------
myDict['address'] = 'London'

#---------------- Traverse Through Dictionary ----------------
def traverseDictionary(dict):
    for key in dict:
        print(key, dict[key]) # --> key, value
traverseDictionary(myDict)
# Returns:
# 'name' 'Eddy'
# 'age' 27
# 'address 'London'

#---------------- Search for Value in Dictionary ----------------
# Linear Search Method:
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist within the dictionary'

print(searchDict(myDict, 'Eddy')) # Returns ('name', 'Eddy')
print(searchDict(myDict, 26)) # Returns 'The value does not exist within the dictionary'

#---------------- Delete Element in Dictionary ----------------
myDict = {'name': 'Eddy', 
          'age': 26,
          'address': 'London',
          'education': 'master'
          }
# .pop() method
myDict.pop('name')
print(myDict)
# Returns: 'age': 26, 'address': 'London', 'education': 'master'

# .popitem() method
myDict.popitem() # This deletes the last element
print(myDict) # Returns 'name': 'Eddy', 'age': 26, 'address': 'London'

myDict = {'name': 'Eddy', 
          'age': 26,
          'address': 'London',
          'education': 'master'
          }

print(myDict.popitem()) # Returns: ('education', 'master')

# .clear() method
myDict.clear()
print(myDict) # Returns {}

# del method
myDict = {'name': 'Eddy', 
          'age': 26,
          'address': 'London',
          'education': 'master'
          }

del myDict['name']
print(myDict)
# Returns: 'age': 26, 'address': 'London', 'education': 'master'

del myDict # Completely deletes it
#print(myDict) 
# # Returns: NameError: name 'myDict' is not defined

myDict = {'name': 'Eddy', 
          'age': 26,
          'address': 'London',
          'education': 'master'
          }

myDict.clear() # Completely deletes it
#print(myDict) 
# # Returns: NameError: name 'myDict' is not defined

#---------------- Dictionary Methods ----------------
myDict = {'name': 'Eddy', 
          'age': 26,
          'address': 'London',
          'education': 'master'
          }

# .copy() method
dictTwo = myDict.copy()

# .fromkeys() method
dictThree = {}.fromkeys([1, 2, 3], 0)
print(dictThree)
# This makes:
# dictThree = {1: 0, 2: 0, 3: 0}

# .get() method
print(myDict.get('name')) # Returns 'Eddy'
print(myDict.get('city')) # Returns 'None' because city doesn't exist in myDict

# .items() method
print(myDict.items())
# Returns dict_items([('name', 'Eddy'), ('age', 26), ('address', 'London'), ('education', 'master')])

# .keys() method
print(myDict.keys())
# Returns dict_keys(['name', 'age', 'address', 'education'])

# .setdefault() method
myDict.setdefault('defaultKey', 'defaultValue')
print(myDict)
# Returns:
# {'name': 'Eddy',
#   'age': 26,
#   'address': 'London', 
#   'education': 'master', 
#   'defaultKey': 'defaultValue'
#   }

# .values() method
print(myDict.values())
# Returns: dict_values(['Eddy', 26, 'London', 'master', 'defaultValue'])

# .update() method
newDict = {'a': 1,
           'b': 2,
           'c': 3}
myDict = {'name': 'Eddy', 
          'age': 26,
          'address': 'London',
          'education': 'master'
          }
myDict.update(newDict)
print(myDict) 
# This makes newDict key:value pairs get added to the end of myDict:
# myDict = {'name': 'Eddy', 
#           'age': 26,
#           'address': 'London',
#           'education': 'master',
#           'a': 1,
#           'b': 2,
#           'c': 3
#           }

#---------------- See if Key Exists ----------------
my_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four"
}

print(1 in my_dict) # Returns True

#---------------- See if Value Exists ----------------
print("one" in my_dict.values()) # Returns True

#---------------- Length ----------------
print(len(my_dict)) # Returns 4 (or the number of elements)

#---------------- Dictionary vs. List ----------------
# ---Dictionary---
# Unordered
# Access via keys
# Collection of key value pairs
# Preferred when you have unique key values
# No duplicate members

# ---List---
# Ordered
# Access via index 
# Collection of elements 
# Preferred when you have ordered data 
# Allow duplicate members 

#---------------- Dictionary Comprehension ----------------
#new_dict = {new_key:new_value for (key, value) in dict.items()}

# With if condition:
#new_dict = {new_key:new_value for (key, value) in dict.items() if condition}

import random
city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

new_dict = {city: random.randint(20, 30) for city in city_names}

print(new_dict)

#---------------- Exercises ----------------
# (1) Define a function to count the frequency of words in a given list of words. 
# Example:      words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# Output:       {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

# (2) Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
# Example:
#     dict1 = {'a': 1, 'b': 2, 'c': 3}
#     dict2 = {'b': 3, 'c': 4, 'd': 5}
#     merge_dicts(dict1, dict2)

# Output:
#     {'a': 1, 'b': 5, 'c': 7, 'd': 5}

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

