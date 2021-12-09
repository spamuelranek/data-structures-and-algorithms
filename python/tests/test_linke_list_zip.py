from linked_list.linked_list import LinkedList
from code_challenges.linked_list_zip.linked_list_zip import zip_lists
import pytest
# @pytest.mark.skip('pending')
def test_zip_lists():
    a = LinkedList()
    a.insert("1")
    b = LinkedList()
    b.insert("One")
    actual = str(zip_lists(a,b))
    expected = "{1} -> {One} -> NULL"

    assert actual == expected

# @pytest.mark.skip('pending')
def test_zip_lists_with_two_zips():
    a = LinkedList()
    a.insert("1")
    a.insert("2")
    b = LinkedList()
    b.insert("One")
    actual = str(zip_lists(a,b))
    expected = "{2} -> {One} -> {1} -> NULL"

    assert actual == expected

# @pytest.mark.skip('pending')
def test_zip_lists_with_three_zips():
    a = LinkedList()
    a.insert("1")
    a.insert("2")
    b = LinkedList()
    b.insert("One")
    b.insert("Two")
    actual = str(zip_lists(a,b))
    expected = "{2} -> {Two} -> {1} -> {One} -> NULL"

    assert actual == expected


def test_zip_lists_with_shorter_second_list():
    a = LinkedList()
    a.insert("1")
    a.insert("2")
    b = LinkedList()
    b.insert("One")
    actual = str(zip_lists(a,b))
    expected = "{2} -> {One} -> {1} -> NULL"

    assert actual == expected


def test_zip_lists_with_shorter_first_list():
    a = LinkedList()
    a.insert("1")
    b = LinkedList()
    b.insert("One")
    b.insert("Two")
    actual = str(zip_lists(a,b))
    expected = "{1} -> {Two} -> {One} -> NULL"

    assert actual == expected

def test_zip_lists_with_way_longer_first_list():
    a = LinkedList()
    a.insert("1")
    a.insert("2")
    a.insert("3")
    a.insert("4")
    b = LinkedList()
    b.insert("One")
    b.insert("Two")
    actual = str(zip_lists(a,b))
    expected = "{4} -> {Two} -> {3} -> {One} -> {2} -> {1} -> NULL"

    assert actual == expected
