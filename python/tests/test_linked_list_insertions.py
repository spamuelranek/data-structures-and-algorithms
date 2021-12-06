from linked_list.linked_list import LinkedList

def test_append_to_list():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(3)
    new_list.insert(1)
    new_list.append(5)
    actual = str(new_list)
    expected = "{1} -> {3} -> {2} -> {5} -> NULL"
    assert expected == actual

def test_append_to_empty_list():
    new_list = LinkedList()
    new_list.append(5)
    actual = str(new_list)
    expected = "{5} -> NULL"
    assert expected == actual

def test_append_to_empty_list():
    new_list = LinkedList()
    new_list.append(5)
    new_list.append(5)
    new_list.append(5)
    actual = str(new_list)
    expected = "{5} -> {5} -> {5} -> NULL"
    assert expected == actual

def test_insert_before():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(3)
    new_list.insert(1)
    new_list.insert_before(5,3)
    actual = str(new_list)
    expected = "{1} -> {5} -> {3} -> {2} -> NULL"
    assert actual == expected

def test_insert_before_all():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(3)
    new_list.insert(1)
    new_list.insert_before(5,1)
    actual = str(new_list)
    expected = "{5} -> {1} -> {3} -> {2} -> NULL"
    assert actual == expected

def test_insert_before_value_not_in_list():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(3)
    new_list.insert(1)
    actual = new_list.insert_before(5,4)
    expected = "That value is not in this list"
    assert actual == expected

def test_insert_before_value_in_empty_list():
    new_list = LinkedList()
    actual = new_list.insert_before(5,4)
    expected = "This list is empty"
    assert actual == expected

def test_insert_after_list():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(3)
    new_list.insert(1)
    new_list.insert_after(5,3)
    actual = str(new_list)
    expected = "{1} -> {3} -> {5} -> {2} -> NULL"
    assert actual == expected

def test_insert_after_all_list():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(3)
    new_list.insert(1)
    new_list.insert_after(5,2)
    actual = str(new_list)
    expected = "{1} -> {3} -> {2} -> {5} -> NULL"
    assert actual == expected

def test_insert_after_value_not_in_list():
    new_list = LinkedList()
    new_list.insert(2)
    new_list.insert(3)
    new_list.insert(1)
    actual = new_list.insert_after(5,4)
    expected = "That value is not in this list"
    assert actual == expected

def test_insert_after_value_in_empty_list():
    new_list = LinkedList()
    actual = new_list.insert_after(5,4)
    expected = "This list is empty"
    assert actual == expected

# def test():
#     acutal
#     expected
#     assert actual == expected

