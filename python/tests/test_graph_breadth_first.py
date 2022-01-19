from graph.graph import Graph, Vertex
import pytest

def test_is_graph():
    assert Graph

def test_graph_is_empty_breadth():
    graph = Graph()
    vertex = Vertex('test')
    with pytest.raises(KeyError):
        graph.breadth_first(vertex)

def test_graph_no_connections():
    graph = Graph()
    one = graph.add_node(1)
    actual = graph.breadth_first(one)
    expected = [one]
    assert actual == expected

def test_graph_no_connections_with_others():
    graph = Graph()
    one = graph.add_node(1)
    two = graph.add_node(2)
    three = graph.add_node(3)
    four = graph.add_node(4)
    five = graph.add_node(5)
    graph.add_edge(three,four)
    graph.add_edge(four,five)
    graph.add_edge(four,three)
    actual = graph.breadth_first(one)
    expected = [one]
    assert actual == expected

def test_graph_breadth_first():
    graph = Graph()
    one = graph.add_node(1)
    two = graph.add_node(2)
    three = graph.add_node(3)
    four = graph.add_node(4)
    five = graph.add_node(5)
    six = graph.add_node(6)
    graph.add_edge(one,six)
    graph.add_edge(one,two)
    graph.add_edge(two,three)
    graph.add_edge(two,four)
    graph.add_edge(three,five)
    graph.add_edge(four,four)
    actual = graph.breadth_first(one)
    expected = [one, six, two, three, four,five]
    assert actual == expected
