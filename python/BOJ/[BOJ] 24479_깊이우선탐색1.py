import sys
from collections import deque

N, M, R = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
graph_cnt = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)


for i in range(N+1):
    graph[i].sort(reverse=True)


cnt = 1
stack = deque()
stack.append(R)


while stack:
    node = stack.pop()
    visited[node] = True

    if graph_cnt[node] == 0:
        graph_cnt[node] = cnt
        cnt += 1

    for next_node in graph[node]:
        if not visited[next_node]:
            stack.append(next_node)


for cnt in graph_cnt[1:]:
    print(cnt)
