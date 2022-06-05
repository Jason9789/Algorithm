from collections import deque


def dfs(graph, start, visited=[]):
    visited.append(start)

    for node in sorted(graph[start]):
        if node not in visited:
            dfs(graph, node, visited)

    return visited


def bfs(graph, start):
    queue = deque()
    visited = []

    queue.append(start)

    while queue:
        node = queue[0]
        queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node]))

    return visited


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    v, u = map(int, input().split())

    graph[v].append(u)
    graph[u].append(v)


print(" ".join(map(str, dfs(graph, V))))
print(" ".join(map(str, bfs(graph, V))))
