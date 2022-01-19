
from code_challenges.stack_and_queue.queue import Queue


class Vertex:
    def __init__(self, value) -> None:
        self.value = value
        self.neighbors = []

class Graph:
    def __init__(self) -> None:
        self.nodes = []

    def add_node(self,value):
        new_node = Vertex(value)
        self.nodes.append(new_node)
        return new_node

    def add_edge(self,node_one,node_two,weight=0):
        if node_one in self.nodes and node_two in self.nodes:
            node_one.neighbors.append((node_two,weight,))
            return
        else:
            raise KeyError


    def get_nodes(self):
        return self.nodes

    def get_neighbors(self,node):
        return node.neighbors

    def size(self):
        return len(self.nodes)

    def breadth_first(self,node):

        if node not in self.nodes:
            raise KeyError
        collection_output = []
        queue = Queue()
        visited_nodes = set()

        queue.enq(node)
        visited_nodes.add(node)

        while queue.is_empty() is not True:
            node_to_check = queue.deq()
            collection_output.append(node_to_check)
            for neighbors in node_to_check.neighbors:
                if neighbors[0] not in visited_nodes:
                    visited_nodes.add(neighbors[0])
                    queue.enq(neighbors[0])

        return collection_output
