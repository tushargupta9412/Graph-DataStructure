from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)
        self.path = 0

    def insertEdge(self, s, d):
        self.graph[s].append(d)

    def countPath(self, s, d):
        visited = [0] * self.v

        self.path = 0
        self.countPathTill(s, d, visited)
        print(self.path)

    def countPathTill(self, s, d, visited):
        visited[s] = 1
        if s == d:
            self.path += 1
        else:
            for i in self.graph[s]:
                if visited[i] == 0:
                    self.countPathTill(i, d, visited)
        visited[s] = 0


if __name__ == '__main__':
    graph = Graph(5)
    graph.insertEdge(0, 1)
    graph.insertEdge(1, 2)
    graph.insertEdge(0, 4)
    graph.insertEdge(1, 3)
    graph.insertEdge(1, 4)
    graph.countPath(0, 4)
