from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def insertEdge(self, src, des):
        self.graph[src].append(des)

    def dfsUntil(self, src, visited):
        visited[src] = 1
        print(src)

        for i in self.graph[src]:
            if visited[i] == 0:
                self.dfsUntil(i, visited)

    def dfs(self, s):
        visited = [0] * self.v
        self.dfsUntil(s, visited)


if __name__ == '__main__':
    graph = Graph(4)
    graph.insertEdge(0, 1)
    graph.insertEdge(1, 2)
    graph.insertEdge(1, 3)
    graph.insertEdge(0, 2)
    graph.dfs(0)
