def dfs(graph, start, visited=[]):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

    return visited


N = int(input())
M = int(input())

computers = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    computers[a].append(b)
    computers[b].append(a)


result = dfs(computers, 1)
print(len(result) - 1)
