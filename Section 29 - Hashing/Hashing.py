'''
Hashing - Is a method of sorting and indexing data.  The idea behind hashing
is to allow large amounts of data to be indexed using keys commonly created 
by formulas.  

Why Hashing?
    *It is time efficient in search operations

Hash function - It is a fucntion that can be used to map an arbitrary size to
data of a fixed size.  

Key - Input data by a user

Hash value - A value that is returned by hash function

Hash table - It is a data structure which implements an associative array abstract
data type, a structure that can map keys to values

Collision - A collision occurs when two different keys to a hash function produce 
the same output

These are simple examples of hashing. However, in the real world, hashing can be much 
more complex:
        *Integers (Mod function): 
            def mod(number, cellNumber):
                return number % cellNumber

        *String (ASCII function):
            def modASCII(string, cellNumber):
                total = 0
                for i in string:
                    total += ord(i)
                return total % cellNumber

Properties of A Good Hash Function:
    *It distributes hash values uniformly across hash tables
    *It has to use all input data (or it can cause potential collisions)

Collision Resolution Techniques
    *Direct Chaining - Implements the buckets as linked list.  Colliding elements are
    stored in lists.  
    *Open Addressing - Colliding elements are stored in other vacant buckets.  During
    storage and lookup these are found through so called probing.  
        a) Linear Probing - It places a new key into a closet following an empty cell
        b) Quadratic Probing - Adding arbitrary quadratic polynomial to the index until
        an empty cell is found
        c) Double Hasing - Interval between probes is computed by another hash function

Hash Table is Full
    *Direct Chaining - The hash table cannot become full from direct chaining.
    *Open Addressing - Create a new hash table that is 2x the size of the old hash table
    and recall the hashing for the current keys 

Pros and Cons of Collision Resolution Techniques
    *Direct Chaining:
        a) Hash table never gets full because of the linked lists
        b) The time complexity can lower the performance if the linked lists start getting
        full
    *Open Addressing:
        a) Easy implementation
        b) When the hash table is full, creation of a new hash table affects the performance.
        The time complexity for search operation becomes O(n).

If the input size is known, we always use "open addressing" 
If we perform deletion operatoins frequently, we should use "direct chaining"

Practical Use of Hashing
    *Password on servers
    *File system - File path is mapped to physical location on disk

Pros and Cons of Hashing:
    *Pro: Average insertion, deletion, and search operations take O(1) time complexity for 
    good hash functions
    *Con: When the hash function is not good enough, it takes O(n) time complexity



'''

