import pytest
from ford_fulkerson import Graph  # Импортируем класс Graph из файла max_flow.py

# Фикстуры для тестов

@pytest.fixture
def sample_graph_1():
    g = Graph(6)
    g.add_edge(0, 1, 16)
    g.add_edge(0, 2, 13)
    g.add_edge(1, 2, 10)
    g.add_edge(1, 3, 12)
    g.add_edge(2, 1, 4)
    g.add_edge(2, 4, 14)
    g.add_edge(3, 2, 9)
    g.add_edge(3, 5, 20)
    g.add_edge(4, 3, 7)
    g.add_edge(4, 5, 4)
    return g

@pytest.fixture
def sample_graph_2():
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 3, 10)
    g.add_edge(2, 1, 15)
    g.add_edge(2, 3, 10)
    return g

# Тесты

def test_max_flow_graph_1(sample_graph_1):
    source = 0
    sink = 5
    expected_max_flow = 23
    max_flow = sample_graph_1.ford_fulkerson(source, sink)
    assert max_flow == expected_max_flow, f"Ожидалось {expected_max_flow}, но получено {max_flow}"

def test_max_flow_graph_2(sample_graph_2):
    source = 0
    sink = 3
    expected_max_flow = 15
    max_flow = sample_graph_2.ford_fulkerson(source, sink)
    assert max_flow == expected_max_flow, f"Ожидалось {expected_max_flow}, но получено {max_flow}"

def test_max_flow_no_path():
    g = Graph(3)
    g.add_edge(0, 1, 10)
    g.add_edge(1, 2, 5)
    source = 0
    sink = 2
    expected_max_flow = 5
    max_flow = g.ford_fulkerson(source, sink)
    assert max_flow == expected_max_flow, f"Ожидалось {expected_max_flow}, но получено {max_flow}"

def test_max_flow_no_possible_flow():
    g = Graph(3)
    g.add_edge(0, 1, 0)  # Нет пропускной способности
    g.add_edge(1, 2, 0)  # Нет пропускной способности
    source = 0
    sink = 2
    expected_max_flow = 0
    max_flow = g.ford_fulkerson(source, sink)
    assert max_flow == expected_max_flow, f"Ожидалось {expected_max_flow}, но получено {max_flow}"
