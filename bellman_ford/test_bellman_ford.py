import pytest
from bellman_ford import Graph  # импортируем класс Graph из файла, где находится реализация алгоритма


def test_bellman_ford_no_negative_cycle():
    # Тест 1: Граф без отрицательных циклов
    g = Graph(5)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    distances = g.bellman_ford(0)

    assert distances is not None  # Проверяем, что результат не None
    assert distances[0] == 0  # Расстояние до самой себя должно быть 0
    assert distances[1] == -1  # Расстояние до вершины 1
    assert distances[2] == 2  # Расстояние до вершины 2
    assert distances[3] == -2  # Расстояние до вершины 3
    assert distances[4] == 1  # Расстояние до вершины 4


def test_bellman_ford_negative_cycle():
    # Тест 2: Граф с отрицательным циклом
    g = Graph(4)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 3, -1)
    g.add_edge(3, 1, -1)

    distances = g.bellman_ford(0)

    assert distances is None  # Алгоритм должен вернуть None, так как в графе есть отрицательный цикл


def test_bellman_ford_no_path():
    # Тест 3: Граф, где нет пути от исходной вершины к другим вершинам
    g = Graph(5)
    g.add_edge(0, 1, 2)
    g.add_edge(1, 2, 3)

    distances = g.bellman_ford(0)

    assert distances is not None
    assert distances[0] == 0  # Расстояние до самой себя
    assert distances[1] == 2  # Расстояние до вершины 1
    assert distances[2] == 5  # Расстояние до вершины 2
    assert distances[3] == float("inf")  # Вершина 3 недостижима
    assert distances[4] == float("inf")  # Вершина 4 недостижима


def test_bellman_ford_single_node():
    # Тест 4: Граф с одной вершиной
    g = Graph(1)
    distances = g.bellman_ford(0)

    assert distances is not None
    assert distances[0] == 0  # Расстояние до самой себя


if __name__ == '__main__':
    pytest.main()
