from tree.binary_search_tree import BinarySearchTree
from code_challenges.tree_intersection.tree_intersection import tree_intersection, tree_intersection_no_hash

def test_is_tree_intersection():
    assert tree_intersection

def test_tree_intersection():
    tree_b = BinarySearchTree()
    tree_b.add('10')
    tree_b.add('5')
    tree_b.add('1')
    tree_b.add('6')
    tree_b.add('14')
    tree_b.add('11')
    tree_b.add('15')
    tree_a = BinarySearchTree()
    tree_a.add('10')
    tree_a.add('5')
    tree_a.add('1')
    tree_a.add('6')
    tree_a.add('14')
    tree_a.add('11')
    tree_a.add('15')
    actual = tree_intersection(tree_a, tree_b)
    lst = ['10','5','1','6','14','11','15']
    expected = set(lst)
    assert actual == expected

def test_tree_intersection_with_not_perfect():
    tree_b = BinarySearchTree()
    tree_b.add('10')
    tree_b.add('5')
    tree_b.add('1')
    tree_b.add('6')
    tree_b.add('14')
    tree_b.add('11')
    tree_b.add('15')
    tree_a = BinarySearchTree()
    tree_a.add('10')
    tree_a.add('5')
    tree_a.add('1')
    tree_a.add('6')
    tree_a.add('7')
    tree_a.add('9')
    tree_a.add('45')
    actual = tree_intersection(tree_a, tree_b)
    lst = ['10','5','1','6']
    expected = set(lst)
    assert actual == expected

def test_tree_intersection_with_dupes():
    tree_b = BinarySearchTree()
    tree_b.add('10')
    tree_b.add('5')
    tree_b.add('5')
    tree_b.add('6')
    tree_b.add('5')
    tree_b.add('11')
    tree_b.add('15')
    tree_a = BinarySearchTree()
    tree_a.add('10')
    tree_a.add('5')
    tree_a.add('1')
    tree_a.add('6')
    tree_a.add('7')
    tree_a.add('9')
    tree_a.add('45')
    actual = tree_intersection(tree_a, tree_b)
    lst = ['10','5','6']
    expected = set(lst)
    assert actual == expected

def test_tree_intersection_with_one_tree_empty():
    tree_b = BinarySearchTree()
    tree_a = BinarySearchTree()
    tree_a.add('10')
    tree_a.add('5')
    tree_a.add('1')
    tree_a.add('6')
    tree_a.add('7')
    tree_a.add('9')
    tree_a.add('45')
    actual = tree_intersection(tree_a, tree_b)
    lst = []
    expected = set(lst)
    assert actual == expected

def test_tree_intersection_no_hash():
    tree_b = BinarySearchTree()
    tree_b.add('10')
    tree_b.add('5')
    tree_b.add('1')
    tree_b.add('6')
    tree_b.add('14')
    tree_b.add('11')
    tree_b.add('15')
    tree_a = BinarySearchTree()
    tree_a.add('10')
    tree_a.add('5')
    tree_a.add('1')
    tree_a.add('6')
    tree_a.add('14')
    tree_a.add('11')
    tree_a.add('15')
    actual = tree_intersection_no_hash(tree_a, tree_b)
    lst = ['10','5','1','6','14','11','15']
    expected = set(lst)
    assert actual == expected
