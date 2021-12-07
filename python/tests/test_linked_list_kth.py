from linked_list.linked_list import LinkedList
import pytest

def test_kth_from_end():
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    actual = lst.kth_from_end(0)
    expected = 1
    assert actual == expected

def test_kth_from_end_list_of_one():
    lst = LinkedList()
    lst.insert(1)
    actual = lst.kth_from_end(0)
    expected = 1
    assert actual == expected

def test_kth_from_end_two():
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    actual = lst.kth_from_end(1)
    expected = 2
    assert actual == expected

def test_kth_from_end_three():
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    actual = lst.kth_from_end(2)
    expected = 3
    assert actual == expected

def test_kth_from_end_same_value_as_length():
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    with pytest.raises(ValueError):
        lst.kth_from_end(3)

def test_kth_from_negative_value():
    lst = LinkedList()
    lst.insert(1)
    lst.insert(2)
    lst.insert(3)
    with pytest.raises(ValueError):
        lst.kth_from_end(-1)

