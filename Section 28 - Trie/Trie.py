'''
Trie - A tree-based data structure that organizes information in a hierarchy.

Properties:
    *Typically used to store or search strings in a space & time efficient way
    *Any node in trie can store non repetitive multiple characters
    *Every node stores a link of the next character of the string
    *Every node keeps track of the 'end of string'



'''

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insertString(self, word):
        '''Takes a word and inserts it into a Trie Tree.'''
        current = self.root 
        for i in word:                                      # Loop through each character to see if it exists within the Trie Tree
            character = i                                       
            node = current.children.get(character)              # Get the node at which the character exists
            if node == None:                                        # If the node doesn't exist
                node = TrieNode()                                   # create one
                current.children.update({character:node})           # and make it a child of the current node
            current = node                                      # Iterate to the new node just created
        current.endOfString = True                          # When we exit the loop, we declare our last node as the end of the string
        print("Succesfully inserted")

    def searchString(self, word):
        '''Searches for a word in a Trie Tree'''
        currentNode = self.root                             # Start at the root
        for i in word:                                      # Loop through each character to see if it exists within the Trie Tree
            node = currentNode.children.get(i)
            if node == None:                                    # If the node doesn't exist, exit and stop looking
                return False
            currentNode = node                                  # Move to the next node

        if currentNode.endOfString == True:
            return True
        else:                                               # This handles cases where we may have the word appear inside of a bigger word but is technically not in the Trie
            return False                                    # Example: "Pizza" is in a Trie Tree.  But "Pi" is not in the Trie Tree.  

    def deleteString(self, root, word, index):
        '''Deletes a word from a Trie Tree given the root and index of the tree.'''
        if len(word) <= index:                              
            return True
        
        character = word[index]                             # Retrieve the character we want to delete
        currentNode = root.children.get(character)          # Retrieve the current node
        canThisNodeBeDeleted = False
        
        # Case 1 - Some of the string we want to delete is used as a prefix for another string
        if len(currentNode.children) > 1:                       # If there is more than one child, we cannot delete the character because it is used by another string
            self.deleteString(currentNode, word, index +1)      # Add +1 to the index to go to the next character
            return False                                        # Return False so that the character isn't deleted

        # Case 2 - The entire or part of the string we want to delete is a prefix of another string
        if index == len(word) -1:                               # If we are at the last node of the string that we want to delete (-1 because index starts at 0):
            if len(currentNode.children) >= 1:                      # If this node has one or more children, we don't delete the node because the string is a prefix of another string
                currentNode.endOfString = False                         # And we declare that node as not being end of string
                return False                                            # Return False so that the character isn't deleted
            else:                                                   # If this node has no children
                root.children.pop(character)                            # We can delete this node
                return True                                             # Return True so that the character is deleted
            
        # Case 3 - Another string is a prefix of the string we want to delete
        if currentNode.endOfString == True:                     # If we get to a node where endOfString = True, another string is a prefix of the string we want to delete
            self.deleteString(currentNode, word, index +1)          # Call the method on itself recursively
            return False                                            # Return False so that the character isn't deleted
        
        # Case 4 - No node depends on the string we want to delete 
        canThisNodeBeDeleted = self.deleteString(currentNode, word, index +1)   # Call the method on itself. 
        if canThisNodeBeDeleted == True:                                            # If True is returned:
            root.children.pop(character)                                                # Remove the character
            return True
        else:                                                                       # If False is returned:
            return False                                                                # Do not remove the character because some other string is dependent on the node
        


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
print(newTrie.searchString("App"))  # Returns True
print(newTrie.searchString("Pizza"))  # Returns False


newTrie.deleteString(newTrie.root, "App", 0)
print(newTrie.searchString("App"))      # Returns False

