'''
Graph - A non-linear data structure consisting of vertices & edges.  The vertices are 
sometimes also referred to as nodes and the edges are lines or arcs that connect any 
two nodes in the graph. More formally a Graph is composed of a set of vertices( V ) 
and a set of edges( E ). The graph is denoted by G(E, V).

*Weighted graph - A graph in which each branch is given a numerical weight associated
with its edges.
*Unweighted graph - A graph which doesn't have a weight associated with any edge.  The
edges are assumed to be the same length (or the length doesn't matter).
*Undirected graph - Have edges that don't have a direction.  (No arrows witih 
direction).
*Directed graph - Have edges that have a direction associated with them. (Arrows with
direction).
*Cyclic graph - A graph which has at least one loop.
*Acyclic graph - A graph with no loop.  
*Tree - Is a special case of directed acylic graph.  There is no loop and arrows flow 
in one direction.  
*Negative edge - An edge having a negative weight.
*Positive edge - An edge having a positive weight.

Graph
    *Directed
        *Weighted
            *Positive
            *Negative
        *Unweighted
    *Undirected
        *Weighted
            *Positive
            *Negative
        *Unweighted

A------D
| \      \
|   \      J
|     \  /
B      K
|    /
|  /
E

A, B, D, E, J, & K represent nodes/vertices.  And the lines represent the edges. 

*Adjacency matrix - A square matrix used to represent a finite graph. The elements of 
the matrix indicate whether pairs of vertices are adjacent or not in the graph. 
  
  A B C D E
A 0 1 1 1 0     A------B            The 0s represent no connection (edge).
B 1 0 0 0 1     |\       \          The 1s represent a connection (edge).
C 1 0 0 1 0     |  \      E
D 1 0 1 0 1     |    \   /
E 0 1 0 1 0     C------D

*Adjacency List -  A collection of unordered lists used to represent a finite graph

[A] -> B -> C -> D
[B] -> A -> E
[C] -> A -> D                       
[D] -> A -> C -> E
[E] -> B -> D

If a graph is complete or almost complete, we should use Adjacency Matrix
If there aren't many edges, then we should use Adjaceny List

'''
#---------Graph Implementation Using Dictionary Method 1---------
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

customDict1 = {"a": ["b", "c"],                 #   A
              "b": ["a", "d", "e"],             # /   \
              "c": ["a", "e"],                  # B   C
              "d": ["b", "e", "f"],             # | \ |
              "e": ["d", "c", "f"],             # D---E
              "f": ["d", "e"]                   # \   /
              }                                 #   F
graph1 = Graph(customDict1)
print(graph1.gdict)      # Returns: {'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['a', 'e'], 'd': ['b', 'e', 'f'], 'e': ['d', 'c', 'f'], 'f': ['d', 'e']}

customDict2 = {"a": ["b", "c"],                 
              "b": ["a", "d", "e"],             
              "c": ["a", "e"],                  
              "d": ["b", "e", "f"],             
              "e": ["d", "f"],            # Removed "c" and add it using the graph.addEdge() function      
              "f": ["d", "e"]                   
              }                                 
graph2 = Graph(customDict2)
graph2.addEdge("e", "c")
print(graph2.gdict)      # Returns: {'a': ['b', 'c'], 'b': ['a', 'd', 'e'], 'c': ['a', 'e'], 'd': ['b', 'e', 'f'], 'e': ['d', 'c', 'f'], 'f': ['d', 'e']}

#---------Graph Implementation Using Dictionary Method 2---------
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
    
print("")
graph3 = Graph()
graph3.add_vertex("A")
graph3.add_vertex("B")
graph3.add_edge("A", "B")
graph3.print_graph()        
# Returns:
# A : ['B']
# B : ['A']
print("")
graph3.add_vertex("C")
graph3.add_edge("A", "C")
graph3.add_edge("B", "C")
graph3.print_graph()   
# Returns:
# A : ['B', 'C']            #   A
# B : ['A', 'C']            #  / \
# C : ['A', 'B']            # B---C
print("")
graph3.remove_edge("A", "C")
graph3.print_graph()   
# Returns:
# A : ['B']                 #   A
# B : ['A', 'C']            #  / 
# C : ['A']                 # B---C
print("")
graph3.add_edge("A", "C")
graph3.print_graph()   
# Returns:
# A : ['B', 'C']            #   A
# B : ['A', 'C']            #  / \
# C : ['A', 'B']            # B---C
print("")
graph3.remove_vertex("C")
graph3.print_graph()  
# Returns:              #   A
# A : ['B']             #   |
# B : ['A']             #   B
