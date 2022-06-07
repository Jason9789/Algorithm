import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)


def dfs(start):
    for i in graph[start]:
        if visited[i] == 0:
            visited[i] = start

            dfs(i)


dfs(1)


for i in range(2, n+1):
    print(visited[i])
