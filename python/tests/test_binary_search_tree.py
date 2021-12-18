from tree.binary_search_tree import BinarySearchTree
from tree.binary_tree import BinaryTree

def test_is_binary_search_tree():
    tree = BinarySearchTree()
    assert tree

def test_is_binary_searh_a_tree():
    tree = BinarySearchTree()
    assert isinstance(tree,BinaryTree)

def test_binary_search_tree_new_root():
    tree_b = BinarySearchTree()
    tree_b.add(15)
    actual = tree_b.pre_order()
    expected = [15]
    assert actual == expected

def test_binary_search_tree_add_multiple():
    tree_b = BinarySearchTree()
    tree_b.add(10)
    tree_b.add(5)
    tree_b.add(15)
    actual = tree_b.pre_order()
    expected = [10,5,15]
    assert actual == expected

def test_binary_search_tree_add_a_lot():
    tree_b = BinarySearchTree()
    tree_b.add(10)
    tree_b.add(5)
    tree_b.add(1)
    tree_b.add(6)
    tree_b.add(14)
    tree_b.add(11)
    tree_b.add(15)
    actual = tree_b.pre_order()
    expected = [10,5,1,6,14,11,15]
    assert actual == expected

def test_binary_search_tree_add_a_lot_in_order():
    tree_b = BinarySearchTree()
    tree_b.add(10)
    tree_b.add(5)
    tree_b.add(1)
    tree_b.add(6)
    tree_b.add(14)
    tree_b.add(11)
    tree_b.add(15)
    actual = tree_b.in_order()
    expected = [1,5,6,10,11,14,15]
    assert actual == expected

def test_binary_search_tree_add_a_lot_post_order():
    tree_b = BinarySearchTree()
    tree_b.add(10)
    tree_b.add(5)
    tree_b.add(1)
    tree_b.add(6)
    tree_b.add(14)
    tree_b.add(11)
    tree_b.add(15)
    actual = tree_b.post_order()
    expected = [1,6,5,11,15,14,10]
    assert actual == expected

def test_binary_search_tree_contains_true():
    tree_b = BinarySearchTree()
    tree_b.add(10)
    tree_b.add(5)
    tree_b.add(15)
    actual = tree_b.contains(15)
    expected = True
    assert actual == expected

def test_binary_search_tree_contains_false():
    tree_b = BinarySearchTree()
    tree_b.add(10)
    tree_b.add(5)
    tree_b.add(15)
    actual = tree_b.contains(6)
    expected = False
    assert actual == expected
