from collections import deque
import sys
sys.setrecursionlimit(10**6)

read = sys.stdin.readline

n = int(read())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):

    v = list(map(int, read().split()))
    graph[v[0]].append([v[1], v[2]])
    graph[v[1]].append([v[0], v[2]])


visited = [-1] * (n+1)
visited[1] = 0


def dfs(start, weight):
    for v in graph[start]:
        node, wei = v

        if visited[node] == -1:
            visited[node] = weight + wei
            dfs(node, weight + wei)


dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (n+1)
visited[start] = 0

dfs(start, 0)

print(max(visited))
