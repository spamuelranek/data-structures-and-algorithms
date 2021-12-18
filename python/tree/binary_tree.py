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




