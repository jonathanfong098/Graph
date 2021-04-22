"""
    Lab Assignment 8
    11/23/20
    Assignment 8: Setups Node, Linked List, and Vertex Class.
"""
from node import Node
from linked_list import LinkedList


class Vertex:
    """
    This class creates a vertex class.

    Attributes:
        id : identifier for vertex
        connected to (LinkedList) = linked list of vertices the current vertex is connect to  
    """
    def __init__(self, key):
        """
        The constructor for the Vertex class.

        Parameter:
            key : identifier for vertex
        """
        self._id = key
        self._connected_to = LinkedList()

    def add_neighbor(self, neighbor, weight=None):
        """
        This function adds neighbor vertices to the current vertex.

        Parameters:
            neighbor (Node) : neighbor vertices
            weight : weight of current vertex
        """
        neighbor = Node(neighbor, weight)
        self._connected_to.add(neighbor)

    def __str__(self):
        description_of_vertex = f'Vertex id: {self.get_id()}\n' \
                                f'Connected to : {self.get_connections()}'
        return description_of_vertex

    def get_connections(self):
        """
        This functions gets the vertices connected to the current vertex.

        Return:
            connections (Dictionary) : dictionary of vertices connected to the current vertex
        """
        connections = {}

        current_node = self._connected_to.head

        while current_node is not None:
            connections[current_node.id._id] = current_node.weight
            if current_node.next is not None:
                current_node = current_node.next
            else:
                current_node = None

        return connections

    def if_visited(self, weight=None):
        current_node = self._connected_to.head

        while current_node is not None:
            current_node.id.add_neighbor(self, weight)
            if current_node.next is not None:
                current_node = current_node.next
            else:
                current_node = None

    def get_id(self):
        """
        This function returns the id of the vertex.

        Return:
            id : identifier for vertex
        """
        return self._id

    def set_id(self, key):
        """
        This function changes the id of the vertex

        Parameter:
            key : identifier for vertex
        """
        self._id = key
