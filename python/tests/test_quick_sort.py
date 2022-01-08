from sorts.quick_sort.quick_sort import quick_sort

def test_is_quick_sort():
    assert quick_sort

def test_quick_sort():
    lst = [6,8,4,1,2]
    quick_sort(lst,0,len(lst)-1)
    actual = lst
    expected = [1,2,4,6,8]
    assert actual == expected

def test_quick_sort_multiple_the_same():
    lst = [4,4,4,4,4]
    quick_sort(lst,0,len(lst)-1)
    actual = lst
    expected = [4,4,4,4,4]
    assert actual == expected

def test_quick_sort_multiple_the_same_plus_others():
    lst = [4,4,4,4,4,8,1,6,7,3]
    quick_sort(lst,0,len(lst)-1)
    actual = lst
    expected = [1,3,4,4,4,4,4,6,7,8]
    assert actual == expected

def test_quick_sort_negatives():
    lst = [-6,-9,2,-1,-3,4]
    quick_sort(lst,0,len(lst)-1)
    actual = lst
    expected = [-9,-6,-3,-1,2,4]
    assert actual == expected
