'''
Topological Sort Algorithm - Is an algorithm that takes a directed acyclic 
graph and returns the sequence of nodes where every node will appear before 
other nodes that it points to.

'''

from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        '''numberOfVertices is the number of nodes you want to initiate a graph data structure with'''
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices

    
    def print_graph(self):
        '''Prints the adjacency list of the graph.'''
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])

    def addEdge(self, vertex, edge):
        '''Adds an  edge between given vertices, vertex and edge.'''
        self.graph[vertex].append(edge)

    def topologicalSortHelper(self, vertex, visited, stack):
        '''
        A helper function for topologicalSort().  
        A recurive function that takes a vertex, visted, and stack.
        '''
        visited.append(vertex)                                      # Append the vertex to the visited list
        for i in self.graph[vertex]:                                # For each element of self.graph[key]
            if i not in visited:                                        # If that element hasn't been visited, 
                self.topologicalSortHelper(i, visited, stack)               # Call the function recursively on that element
        stack.insert(0, vertex)                                          # .insert(0, element) pushes the element to the left or bottom of the stack
        # The most bottom vertices of the graph appear to the left of the stack

    def topologicalSort(self):
        '''Returns the sequence of nodes where every node will appear before other nodes that it points to.'''
        visited = []
        stack = []
        for key in list(self.graph):                                # For each key in the adjacency list:
            if key not in visited:                                      # If the key has not been visited
                self.topologicalSortHelper(key, visited, stack)             # Call topologicalSortHelper()
        print(stack)



customGraph = Graph(8)          # Graph the flows downward:
customGraph.addEdge("A", "C")   # 
customGraph.addEdge("C", "E")   #   A   B
customGraph.addEdge("E", "H")   #    \ / \
customGraph.addEdge("E", "F")   #     C   D
customGraph.addEdge("F", "G")   #    /   /
customGraph.addEdge("B", "D")   #   E   /
customGraph.addEdge("B", "C")   #  / \ /
customGraph.addEdge("D", "F")   # H   F---G
customGraph.print_graph()   
# A : ['C']
# C : ['E']
# E : ['H', 'F']
# F : ['G']
# B : ['D', 'C']
# D : ['F']
customGraph.topologicalSort()   # Returns: ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']