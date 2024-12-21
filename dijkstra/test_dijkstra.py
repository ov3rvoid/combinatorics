import pytest
from dijkstra import Graph  # Импортируйте свой класс Graph


# Тест 1: Проверка стандартного случая
def test_dijkstra_basic():
    g = Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 1)
    g.add_edge(2, 3, 9)
    g.add_edge(3, 4, 4)

    distances = g.dijkstra(0)

    # Проверяем минимальные расстояния от вершины 0
    assert distances[0] == 0
    assert distances[1] == 7
    assert distances[2] == 5
    assert distances[3] == 8
    assert distances[4] == 12


# Тест 2: Проверка на граф с одной вершиной
def test_dijkstra_single_vertex():
    g = Graph(1)
    distances = g.dijkstra(0)

    # Для графа с одной вершиной расстояние до самой себя должно быть 0
    assert distances[0] == 0


# Тест 3: Проверка на граф без рёбер
def test_dijkstra_no_edges():
    g = Graph(3)
    distances = g.dijkstra(0)

    # Если нет рёбер, расстояние от вершины 0 до остальных должно быть бесконечностью
    assert distances[0] == 0
    assert distances[1] == float("inf")
    assert distances[2] == float("inf")


# Тест 4: Проверка на недопустимую вершину
def test_dijkstra_invalid_vertex():
    g = Graph(3)

    with pytest.raises(ValueError):
        g.add_edge(0, 3, 5)  # Вершина 3 не существует в графе с 3 вершинами

    with pytest.raises(ValueError):
        g.dijkstra(3)  # Дейкстра не может стартовать с вершины, которой нет в графе


# Тест 5: Проверка корректности работы при добавлении нескольких одинаковых рёбер
def test_dijkstra_multiple_edges():
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 1, 5)  # Добавляем ещё одно ребро с меньшим весом

    distances = g.dijkstra(0)

    # Проверяем, что алгоритм использует наименьший вес
    assert distances[1] == 5  # Ожидаем, что минимальное расстояние будет равно 5


# Тест 6: Проверка на пустой граф
def test_dijkstra_empty_graph():
    g = Graph(0)

    # Алгоритм не может работать с пустым графом, должен выбросить ошибку
    with pytest.raises(ValueError):
        g.dijkstra(0)


if __name__ == '__main__':
    pytest.main()
