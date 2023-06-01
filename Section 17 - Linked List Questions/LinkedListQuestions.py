#----------------------Question 1----------------------
# Remove duplicates
# Write a code to remove duplicates from an unsorted linked list

from LinkedList import LinkedList

def removeDups(ll):
    if ll.head is None:
        return
    else:
        currentNode = ll.head
        visited = set([currentNode.value])
        while currentNode.next:
            if currentNode.next.value in visited:           # If the next node is in the visited set, we delete this next node
                currentNode.next = currentNode.next.next    # We iterate to the next next node
            else:                                           
                visited.add(currentNode.next.value)         # If the next node is not in the visited set, we add it to the visited set
                currentNode = currentNode.next              # We iterate to the next node
        return ll                                           # We then return the linked list that has had it's duplicates removed and unlinked

customLL = LinkedList()
customLL.generate(7, 0, 10)
print('\n')
print("Question 1")
print(customLL) # Returns 3 -> 0 -> 10 -> 10 -> 4  -> 2  -> 4
removeDups(customLL)
print(customLL) # Returns 3 -> 0 -> 10 -> 4  -> 2  

#----------------------Question 2----------------------
# Return Nth to Last
# Implement an algorithm to find the nth to last element of a singly linked list
# So if n = 3, we return the 3rd last node

from LinkedList import LinkedList

def nthToLast(ll, n):
    '''Return n steps from the last node of linked list, ll'''
    pointer1 = ll.head                  # We initially start pointer 1 & 2 at the head.  
    pointer2 = ll.head

    for i in range(n):
        if pointer2 is None:            # If the LL has no nodes, return None
            return None
        pointer2 = pointer2.next        # We then move pointer2 n number of nodes apart from pointer 1
                                        # While we keep pointer 1 at the head
    while pointer2:                     # We iterate through until pointer 2 reaches the end
        pointer1 = pointer1.next        # At each iteration, pointer 1 and 2 both move 1 node
        pointer2 = pointer2.next        # When pointer 2 reaches the end, pointer 1 will be n steps from the last node of the Linked List
    return pointer1                     # We return the answer

customLL = LinkedList()
customLL.generate(10, 0, 99)

print('\n')
print("Question 2")
print(customLL)
# Returns: 78 -> 9 -> 91 -> 62 -> 85 -> 44 -> 23 -> 41 -> 24 -> 35
print(nthToLast(customLL, 3))
# Returns: 41

#----------------------Question 3----------------------
# Partition
# Write code to partition/divide a linked list around a value x, such that all 
# nodes less than x come before all nodes greater than or equal to x

from LinkedList import LinkedList

def partition(ll, x):
    curNode = ll.head                   # We create a temporary single node Linked List with the 1st node
    ll.tail = ll.head                   
    
    while curNode:
        nextNode = curNode.next         # Temporarily save the curNode's next reference into nextNode
        curNode.next = None             # We replace the curNode's next reference to Null
        if curNode.value < x:           # If the node value is lower than x, we attach at beginning
            curNode.next = ll.head          # The node's next reference becomes the old head
            ll.head = curNode               # This node then becomes the new head
        else:                           # If the node value is greater than x, we attach at end
            ll.tail.next = curNode          # The old tail's next reference becomes the node
            ll.tail = curNode               # The node then becomes the new tail
        curNode = nextNode              # We iterate to the next node 
    
    ll.tail.next = None                 # If all nodes are less than x, this makes sure that the tail's next reference 
                                        # is set to null so that we don't have a circular infinite linked list

customLL = LinkedList()
customLL.generate(15, 0, 9)

print('\n')
print("Question 3")
print(customLL) # Returns: 29 -> 89 -> 3 -> 72 -> 81 -> 85 -> 32 -> 59 -> 55 -> 48 -> 88 -> 96 -> 8 -> 41 -> 0
partition(customLL, 50)
print(customLL) # Returns: 0 -> 41 -> 8 -> 48 -> 32 -> 3 -> 29 -> 89 -> 72 -> 81 -> 85 -> 59 -> 55 -> 88 -> 96
# The values less than 50 are located are on the left.  THe values located more than 50 are located on the right.

#----------------------Question 4----------------------
# Sum Linked List
# You have two numbers represented by a linked list, where each node contains a single digit
# The digits are stored in reverse order, such that the 1's digit is at the head of the list
# Write a function that adds the two numbers and returns the sum as a linked list
# Example: 
# list1 = 7 -> 1 -> 6    ----> 617    \
#                                       ---->  617 + 295 = 912    ---->    sumList = 2 -> 1 -> 9
# list2 = 5 -> 9 -> 2    ----> 295    /

from LinkedList import LinkedList

def sumList(llA, llB):
    n1 = llA.head                               # We start at the head
    n2 = llB.head                               
    carry = 0                                   # And initialize the carry to 0
    ll = LinkedList()                            

    while n1 or n2:
        result = carry                          # For each iteration, the carry over from the last iteration is added to our result
        if n1:
            result += n1.value                  # Add n1 value to the result
            n1 = n1.next
        if n2:
            result += n2.value                  # Add n2 value to the result
            n2 = n2.next                        
        ll.add(int(result % 10))                # We add the one's digit to our linked list.  Fro example 7 + 5 = 12.  We add "2"
        carry = (result - (result % 10))/ 10    # And then the "1" from the remaining "10" gets carried to the next step
    
    if int(carry) != 0:                         # If there is a carry leftover at the end, we add it to the linked list
        ll.add(int(carry))

    return ll 

llA = LinkedList()
llA.add(7)
llA.add(1)
llA.add(6)

llB = LinkedList()
llB.add(5)
llB.add(9)
llB.add(2)

print('\n')
print("Question 4")
print(sumList(llA, llB))

#----------------------Question 5----------------------
# Intersection
# Given two singly linked lists, determine if the two lists intersect.  Return the intersecting node.
# Note that the intersection is defined based on reference, not value.  That is, if the kth node of the 1st
# linked list is the exact same node (by reference), as the jth node of the 2nd linked list, then they are
# intersecting

# Example of intersecting linked lists:
# 3 -> 1 -> 5 -> 9 \
#                    -> 7 -> 2 -> 1
#      2 -> 4 -> 6 /
# Here they both point to the same 7 node

# Example of non intersecting linked list
# 3 -> 1 -> 5 -> 9 -> 7 -> 2 -> 1
#      2 -> 4 -> 6 -> 7 -> 2 -> 1
# They do not point to the same 7 node

from LinkedList import LinkedList, Node

def intersection(llA, llB):
    if llA.tail is not llB.tail:            # If the tails are not the same, the lists are not intersecting
        return False
    
    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA < lenB else llB   # Find the shorter linked list
    longer = llB if lenA < lenB else llA    # Find the longer linked list 

    diff = len(longer) - len(shorter)       # Get the difference in node length
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):                   # Traverse through the longer node until you get to the node
        longerNode = longerNode.next        # that makes both nodes of equal length
                                            # There is no neeed to look at extra nodes before potential intersections
    while shorterNode is not longerNode:    
        shorterNode = shorterNode.next  
        longerNode = longerNode.next        # If an intersection is found, the loop exits at the node that is the intersection

    return longerNode                       # If no intersection is found the while loop exits and False is returned 


# Helper addition method to make an intersecting linked list
def addSameNode(llA, llB, value):
    '''This function takes 2 linked lists, and intersects them at the end with a new value'''
    tempNode = Node(value)
    llA.tail.next = tempNode    # Set the old tail's next reference to the new value/node
    llA.tail = tempNode         # Se the new value/node as the new tail
    llB.tail.next = tempNode    # Set the old tail's next reference to the new value/node
    llB.tail = tempNode         # Se the new value/node as the new tail

llA = LinkedList()
llA.generate(3, 0, 10)          # Make a random linked list that is 3 nodes long
llB = LinkedList()
llB.generate(4, 0, 10)          # Make a random linked list that is 3 nodes long
addSameNode(llA, llB, 11)       # Make llA and llB intersect at a new tail of value 11
addSameNode(llA, llB, 14)       # Make llA and llB intersect at a new tail of value 14

print('\n')
print("Question 5")
print(llA)                      # Returns: 0 -> 2 -> 6 -> 11 -> 14
print(llB)                      # Returns: 4 -> 0 -> 9 -> 1 -> 11 -> 14
print(intersection(llA, llB))   # Returns: 11 because the list intitially links at 11

#      0 -> 2 -> 6 -> 11 -> 14 \
#                                -> 11 -> 14
# 4 -> 0 -> 9 -> 1 -> 11 -> 14 /

llA.generate(3, 0, 10)          # Make a random linked list that is 3 nodes long
llB.generate(3, 0, 10)          # Make a random linked list that is 3 nodes long
print(llA)                      # Returns: 10 -> 0 -> 4
print(llB)                      # Returns: 0 -> 9 -> 0
print(intersection(llA, llB))   # Returns: False because the lists do not intersect