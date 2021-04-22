class Node:
    """
    This class creates a node class.

    Attributes:
        id (Node) : identification for node
        weight : weight of node
        next (Node): next Node
    """
    def __init__(self, key, weight=None):
        """
        The constructor for the Node class

        id (Node) : identification for node
        weight : weight of node
        next (Node) : next Node
        """
        self._id = key
        self._weight = weight
        self._next = None

    @property
    def id(self):
        """
        This function returns the id of the node.

        Return:
            id : identifier for node
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        This function changes the id of the node.

        Parameter:
            id : new id
        """
        self._id = id

    @property
    def weight(self):
        """
        This function returns the weight of the node.

        Return:
            weight : weight of the node
        """
        return self._weight

    @weight.setter
    def weight(self, new_weight):
        """
        This function changes the weight of the node.

        Parameter:
            new weight : new weight of th enode
        """
        self._id = new_weight

    @property
    def next(self):
        """
        This function returns the next node.

        Return:
            next (Node) : next node
        """
        return self._next

    @next.setter
    def next(self, new_next):
        """
        This function changes the next node.

        Parameter:
            new next (Node) : new next node
        """
        self._next = new_next
