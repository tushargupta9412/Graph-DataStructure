from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def insertEdge(self, src, des):
        self.graph[src].append(des)

    def bfs(self, src):
        visited = [0] * self.v
        # print(max(self.graph))
        # print(self.graph)
        l = [src]
        visited[src] = 1
        while l:
            s = l.pop(0)
            print(s)
            # print(self.graph[s])
            for i in self.graph[s]:
                if visited[i] == 0:
                    l.append(i)
                    visited[i] = 1


if __name__ == '__main__':
    graph = Graph(4)
    graph.insertEdge(0, 1)
    graph.insertEdge(1, 2)
    graph.insertEdge(1, 3)
    graph.insertEdge(0, 2)
    graph.bfs(0)
