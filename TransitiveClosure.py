from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.closure = [[0 for i in range(self.v)] for j in range(self.v)]

    def insertEdge(self, src, des):
        self.graph[src].append(des)

    def dfsUntil(self, src, visited):
        visited[src] = 1

        for i in self.graph[src]:
            if visited[i] == 0:
                self.dfsUntil(i, visited)

    def getClosure(self):

        for i in range(self.v):
            visited = [0] * self.v
            self.dfsUntil(i,visited)
            for j in range(self.v):
                self.closure[i][j] = visited[j]

        print(*self.closure)


if __name__ == '__main__':
    graph = Graph(4)
    graph.insertEdge(0, 1)
    graph.insertEdge(1, 2)
    graph.insertEdge(1, 3)
    graph.insertEdge(0, 2)
    graph.getClosure()
