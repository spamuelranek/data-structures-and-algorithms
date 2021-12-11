from code_challenges.stack_and_queue.stack import Stack
import pytest
def test_if_stack():
    stack = Stack
    assert stack

def test_is_empty():
    stack = Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek_stack_empty():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.peek()

def test_push_stack():
    stack = Stack()
    stack.push("first")
    actual = stack.peek()
    expected = "first"
    assert actual == expected

def test_pop_stack():
    stack = Stack()
    stack.push("first")
    stack.push("second")
    stack.pop()
    actual = stack.peek()
    expected = "first"
    assert actual == expected

def test_multiple_pops_stack():
    stack = Stack()
    stack.push("first")
    stack.push("second")
    stack.pop()
    stack.pop()
    with pytest.raises(ValueError):
        stack.peek()


def test_pop_stack_empty():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.pop()
