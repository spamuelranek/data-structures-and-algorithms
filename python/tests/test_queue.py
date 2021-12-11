from code_challenges.stack_and_queue.queue import Queue
import pytest

def test_is_queue():
    q = Queue()
    assert q

def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected

def test_peek_queue():
    q = Queue()
    with pytest.raises(ValueError):
        q.peek()

def test_en_q():
    q = Queue()
    q.enq("Bubba Gump")
    actual = q.peek()
    expected = "Bubba Gump"
    assert actual == expected

def test_de_q_empty():
    q = Queue()
    with pytest.raises(ValueError):
        q.deq()

def test_de_q_empty():
    q = Queue()
    q.enq("Dog")
    actual = q.deq()
    expected = "Dog"
    assert actual == expected

def test_multiple_en_q():
    q = Queue()
    q.enq("Bubba Gump")
    q.enq("Shrimp Company")
    q.deq()
    actual = q.peek()
    expected = "Shrimp Company"
    assert actual == expected

def test_multiple_dn_q():
    q = Queue()
    q.enq("Bubba Gump")
    q.enq("Shrimp Company")
    q.deq()
    q.deq()
    with pytest.raises(ValueError):
        q.peek()

def test_multiple_dn_q_is_empty():
    q = Queue()
    q.enq("Bubba Gump")
    q.enq("Shrimp Company")
    q.deq()
    q.deq()
    actual = q.is_empty()
    expected = True
    assert actual == True

def test_dequeue():
    q = Queue()
    q.enq("apple")
    q.enq("banana")
    actual = q.deq()
    expected = "apple"
    assert actual == expected
