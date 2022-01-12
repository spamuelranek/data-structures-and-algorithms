from hash_table.hash_table import HashTable

def test_is_hash_table():
    actual = HashTable
    assert actual

def test_hash():
    make_hash = HashTable(10)
    actual = make_hash.hash("cat")
    expected = 2
    assert actual == expected

def test_hash_table_cat():
    make_hash = HashTable(10)
    make_hash.add("cat",1)
    actual = make_hash.buckets[2].head.value["cat"]
    expected = 1
    assert actual == expected

def test_hash_table_act_collision():
    make_hash = HashTable(10)
    make_hash.add("cat",1)
    make_hash.add("act",2)
    actual = make_hash.buckets[2].head.next.value["act"]
    expected = 2
    assert actual == expected

def test_hash_table_get():
    make_hash = HashTable(10)
    make_hash.add("cat",1)
    actual = make_hash.get("cat")
    expected = 1
    assert actual == expected

def test_hash_table_get_collision():
    make_hash = HashTable(10)
    make_hash.add("cat",1)
    make_hash.add("act",2)
    actual = make_hash.get("act")
    expected = 2
    assert actual == expected

def test_hash_table_contain():
    make_hash = HashTable(10)
    make_hash.add("cat",1)
    actual = make_hash.get("cat")
    expected = True
    assert actual == expected

def test_hash_table_does_not_contain():
    make_hash = HashTable(10)
    make_hash.add("cat",1)
    actual = make_hash.contains("act")
    expected = False
    assert actual == expected

def test_hash_table_does_not_get():
    make_hash = HashTable(10)
    make_hash.add("cat",1)
    actual = make_hash.get("act")
    expected = "null"
    assert actual == expected
