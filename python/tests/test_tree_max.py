from tree.binary_tree import BinaryTree
from tree.binary_tree import Node

def test_is_binary_tree():
    tree = BinaryTree()
    assert tree

def test_is_binary_tree_max_empty():
    tree = BinaryTree()
    actual = tree.pre_order_max_finder()
    expected = "Tree is empty"
    assert actual == expected

def test_node_in_binary_tree_pre_order_max():
    ten = Node(10)
    five = Node(5)
    fifteen = Node(15)
    ten.left = five
    ten.right = fifteen
    tree = BinaryTree(ten)
    actual = tree.pre_order_max_finder()
    expected = 15
    assert actual == expected

def test_node_in_binary_tree_pre_xx_order_max():
    ten = Node(10)
    five = Node(5)
    fifteen = Node(15)
    eleven = Node(11)
    twenty_five = Node(25)
    fifteen.right = eleven
    fifteen.left = twenty_five
    ten.left = five
    ten.right = fifteen
    tree = BinaryTree(ten)
    actual = tree.pre_order_max_finder()
    expected = 25
    assert actual == expected
