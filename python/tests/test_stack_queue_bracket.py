from code_challenges.stack_queue_brackets.stack_queue_brackets import validate_brackets

def test_is_validate_brackets():
    assert validate_brackets

def test_validate_brackets_input():
    string = "Hello"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets_with_odd_brackets():
    string = "((("
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_validate_brackets_true():
    string = "(())"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets_true_with_letters():
    string = "(adsgf(asdf)asd)asdf"
    actual = validate_brackets(string)
    expected = True
    assert actual == expected

def test_validate_brackets_false():
    string = "(()()))("
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

def test_validate_brackets_false_weird():
    string = "({(asdfsadf){[]asdf()))(}"
    actual = validate_brackets(string)
    expected = False
    assert actual == expected

