from collections import deque


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.link = None


class Graph:
    def __init__(self, size):
        self.adjList = [None] * size
        self.visited = [False] * size
        self.n = size
        self.indegree = [0] * size
        self.Q = deque()

    def add_edge(self, v1, v2):
        new_node = Node(v2)
        new_node.link = self.adjList[v1]
        self.adjList[v1] = new_node
        self.indegree[v2] += 1

    def indegreeM(self):
        for v in range(self.n):
            if (self.indegree[v] == 0):
                self.Q.append(v)
        temp = []
        while (self.Q):
            print("Q:", self.Q)
            V = self.Q.popleft()
            temp.append(V)
            node = self.adjList[V]
            while node is not None:
                self.indegree[node.vertex] -= 1
                if (self.indegree[node.vertex] == 0):
                    self.Q.append(node.vertex)
                node = node.link

        for i in range(len(temp) - 1):
            print(temp[i], end="->")
        print(temp[-1])

    def dfs(self, v):
        self.visited[v] = True
        node = self.adjList[v]
        while node != None:
            w = node.vertex
            if self.visited[w] is False:
                self.dfs(w)
            node = node.link
        print(v, end=' ')

    def printGraph(self):
        for v in range(self.n):
            print(v, end=": ")
            current = self.adjList[v]
            while current is not None:
                print(current.vertex, end=' ')
                current = current.link
            print()

    def revTopologicalSort(self):
        for v in range(self.n):
            if self.visited[v] is False:
                self.dfs(v)


n, m = [int(x) for x in input().split()]
g = Graph(n)
for i in range(m):
    v1, v2 = [int(x) for x in input().split()]
    g.add_edge(v1, v2)

g.indegreeM()
# g.printGraph()
# g.revTopologicalSort()