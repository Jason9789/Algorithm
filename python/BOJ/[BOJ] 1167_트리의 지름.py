import sys
from collections import deque

read = sys.stdin.readline

V = int(sys.stdin.readline())
graph = [[] for _ in range(V+1)]


for _ in range(V):
    v = list(map(int, read().split()))

    for i in range(1, len(v)-2, 2):
        graph[v[0]].append((v[i], v[i+1]))


def bfs(start):
    visited = [-1] * (V+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    result = [0, 0]

    while q:
        node = q.popleft()

        for e, d in graph[node]:
            if visited[e] == -1:
                visited[e] = visited[node] + d

                q.append(e)
                if result[0] < visited[e]:
                    result = visited[e], e

    return result


distance, node = bfs(1)
distance, node = bfs(node)

print(distance)
