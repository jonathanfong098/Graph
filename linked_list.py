class LinkedList:
    """
    This class creates a linked list class.

    Attributes:
        head (Node) : head of linked list
    """
    def __init__(self):
        """
        The constructor for the LinkedList class

        head (Node) : head of linked list
        """
        self._head = None

    def add(self, item):
        """
        This function adds a node containing the specifieed item to the linked list.

        Parameter:
            item : item to add to linked list
        """
        if self.is_empty():
            self.head = item
        else:
            # new_head_node = Node(item)
            new_head_node = item
            new_head_node.next = self._head
            self._head = new_head_node

    def remove(self, item):
        """
        This function adds removes the node containing the specified item to the linked list.

        Parameter:
            item : item to remove from linked list
        """
        if self.is_empty():
            raise ValueError('Linked list is empty')

        if self.head == item:
            self.head = self.head.next

        current_node = self.head
        while current_node is not None:
            current_node = current_node.next
            if current_node.next.id == item:
                current_node.next = current_node.next.next
                break

    def is_empty(self):
        """
        This function determines if the linked list is empty.

        Returns:
            true (Boolean) : true if linked list is empty
            false (Boolean) : false if linked list is not empty
        """
        if self._head is None:
            return True
        else:
            return False

    @property
    def head(self):
        """
        This function returns the head of the linked list.

        Return:
            head (Node) : head of linked list
        """
        return self._head

    @head.setter
    def head(self, new_head):
        """
        This function changes the head  of the linked list.

        Parameter:
            new head (Node) : new head of linked list
        """
        self._head = new_head
