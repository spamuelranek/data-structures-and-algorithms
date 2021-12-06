from typing import Counter


class Node:
    def __init__(self,value,next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        return None



    def append(self, value):
        if self.head is None:
            self.insert(value)
            return None

        current = self.head

        while current:
            if current.next is None:
                new_node = Node(value)
                current.next = new_node
                return None
            current = current.next

    def insert_before(self,value,value_to_add_before):
        if self.head is None:
            return "This list is empty"
        if self.head.value == value_to_add_before:
            self.insert(value)
            return None

        current = self.head

        while current.next:
            if current.next.value:
                if current.next.value == value_to_add_before:
                    new_node = Node(value)
                    new_node.next = current.next
                    current.next = new_node
                    return None
            current = current.next

        return "That value is not in this list"

    def insert_after(self, value, value_to_add_after):
        if self.head is None:
            return "This list is empty"
        current = self.head

        while current:
            if current.value == value_to_add_after:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                return None
            current = current.next

        return "That value is not in this list"

    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):

        current = self.head

        output = ""
        while current:
            output += "{" + str(current.value) + "} -> "
            current = current.next
        output = output + "NULL"
        return output



