from sorts.merge_sort.merge_sort import merge_sort

def test_is_merge_sort():
    assert merge_sort

def test_merge_sort():
    lst = [6,8,4,1,2]
    merge_sort(lst)
    actual = lst
    expected = [1,2,4,6,8]
    assert actual == expected

def test_merge_sort_multiple_the_same():
    lst = [4,4,4,4,4]
    merge_sort(lst)
    actual = lst
    expected = [4,4,4,4,4]
    assert actual == expected

def test_merge_sort_multiple_the_same_plus_others():
    lst = [4,4,4,4,4,8,1,6,7,3]
    merge_sort(lst)
    actual = lst
    expected = [1,3,4,4,4,4,4,6,7,8]
    assert actual == expected

def test_merge_sort_negatives():
    lst = [-6,-9,2,-1,-3,4]
    merge_sort(lst)
    actual = lst
    expected = [-9,-6,-3,-1,2,4]
    assert actual == expected
