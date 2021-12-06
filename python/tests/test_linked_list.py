from linked_list.linked_list import LinkedList, Node


def test_import():
    assert LinkedList

def test_node():
    node = Node("piggy smalls")
    actual = node.value
    expected = "piggy smalls"
    assert actual == expected

def test_init_linked_list():
    linked_list = LinkedList()
    actual = linked_list.head
    expected = None
    assert actual == expected

def test_add_node_to_front_empty():
    linked_list = LinkedList()
    linked_list.insert("the truest true")
    actual = linked_list.head.value
    expected = "the truest true"
    assert actual == expected

def test_add_node_to_front():
    linked_list = LinkedList()
    linked_list.insert("the truest true")
    linked_list.insert("somber leaves leave")
    actual = linked_list.head.value
    expected = "somber leaves leave"
    assert actual == expected

def test_includes():
    linked_list = LinkedList()
    linked_list.insert("the truest true")
    linked_list.insert("somber leaves leave")
    actual = linked_list.includes("somber leaves leave")
    expected = True
    assert actual == expected

def test_includes():
    linked_list = LinkedList()
    linked_list.insert("the truest true")
    linked_list.insert("somber trees only bloom in the winter")
    actual = linked_list.includes("somber leaves leave")
    expected = False
    assert actual == expected

def test_str():
    linked_list = LinkedList()
    linked_list.insert("the truest true")
    linked_list.insert("somber trees only bloom in the winter")
    linked_list.insert("trampling on broken flowers only hurts me")
    actual = str(linked_list)
    expected = "{trampling on broken flowers only hurts me} -> {somber trees only bloom in the winter} -> {the truest true} -> NULL"
    assert actual == expected



