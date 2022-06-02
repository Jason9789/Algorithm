from collections import deque
import sys


def bfs(r):
    cnt = 1
    visited[r] = cnt

    queue = deque()
    queue.append(r)

    while queue:
        node = queue.popleft()

        for i in graph[node]:
            if visited[i] == 0:
                cnt += 1
                queue.append(i)
                visited[i] = cnt


n, m, r = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

# 그래프 만들기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

bfs(r)

for i in range(1, n+1):
    print(visited[i])
