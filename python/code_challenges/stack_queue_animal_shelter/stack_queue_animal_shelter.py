from code_challenges.stack_and_queue.stack import Stack

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Kiwi:
    pass

class Dog:
    def __init__(self, name):
        self.name = name


class Cat:
    def __init__(self, name):
        self.name = name

class Stopper:
    pass



class AnimalShelter:

    def __init__(self) -> None:
        self._enqueue_stack = Stack()
        self._dequeue_stack = Stack()

    def enqueue(self,animal):

        if isinstance(animal,Dog) or isinstance(animal,Cat):
            self._enqueue_stack.push(animal)
            return

        raise ValueError("Only Dogs and Cats are allowed into this animal shelter")

    def _invert_enqueue_stack_to_dequeue_stack(self):
         while not self._enqueue_stack.is_empty():
            self._dequeue_stack.push(self._enqueue_stack.pop())

    def _invert_dequeue_stack_to_enqueue_stack(self):
         while not self._dequeue_stack.is_empty():
            self._enqueue_stack.push(self._dequeue_stack.pop())


    def dequeue(self, pref = None):
        if self._enqueue_stack.is_empty():
            raise IndexError("This shelter is empty")

        self._invert_enqueue_stack_to_dequeue_stack()

        return_value = ""

        while not self._dequeue_stack.is_empty():
            transfer_value = self._dequeue_stack.pop()
            if pref is None:
                return_value = transfer_value
                break
            if pref == "dog" and isinstance(transfer_value, Dog):
                return_value = transfer_value
                break
            if pref == "cat" and isinstance(transfer_value, Cat):
                return_value = transfer_value
                break

            self._enqueue_stack.push(transfer_value)

        self._invert_dequeue_stack_to_enqueue_stack()

        if return_value:
            return return_value

        return f"There are no {pref}s in the shelter at the time"



if __name__ == "__main__":
    marco = AnimalShelter()
    polo = Cat("Ruby")
    marco.enqueue(polo)
    print(marco._enqueue_stack.peek().name)

