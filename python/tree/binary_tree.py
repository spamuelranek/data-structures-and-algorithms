class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self, root = None):
        self.root = root

    def pre_order(self):
        pre_order_list = []

        def move_in_list(root):
            if not root:
                return
            pre_order_list.append(root.value)
            move_in_list(root.left)
            move_in_list(root.right)


        move_in_list(self.root)

        return pre_order_list

    def in_order(self):
        in_order_list = []

        def move_in_list(root):
            if not root:
                return
            move_in_list(root.left)
            in_order_list.append(root.value)
            move_in_list(root.right)


        move_in_list(self.root)

        return in_order_list

    def post_order(self):
        post_order_list = []

        def move_in_list(root):
            if not root:
                return
            move_in_list(root.left)
            move_in_list(root.right)
            post_order_list.append(root.value)


        move_in_list(self.root)

        return post_order_list

    def pre_order_max_finder(self):
        if not self.root:
            return "Tree is empty"

        def move_in_list(root, pre_order_max = 0):
            if not root:
                return
            if root.value > pre_order_max:
                pre_order_max = root.value

            left = move_in_list(root.left, pre_order_max)
            right = move_in_list(root.right, pre_order_max)
            if left and left > pre_order_max:
                pre_order_max = left

            if right and right> pre_order_max:
                pre_order_max = right


            return pre_order_max

        return move_in_list(self.root)

    # def add_node(self, value):
    #     # we want to add a node to the next available position
    #     # also want to fill the level before moving to the next
    #     # want to build a balancing tree
    #     new_node = Node(value)
    #     if not self.root:
    #         self.root = new_node
    #         return

    #     def find_empty_location(root,node):

    #         if root.left:
    #             if root.right:
    #                 return find_empty_location(root.left,node)
    #             else:
    #                 root.right = node

    #         else:
    #             root.left = node




