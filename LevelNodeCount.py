from collections import defaultdict


class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = defaultdict(list)

    def insertEdge(self, s, d):
        self.graph[s].append(d)
        self.graph[d].append(s)

    def countNode(self, lev):
        visited = [0] * self.v
        level = [0] * self.v

        l = [0]
        visited[0] = 1
        level[0] = 0

        while len(l) > 0:
            s = l[0]
            l = l[1:len(l) - 1]
            for i in self.graph[s]:
                if visited[i] == 0:
                    visited[i] = 1
                    level[i] = level[s] + 1
                    l.append(i)
        count = 0
        for i in level:
            if i == lev:
                count += 1
        print(count)


if __name__ == '__main__':
    graph = Graph(5)
    graph.insertEdge(0, 1)
    graph.insertEdge(1, 2)
    graph.insertEdge(1, 3)
    graph.insertEdge(1, 4)
    graph.countNode(2)
