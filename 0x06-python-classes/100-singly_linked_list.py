#!/usr/bin/python3
"""Module implements concept of singly linked list
"""


class Node:
    """Class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Method to initialize the Node object

        Args:
            data (int): integer value stored in node
            next_node (Node): next node on the list

        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Method to return the data value"""

        return self.__data

    @property
    def next_node(self):
        """Method to return the next node"""

        return self.__next_node

    @data.setter
    def data(self, value):
        """Method to set the data attribute"""

        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Method to set the next_node attribute"""

        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """Method to initialize a SinglyLinkedList object"""

        self.__head = None

    def __str__(self):
        """Method to display the values stored in a SinglyLinkedList object"""

        node = self.__head
        value = ""
        while node is not None:
            value += f"{node.data}"
            node = node.next_node
            if node:
                value += "\n"
        return value

    def sorted_insert(self, value):
        """Method that inserts a new Node object into the correct sorted
        position in the list"""

        prev = None
        curr = self.__head
        while curr is not None and value > curr.data:
            prev = curr
            curr = curr.next_node

        new = Node(value, curr)
        if prev is not None:
            prev.next_node = new
        else:
            self.__head = new
