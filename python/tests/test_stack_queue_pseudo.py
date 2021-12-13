from code_challenges.stack_queue_pseudo.stack_queue_pseudo import PseudoQueue
import pytest

def test_is_psuedo_queue():
    pq = PseudoQueue
    assert pq

def test_is_psuedo_queue_enque():
    pq = PseudoQueue
    assert pq.enqueue

def test_is_psuedo_queue_deque():
    pq = PseudoQueue
    assert pq.dequeue

def test_psuedo_queue_enque():
    pq = PseudoQueue()
    pq.enqueue("z")
    actual = pq.dequeue()
    expected = "z"
    assert actual == expected

def test_psuedo_queue_enque_multiple():
    pq = PseudoQueue()
    pq.enqueue("z")
    pq.enqueue("y")
    pq.enqueue("x")
    actual = pq.dequeue()
    expected = "z"
    assert actual == expected

def test_psuedo_queue_enque_multiple_and_deque_multiple():
    pq = PseudoQueue()
    pq.enqueue("z")
    pq.enqueue("y")
    pq.enqueue("x")
    pq.dequeue()
    pq.dequeue()
    actual = pq.dequeue()
    expected = "x"
    assert actual == expected

def test_psuedo_queue_deque_empty():
    pq = PseudoQueue()
    with pytest.raises(IndexError):
        pq.dequeue()
