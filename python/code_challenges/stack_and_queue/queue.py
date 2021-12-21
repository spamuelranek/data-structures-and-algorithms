from code_challenges.stack_and_queue.node import Node
class Queue:

    def __init__(self) -> None:
        self.front = None
        self.rear = None


    def is_empty(self):
        if not self.front:
            return True
        return False

    def peek(self):
        if not self.front:
            raise ValueError("There is nothing in this list")
        return self.front.value

    def deq(self):
        if not self.front:
            raise ValueError("There is nothing in this list")
        temp_front = self.front
        self.front = temp_front.next
        temp_front.next = None
        return temp_front.value

    def enq(self,value):
        new_node = Node(value)
        if not self.front:
            self.rear = new_node
            self.front = new_node
            return
        self.rear.next = new_node
        self.rear = new_node


