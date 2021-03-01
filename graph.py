"""
Create a class named Graph which contains all the methods of an Undirected Graph
i.e: add_edge, remove_edge, no_of_nodes, no_of_edges, get_adj_list, get_adj_matrix, get_adj_list

Example: 
g = Graph() #  initialization
g.add_edge(1,2)
g.add_edge(2,3)

Note: Graph must not contain missing nodes and graph can be Directed
Directed graph technique can also be implemented with small change in logic

Bonus task: Create a class graph which handles Undirected or Directed, 
also with starting nodes can be any number/string and should handle missing nodes inbetween

Important tips/Clue for Bonus task: Nodes can have 0 or 1 as starting node and missing nodes
To tackle create a unique list of node names into a list and 
and we can use number of nodes as the shape/dimension of the adjacency matrix 
(i.e. if no_of_nodes is 3, then adj_matrix is 3x3 matrix)
only while displaying nodes we can use original node list to display their real node names

Example for above:
g = Graph()
g.add_edge(4,5)
g.add_edge(6,4)
g.add_edge(7,4)

# 4,5,6,7 are real node names
# real node names are configured like: 4,5,6,7 to 1,2,3,4
# node 4 will be 1 and node 5 will be 2 and so on.

"""

# Numpy for handing adjacency matrix/array
# List of Lists can be used as an alternative for numpy
import numpy as np

class Graph:
    def __init__(self, graph_type='U'):
        self.graph_type = graph_type
        self.edge_list = []
        # self.adjacency_list = {}
        self.number_of_edges = 0

    def __repr__(self):
        return f"Graph(graph_type='{self.graph_type}')"
    
    
    def edges(self):
        return len(self.edge_list)
    
    
    def nodes(self):
        self.no_of_nodes = len(self.get_adj_list())
        return self.no_of_nodes
    
    
    def add_edge(self, edge_i, edge_j):
        self.number_of_edges += 1
        if (edge_i, edge_j) not in self.edge_list:
            self.edge_list.append((edge_i, edge_j))
    
    
    def remove_edge(self, edge_i, edge_j):
        self.number_of_edges -= 1
        if (edge_i, edge_j) in self.edge_list:
            self.edge_list.remove((edge_i, edge_j))
        else:
            return f"{(edge_i, edge_j)} Not in edge list !"
    
    
    def get_edge_list(self):
        return self.edge_list
    
    
    def get_adj_matrix(self):
        
        self.no_of_nodes = len(self.get_adj_list())
        self.adjacency_matrix = np.zeros((self.no_of_nodes, self.no_of_nodes))
    
        for i in self.edge_list:
            self.adjacency_matrix[i[0]-1][i[1]-1] = 1
            if self.graph_type == 'U':
                self.adjacency_matrix[i[1]-1][i[0]-1] = 1
                
        return self.adjacency_matrix
    
    
    def get_adj_list(self):
        self.adjacency_list = {}
        for i in self.edge_list:
            self.adjacency_list.setdefault(i[0],[])
            self.adjacency_list[i[0]].append(i[1])
            if self.graph_type == 'U': 
                self.adjacency_list.setdefault(i[1],[])
                self.adjacency_list[i[1]].append(i[0])
        
        return self.adjacency_list
    