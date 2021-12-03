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


    def includes(self, value):

        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def __str__(self):

        current = self.head

        str_format = "{} -> "
        output = ""
        while current:
            output += str_format.format(current.value)
            current = current.next
        output = output + "NULL"
        return output



