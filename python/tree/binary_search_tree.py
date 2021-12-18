from tree.binary_tree import BinaryTree
from tree.binary_tree import Node

class BinarySearchTree(BinaryTree):

    def add(self,value):
        def __init__(self):
            self.root = None

        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        def place_in_tree(root, node):
            if not root:
                return

            if node.value < root.value:
                if root.left:
                    place_in_tree(root.left,node)
                else:
                    root.left = node

            else:
                if root.right:
                    place_in_tree(root.right,node)
                else:
                    root.right = node

        place_in_tree(self.root, new_node)

    def contains(self,value):
        if not self.root:
            return "List is empty"

        def move_trough_tree(root,value):
            if root.value == value:
               return True

            if value < root.value:
                if root.left:
                    return move_trough_tree(root.left, value)
                else:
                    return False

            else:
                if root.right:
                    return move_trough_tree(root.right, value)
                else:
                    return False


        return move_trough_tree(self.root, value)
