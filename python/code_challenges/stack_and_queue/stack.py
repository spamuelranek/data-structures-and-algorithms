from code_challenges.stack_and_queue.node import Node
class Stack:

    def __init__(self) -> None:
        self.top = None

    def is_empty(self):
        if not self.top:
            return True
        return False

    def push(self,value):
        self.top = Node(value,self.top)

    def peek(self):
        if not self.top:
            raise ValueError("This stack is empty")
        return self.top.value

    def pop(self):
        if not self.top:
            raise ValueError("This stack is empty")
        temp_top = self.top
        self.top = self.top.next
        temp_top.next = None
        return temp_top.value


