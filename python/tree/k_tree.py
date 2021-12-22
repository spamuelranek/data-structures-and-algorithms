from code_challenges.stack_and_queue.queue import Queue

class NodeKtree:
    def __init__(self,value):
        self.value = value
        self.children = []

class Ktree:
    def __init__(self,k):
        self.root = None
        self.k = k

    def add_node(self,value):
        new_node = NodeKtree(value)
        if self.root is None:
            self.root = new_node
            return

        q = Queue()
        q.enq(self.root)

        while q.is_empty() is False:
            dequeue = q.deq()
            if len(dequeue.children) < self.k:
                dequeue.children.append(new_node)
                return
            else:
                for child in dequeue.children:
                    q.enq(child)

        return

    def breadth_first(self):
        if self.root is None:
            return "Tree is empty"

        first_into_queue = self.root
        q = Queue()
        q.enq(self.root)

        return_list = []


        while q.is_empty() is False:

            dequeue = q.deq()
            return_list.append(dequeue.value)


            for child in dequeue.children:
                q.enq(child)

        return return_list
