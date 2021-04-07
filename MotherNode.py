from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def insertEdge(self, src, des):
        self.graph[src].append(des)

    def dfsUntil(self, src, visited):
        visited[src] = 1

        for i in self.graph[src]:
            if visited[i] == 0:
                self.dfsUntil(i, visited)

    def getMother(self):

        visited = [0] * self.v
        a = 0
        for i in self.graph[a]:
            if visited[i] == 0:
                self.dfsUntil(i, visited)
                a = i
        visited = [0] * self.v
        self.dfsUntil(a, visited)
        if any(i == 0 for i in visited):
            return -1
        return a


if __name__ == '__main__':
    graph = Graph(4)
    graph.insertEdge(0, 1)
    graph.insertEdge(1, 2)
    graph.insertEdge(1, 3)
    graph.insertEdge(0, 2)
    print(graph.getMother())
