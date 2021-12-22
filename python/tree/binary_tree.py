class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class NodeTwo:
    def __init__(self,value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

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






