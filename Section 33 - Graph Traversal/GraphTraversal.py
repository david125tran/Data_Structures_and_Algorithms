'''
Breadth First Search (BFS) - Is used to search a graph data structure for a 
node that meets a set of criteria. It starts at the root of the graph and 
visits all nodes at the current depth level before moving on to the nodes at
the next depth level.  It goes in breadth first.  Uses a queue.  

Depth First Search (DFS) - Is used to search a graph data structure where we 
traverse downwards through linked nodes until we reach the end, then retrace
our steps to check which nodes we haven't visted and repeat the process.  It 
goes in depth first.  Uses a stack.

A : ['B', 'C']          BFS: 'A' -> 'B' -> 'C' -> 'E' -> 'D'
B : ['A', 'E']
C : ['A', 'D']          DFS: 'A' -> 'C' -> 'D' -> 'E' -> 'B'
D : ['C', 'E']
E : ['B', 'D']

A------B
|        \
|         E
|        /
C------D


Which search to use?
*BFS - When we know the target is close to the starting point
*DFS - When we know the target is close to the end point

BFS and DFS have the same time and space complexity.  
'''
from collections import deque

class Graph:
    '''Creates an unweighted & undirected graph.'''
    def __init__(self):
        self.adjacency_list = {}            

    def add_vertex(self, vertex):
        '''Takes a vertex and adds it to the graph'''
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        '''Prints the adjacency list of the graph.'''
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):
        '''Adds an unweighted and undirected edge between given vertices, vertex1 and vertex2.'''
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():     # If both vertexs exists:
            self.adjacency_list[vertex1].append(vertex2)        # Reference vertex2 in vertex1's adjacency list
            self.adjacency_list[vertex2].append(vertex1)        # Reference vertex1 in vertex2's adjacency list
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        '''Removes an edge between given vertices, vertex1 and vertex2.'''
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:                                                # Try to remove an edge
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:                                  # Raise an exception if the edge was never formed
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        '''Removes a vertex from a graph and deletes it from any adjacency list that the vertex may be in.'''
        if vertex in self.adjacency_list.keys():                    # If the vertex exists
            for other_vertex in self.adjacency_list[vertex]:            # For each adjacency list it may be referenced in
                self.adjacency_list[other_vertex].remove(vertex)            # Remove that vertex from that adjacency list
            del self.adjacency_list[vertex]                             # Delete the actual vertex
            return True
        return False
    
    def breadthFirstSearch(self, vertex):
        '''
        Used to search a graph data structure starting at the root.  
        It visits all nodes at the current depth before moving onto the nodes at the next depth level.
        '''
        visited = set()                     # Holds vertexs that have been visited.  We use set() instead of list because it has faster performance
        visited.add(vertex)                 # Add vertex to the visited set since it will get visited 1st
        queue = deque([vertex])             # Add the vertex to a queue using collections import and double ended queue to reduce time complexity
        print(vertex)
        while queue:                        # While queue is not empty:
            current_vertex = queue.popleft()                                # .popleft() removes the first in vertex from the queue (FIFO style)
            for adjacent_vertex in self.adjacency_list[current_vertex]:     # Start iterating through each of current_vertex's adjacent vertexs
                if adjacent_vertex not in visited:                              # If the current vertex's adjacent vertex hasn't been visited yet
                    visited.add(adjacent_vertex)                                    # Add the vertex to the visited set()
                    queue.append(adjacent_vertex)                                   # And add it to the queue
                    print(adjacent_vertex)                                          # Print the vertex as it is visted because set() won't keep added elements in order

    def depthFirstSearch(self, vertex):
        '''
        Used to search a graph data structure starting at the root.  
        Traverse downwards through linked nodes until the end is reached, 
        then retraces to check which nodes we haven't been visted and 
        repeats the process. 
        '''
        visited = set()                                                     # Holds vertexs that have been visited.  We use set() instead of list because it has faster performance
        stack = [vertex]                                                    # Add the vertex to a list instead of a queue since we want to elements in the stack as LIFO
        while stack: 
            current_vertex = stack.pop()                                        # .pop() removes the last vertex in the stack (LIFO style)
            if current_vertex not in visited:                                   # If the current vertex hasn't been visited yet:
                print(current_vertex)                                               # Print the vertex as it is visted because set() won't keep added elements in order   
                visited.add(current_vertex)                                         # Add the vertex to the visited set()                   
            for adjacent_vertex in self.adjacency_list[current_vertex]:         # Start iterating through each of current_vertex's adjacent vertexs
                if adjacent_vertex not in visited:                                  # If the current vertex's adjacent vertex hasn't been visited yet
                    stack.append(adjacent_vertex)                                   # Append it to the waiting list to be visited.  Eventually the last in element will be the 1st out element



graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_edge("A", "B")        #       A------B
graph.add_edge("A", "C")        #       |        \
graph.add_edge("B", "E")        #       |         E
graph.add_edge("C", "D")        #       |        /
graph.add_edge("D", "E")        #       C------D
graph.print_graph()
# A : ['B', 'C']
# B : ['A', 'E']
# C : ['A', 'D']
# D : ['C', 'E']
# E : ['B', 'D']
graph.breadthFirstSearch("A")   # Returns: A B C E D
graph.depthFirstSearch("A")     # Returns: A C D E B