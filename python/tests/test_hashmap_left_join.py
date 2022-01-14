from code_challenges.hashmap_left_join.hashmap_left_join import add_left

def test_is_add_left():
    assert add_left

def test_add_left():
    hash_left = {'x':1, 'y':2, 'z':3}
    hash_right = {'x':-1,'z':-3}
    actual = add_left(hash_left, hash_right)
    expected = [['x',1,-1],['y',2,None],['z',3,-3]]
    assert actual == expected

def test_add_left_if_empty():
    hash_left = {}
    hash_right = {'x':-1,'z':-3}
    actual = add_left(hash_left, hash_right)
    expected = []
    assert actual == expected

def test_add_left_right_if_empty():
    hash_left = {'x':1, 'y':2, 'z':3}
    hash_right = {}
    actual = add_left(hash_left, hash_right)
    expected = [['x',1,None],['y',2,None],['z',3,None]]
    assert actual == expected

def test_add_left_sample():
    hash_left = {'diligent':'employed', 'fond':'enamored', 'guide':'usher', 'outfit': 'garb', 'wrath': 'anger'}
    hash_right = {'diligent':'idle', 'fond': 'averse', 'guide':'follow', 'flow':'jam', 'wrath':'delight'}
    actual = add_left(hash_left, hash_right)
    expected = [['diligent','employed','idle'],['fond','enamored','averse'],['guide','usher','follow'],['outfit','garb',None],['wrath','anger','delight']]
    assert actual == expected
