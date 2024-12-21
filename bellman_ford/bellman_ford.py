# Алгоритм Беллмана-Форда для нахождения кратчайших расстояний

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.edges = []    # Список рёбер графа

    # Добавляем ребро с заданными вершинами и весом
    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    # Реализация алгоритма Беллмана-Форда
    def bellman_ford(self, source):
        # Шаг 1: Инициализация
        distances = [float("inf")] * self.V  # Расстояния от исходной вершины
        distances[source] = 0  # Расстояние до самой себя равно 0

        # Шаг 2: Повторяем релаксацию рёбер V-1 раз
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight

        # Шаг 3: Проверка на отрицательные циклы
        for u, v, weight in self.edges:
            if distances[u] != float("inf") and distances[u] + weight < distances[v]:
                print("Граф содержит отрицательный цикл")
                return None

        return distances

# Пример использования
if __name__ == "__main__":
    # Создаём граф с 5 вершинами
    g = Graph(5)

    # Добавляем рёбра (u, v, weight)
    g.add_edge(0, 1, -1)
    g.add_edge(0, 2, 4)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 4, 2)
    g.add_edge(3, 2, 5)
    g.add_edge(3, 1, 1)
    g.add_edge(4, 3, -3)

    # Находим кратчайшие расстояния от вершины 0
    distances = g.bellman_ford(0)

    if distances:
        print("Кратчайшие расстояния от вершины 0:")
        for i, dist in enumerate(distances):
            print(f"До вершины {i}: {dist}")
