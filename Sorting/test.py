#Design Directed Graph class with minimum of 6 edges.
#  Write function to retrieve minimum and maximum cost edges from constructed graph. 
# While returning min/max cost, provided the edge names also. ####sublime,jupyter

import sys

class Graph:
    class Vertex:
        def __init__(self, id):
            self.id = id
            self.adjacency = {}

        def is_neighbor(self, id):
            return id in self.adjacency

        def add_neighbor(self, id, wt):
            if not self.is_neighbor(id):
                self.adjacency[id] = wt

        def list_neighbors(self):
            return list(self.adjacency.keys())

        def edge_cost(self, id):
            return self.adjacency.get(id, sys.maxsize)

    def __init__(self):
        self.vertex_count = 0
        self.adjacency_list = {}

    def vertex_count(self):
        return len(self.adjacency_list)

    def add_node(self, id):
        if id not in self.adjacency_list:
            new_vertex = self.Vertex(id)
            self.adjacency_list[id] = new_vertex
            self.vertex_count += 1

    def add_directed_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.adjacency_list:
            self.add_node(from_vertex)
        if to_vertex not in self.adjacency_list:
            self.add_node(to_vertex)
        self.adjacency_list[from_vertex].add_neighbor(to_vertex, weight)

    def get_min_max_edges(self):
        min_edge = (None, None, 99999999)
        max_edge = (None, None, -9999999)

        for from_vertex in self.adjacency_list:
            neighbors = self.adjacency_list[from_vertex].adjacency
            for to_vertex, weight in neighbors.items():
                if weight < min_edge[2]:
                    min_edge = (from_vertex, to_vertex, weight)
                if weight > max_edge[2]:
                    max_edge = (from_vertex, to_vertex, weight)

        return min_edge, max_edge

g = Graph()

g.add_directed_edge('A', 'B', 5)
g.add_directed_edge('B', 'C', 3)
g.add_directed_edge('C', 'D', 7)
g.add_directed_edge('D', 'A', 2)
g.add_directed_edge('B', 'E', 9)
g.add_directed_edge('E', 'F', 4)
g.add_directed_edge('F', 'C', 6)

min_edge, max_edge = g.get_min_max_edges()
print("Minimum cost edge:", min_edge)  
print("Maximum cost edge:", max_edge)