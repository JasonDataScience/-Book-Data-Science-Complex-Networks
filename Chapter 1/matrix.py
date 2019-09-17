# Chapter 1.1 foodweb, an undirected graph
# implementation of an undirected graph using Adjacency Matrix, with weighted or unweighted edges
# learned from here, code reference to https://gist.github.com/anirudhjayaraman
# refactored by Jin Hyung Park

import numpy as np

class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.peers = []
    
    def add_peer(self, peer):
        if isinstance(peer, Vertex): #if peer itself is also vertex
            if peer.name not in self.peers: #if peer is not registered on self.peers' list
                self.peers.append(peer.name) #append the missing peer's name first
                peer.peers.append(self.name) #that peer's peers should append all the name.. recursive
                self.peers = sorted(self.peers) #sorted the self.peers list
                peer.peers = sorted(peer.peers) #sorted the peer.peers list
            return True
        else:
            return False
    
    def add_peers(self, peers):
        for peer in peers:
            if isinstance(peer, Vertex):
                if peer.name not in self.peers:
                    self.peers.append(peer.name)
                    peer.peers.append(self.name)
                    self.peers = sorted(self.peers)
                    peer.peers = sorted(peer.peers)
                return True
            else:
                return False
    
    def __str__(self):
        return str(self.peers)

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex):
            self.vertices[vertex.name] = vertex.peers #list in each element of dictionary

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.name] = vertex.peers #put vertex.name into self.vertices as key(dictionary), and put vertex.peers as values

    def add_edge(self, vertexfrom, vertexto):
        if isinstance(vertexfrom, Vertex) and isinstance(vertexto, Vertex):
            vertexfrom.add_peer(vertexto)
            if isinstance(vertexfrom, Vertex) and isinstance(vertexto, Vertex):
                self.vertices[vertexfrom.name] = vertexfrom.peers
                self.vertices[vertexto.name] = vertexto.peers
    
    def add_edges(self, edges):
        for edge in edges:
            self.add_edge(edge[0],edge[1]) #edge[0] is vertexfrom, edge[1] is vertexto
    
    def adjacencyList(self):
        if len(self.vertices) >= 1:
            return [str(key) + ":" + str(self.vertices[key]) for key in self.vertices.keys()]

    def adjacencyMatrix(self):
        if len(self.vertices) >= 1:
            self.vertex_names = sorted(g.vertices.keys())
            self.vertex_indices = dict(zip(self.vertex_names, range(len(self.vertex.names))))
            self.adjacency_matrix = np.zeros(shape=(len(self.vertices), len(self.vertices)))

            for i in range(len(self.vertex_names)):
                for j in range(i,len(self.vertices)):
                    for k in g.vertices[self.vertex_names[i]]: #converting into the index of g.vertices
                        j = g.vertex_indices[k]
                        self.adjacency_matrix[i,j] = 1
        return self.adjacency_matrix
    
def graph(g):
    return str(g.adjacencyList()) + str(g.adjacencyMatrix())

#####################

a = Vertex('A')
b = Vertex('B')
c = Vertex('C')
d = Vertex('D')

a.add_peers([b,c,d])
b.add_peers([a,c])
c.add_peers([a,b,d])
d.add_peers([a,c])

g = Graph()
g.add_vertices([a,b,c,d])
print(graph(g))