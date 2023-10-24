#!/usr/bin/python3
"""Defines a Singly linked Data structure"""


class Node:
    """Represents the Node class"""
    def __init__(self, data, next_node=None):
        """Initialize the Node class

        Args:
            data (int): the element of the list
            next_node (Node): the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents the SinglyLinkedList class"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value)
        if not self.__head:
            new.next_node = None
            self.__head = new
        elif value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None
                    and current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        elements = []
        current = self.__head
        while current:
            elements.append(str(current.data))
            current = current.next_node
        return '\n'.join(elements)
