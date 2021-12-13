from code_challenges.stack_and_queue.stack import Stack

class PseudoQueue:

    def __init__(self) -> None:
        self.enque_stack = Stack()
        self.deque_stack = Stack()

    def enqueue(self,value):
        self.enque_stack.push(value)

    def dequeue(self):
        if self.enque_stack.is_empty():
            raise IndexError("This queue is empty")

        while not self.enque_stack.is_empty():
            self.deque_stack.push(self.enque_stack.pop())

        return_value = self.deque_stack.pop()

        while not self.deque_stack.is_empty():
            self.enque_stack.push(self.deque_stack.pop())

        return return_value


