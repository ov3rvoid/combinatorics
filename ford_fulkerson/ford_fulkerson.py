from collections import defaultdict

# Класс для представления графа
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.graph = defaultdict(list)  # Список рёбер, хранимых в виде списка смежности

    # Добавление рёбер в граф
    def add_edge(self, u, v, w):
        self.graph[u].append([v, w])  # Добавляем ребро u->v с пропускной способностью w

    # Поиск увеличивающего пути с помощью DFS
    def dfs(self, source, sink, parent):
        visited = [False] * self.V  # Массив для отслеживания посещённых вершин
        stack = [source]
        visited[source] = True

        while stack:
            u = stack.pop()

            for v, capacity in self.graph[u]:
                if not visited[v] and capacity > 0:  # Если есть остаточная пропускная способность
                    stack.append(v)
                    visited[v] = True
                    parent[v] = u

                    # Если мы достигли стока, возвращаем True
                    if v == sink:
                        return True
        return False

    # Алгоритм Форда-Фалкерсона
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V  # Массив для отслеживания пути
        max_flow = 0  # Изначальный поток

        # Пока существует увеличивающий путь
        while self.dfs(source, sink, parent):
            # Находим минимальную пропускную способность на найденном пути
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, next(capacity for v, capacity in self.graph[parent[s]] if v == s))
                s = parent[s]

            # Обновляем остаточные пропускные способности рёбер
            v = sink
            while v != source:
                u = parent[v]
                for i in range(len(self.graph[u])):
                    if self.graph[u][i][0] == v:
                        self.graph[u][i][1] -= path_flow  # Уменьшаем пропускную способность
                for i in range(len(self.graph[v])):
                    if self.graph[v][i][0] == u:
                        self.graph[v][i][1] += path_flow  # Увеличиваем пропускную способность
                v = parent[v]

            max_flow += path_flow  # Увеличиваем общий поток на найденный путь

        return max_flow

# Пример использования
if __name__ == "__main__":
    g = Graph(6)  # Граф с 6 вершинами

    # Добавляем рёбра с пропускными способностями
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

    source = 0
    sink = 5

    # Находим максимальный поток
    print(f"Максимальный поток из {source} в {sink}: {g.ford_fulkerson(source, sink)}")
