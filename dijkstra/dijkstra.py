import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices  # количество вершин
        self.graph = [[] for _ in range(vertices)]  # список смежности

    def add_edge(self, u, v, weight):
        """Добавляем ребро (u, v) с весом weight"""
        if u >= self.V or v >= self.V:
            raise ValueError("Неверные вершины.")
        if weight < 0:
            raise ValueError("Вес рёбер не может быть отрицательным.")
        self.graph[u].append((v, weight))  # ребро u -> v с весом weight
        self.graph[v].append((u, weight))  # для неориентированного графа, добавляем и обратное ребро

    def dijkstra(self, start):
        """Алгоритм Дейкстры с использованием черпака (min-heap)"""
        if start >= self.V:
            raise ValueError("Начальная вершина выходит за пределы графа.")

        # Расстояния до всех вершин, начнем с бесконечности
        distances = [float("inf")] * self.V
        distances[start] = 0

        # Множество вершин, которые ещё не были обработаны
        pq = [(0, start)]  # (расстояние, вершина)
        visited = [False] * self.V  # Массив для проверки, были ли вершины обработаны

        while pq:
            current_distance, u = heapq.heappop(pq)  # извлекаем вершину с минимальным расстоянием

            # Если вершина уже была обработана, пропускаем её
            if visited[u]:
                continue
            visited[u] = True

            # Рассматриваем все соседние вершины
            for v, weight in self.graph[u]:
                distance = current_distance + weight

                # Если нашли более короткий путь до вершины v, обновляем расстояние
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))  # добавляем новую вершину в очередь с приоритетом

        return distances
