from tree.binary_tree import BinaryTree
from tree.binary_tree import Node

def test_is_binary_tree():
    tree = BinaryTree()
    assert tree

def test_binary_tree_root():
    first = Node("First")
    tree = BinaryTree(first)
    actual = tree.root.value
    expected = "First"
    assert actual == expected

def test_node_in_binary_tree():
    ten = Node(10)
    tree = BinaryTree(ten)
    actual = tree.root.value
    expected = 10
    assert actual == expected

def test_node_in_binary_tree_pre_xx_order():
    ten = Node(10)
    five = Node(5)
    fifteen = Node(15)
    ten.left = five
    ten.right = fifteen
    tree = BinaryTree(ten)
    actual = tree.pre_order()
    expected = [10,5,15]
    assert actual == expected

def test_node_in_binary_tree_in_order():
    ten = Node(10)
    five = Node(5)
    fifteen = Node(15)
    ten.left = five
    ten.right = fifteen
    tree = BinaryTree(ten)
    actual = tree.in_order()
    expected = [5,10,15]
    assert actual == expected

def test_node_in_binary_tree_post_order():
    ten = Node(10)
    five = Node(5)
    fifteen = Node(15)
    ten.left = five
    ten.right = fifteen
    tree = BinaryTree(ten)
    actual = tree.post_order()
    expected = [5,15,10]
    assert actual == expected
