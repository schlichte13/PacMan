import pygame, sys, random, os
from pygame.locals import *
from collections import defaultdict



#class to build weighted graph from edges
class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
    
    def add_edge(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

tempPath = {}
graph = Graph()
path =[]


#edges to be used for the weighted graph. Weight represents distance from points
edges = [
    #e1
    ('n1', 'n2', 80),
    ('n2', 'n3', 120),
    ('n4', 'n5', 120),
    ('n5', 'n6', 80),
    ('n1', 'n7', 60),
    ('n2', 'n8', 60),
    ('n3', 'n10', 60),
    ('n4', 'n11', 60),
    ('n5', 'n13', 60),
    #e10
    ('n6', 'n14', 60),
    ('n7', 'n8', 80),
    ('n8', 'n9', 40),
    ('n9', 'n10', 80),
    ('n10', 'n11', 40),
    ('n11', 'n12', 80),
    ('n12', 'n13', 40),
    ('n13', 'n14', 80),
    ('n7', 'n15', 40),
    ('n8', 'n16', 40),
    #e20
    ('n9', 'n17', 40),
    ('n12', 'n20', 40),
    ('n13', 'n21', 40),
    ('n14', 'n22', 40),
    ('n15', 'n16', 80),
    ('n17', 'n18', 80),
    ('n19', 'n20', 80),
    ('n21', 'n22', 80),
    ('n16', 'n27', 80),
    ('n18', 'n24', 40),
    #e30
    ('n19', 'n25', 40),
    ('n21', 'n30', 80),
    ('n23', 'n28', 40),
    ('n23', 'n24', 80),
    ('n24', 'n25', 40),
    ('n25', 'n26', 80),
    ('n26', 'n29', 40),
    ('n27', 'n28', 40),
    ('n29', 'n30', 40),
    ('n27', 'n34', 100),
    #e40
    ('n28', 'n31', 60),
    ('n29', 'n32', 60),
    ('n30', 'n39', 100),
    ('n31', 'n32', 200),
    ('n31', 'n35', 40),
    ('n32', 'n38', 40),
    ('n33', 'n34', 80),
    ('n34', 'n35', 40),
    ('n35', 'n36', 80),
    ('n37', 'n38', 80),
    #e50
    ('n38', 'n39', 40),
    ('n39', 'n40', 80),
    ('n33', 'n41', 40),
    ('n34', 'n43', 40),
    ('n36', 'n63', 40),
    ('n37', 'n64', 40),
    ('n39', 'n46', 40),
    ('n40', 'n48', 40),
    ('n41', 'n42', 40),
    ('n43', 'n44', 40),
    #e60
    ('n44', 'n63', 80),
    ('n63', 'n64', 40),
    ('n64', 'n45', 80),
    ('n45', 'n55', 40),
    ('n45', 'n46', 40),
    ('n47', 'n48', 40),
    ('n42', 'n50', 40),
    ('n43', 'n51', 40),
    ('n44', 'n52', 40),
    ('n46', 'n56', 40),
    #e70
    ('n47', 'n57', 40),
    ('n49', 'n50', 40),
    ('n50', 'n51', 40),
    ('n52', 'n53', 80),
    ('n54', 'n55', 80),
    ('n56', 'n57', 40),
    ('n57', 'n58', 40),
    ('n59', 'n60', 200),
    ('n53', 'n60', 40),
    ('n60', 'n61', 40),
    #e80
    ('n54', 'n61', 40),
    ('n61', 'n62', 200),
    ('n49', 'n59', 40),
    ('n58', 'n62', 40),
    #gh
    ('n24', 'nb', 40),
    ('n25', 'ni', 40),
    ('nc', 'nb', 30),
    ('nb', 'ni', 40),
    ('ni', 'np', 30),
    
]

#adds edges to graph
for edge in edges:
    graph.add_edge(*edge)


#gets the shortest path between two points based on our graphs weighted edges
def dijsktra(graph, initial, end, path):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        #print(graph.edges[current_node])
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    #print(current_node)

    return path

dijsktra(graph, 'n13', 'n8', path)

print(path)

    
