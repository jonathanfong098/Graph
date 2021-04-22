"""
    Lab Assignment 8
    11/23/20
    Assignment 9: Test Class
"""
from vertex import Vertex


class Graph:
    """
        This class creates a graph data structure.

        Attributes:
            vertices (Dictionary) : dictionary of vertices in the graph
    """
    def __init__(self):
        """
        The constructor for the Graph class.
        """
        self._vertices = {}

    def add_vertex(self, key):
        """
        This function adds a vertex to the graph

        Parameters:
            key : data
        """
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex

    def add_edge(self, f, t, weight=None):
        """
        This function adds a edge between two vertices in the graph.

        Parameters:
             f (Vertex) : vertex to connect edge from
             t (Vertex) : vertex to connect edge to
             weight : weight of an edge
        """
        if f not in self.vertices:
            self.add_vertex(f)
        if t not in self.vertices:
            self.add_vertex(t)
        self.vertices[f].add_neighbor(self.vertices[t], weight)

    def all_edges(self):
        """
        This function returns a dictionary listing each vertex in the graph, each vertex's neighbor, and the weight
        between a vertex and its neighbor.

        Return:
            edges (Dictionary) : a dictionary listing each vertex in the graph, each vertex's neighbor and the weight
            between a vertex and its neighbor Vertex{Neighbor Vertex:Weight of Connection between Vertex and Neighbor Vertex}
        """
        edges = {}
        vertices = self.vertices.values()
        for vertex in vertices:
            edges[vertex.get_id()] = vertex.get_connections()
        return edges

    @property
    def vertices(self):
        """
        This function returns the vertices in the graph.

        Return:
            vertices (Dictionary) : dictionary of vertices in the graph
        """
        return self._vertices

