from tree.k_tree import NodeKtree, Ktree

def test_is_node_ktree():
    assert NodeKtree

def test_is_ktree():
    assert Ktree

def test_ktree_add_to_empty():
    tree = Ktree(3)
    tree.add_node(2)
    actual = tree.root.value
    expected = 2
    assert actual == expected

def test_ktree_add_to_one():
    tree = Ktree(3)
    tree.add_node(2)
    tree.add_node(3)
    actual = tree.root.children[0].value
    expected = 3
    assert actual == expected

def test_ktree_add():
    tree = Ktree(3)
    tree.add_node(2)
    tree.add_node(3)
    tree.add_node(4)
    tree.add_node(5)
    tree.add_node(3)
    tree.add_node(7)
    actual = tree.breadth_first()
    expected = [2,3,4,5,3,7]
    assert actual == expected
