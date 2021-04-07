# Node class to make link list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# graph class to make adjacency matrix
class Graph:
    def __init__(self, v):
        self.v = v
        self.graph = [None] * self.v

    # to insert edge to undirected graph
    def insertEdge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def printGraph(self):
        for i in range(self.v):
            temp = self.graph[i]
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next
            print()


if __name__ == '__main__':
    graph = Graph(3)
    graph.insertEdge(0, 1)
    graph.insertEdge(0, 2)
    graph.insertEdge(1, 2)
    graph.printGraph()
