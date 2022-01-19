from logging import raiseExceptions


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
