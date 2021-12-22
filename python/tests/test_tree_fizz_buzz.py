from code_challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree
from tree.k_tree import Ktree
from code_challenges.tree_fizz_buzz.tree_fizz_buzz import fizz_buzz_tree
import pytest

def test_is_ktree():
    assert Ktree

def test_is_fiz_buzz():
    assert fizz_buzz_tree

def test_ktree_add_and_fizz_buzz():
    tree = Ktree(3)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(4)
    tree.add_node(5)
    tree.add_node(3)
    tree.add_node(7)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ["2","Fizz","4","Buzz","Fizz","7"]
    assert actual == expected

def test_ktree_add_and_fizz_buzz_fizzbuzz():
    tree = Ktree(3)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(15)
    tree.add_node(5)
    tree.add_node(3)
    tree.add_node(7)
    new_tree = fizz_buzz_tree(tree)
    actual = new_tree.breadth_first()
    expected = ["2","Fizz","FizzBuzz","Buzz","Fizz","7"]
    assert actual == expected

def test_ktree_add_check_children():
    tree = Ktree(3)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(15)
    tree.add_node(5)
    tree.add_node(3)
    tree.add_node(7)
    actual = tree.root.children[2].value
    expected = 5
    assert actual == expected

def test_ktree_add_check_children():
    tree = Ktree(3)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(15)
    tree.add_node(5)
    tree.add_node(3)
    tree.add_node(7)
    with pytest.raises(IndexError):
        tree.root.children[3].value

def test_ktree_add_check_children():
    tree = Ktree(3)
    actual = fizz_buzz_tree(tree)
    expected = "Empty Tree"
    assert actual == expected

