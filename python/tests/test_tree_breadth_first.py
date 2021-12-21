from tree.binary_tree import BinaryTree
from tree.binary_tree import NodeTwo
from tree.binary_tree import Node
from code_challenges.tree_breadth_first.tree_breadth_first import tree_breadth_first
from code_challenges.tree_breadth_first.tree_breadth_first import tree_breadth_first_list

def test_is_tree_breadth_first():
    assert tree_breadth_first_list

def test_tree_breadth_first_basic_tree():
    ten = NodeTwo(10)
    tree_try = BinaryTree(ten)
    actual = tree_breadth_first_list(tree_try)
    expected = [10]
    assert actual == expected

def test_tree_breadth_first_tree():
    ten = NodeTwo(10,Node(5),Node(15))
    tree_try = BinaryTree(ten)
    actual = tree_breadth_first_list(tree_try)
    expected = [10,5,15]
    assert actual == expected
