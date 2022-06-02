from collections import deque
import sys


# def dfs(r):

#     stack = deque()
#     visited = []
#     stack.append(r)

#     while stack:
#         node = stack.pop()

#         if node not in visited:
#             visited.append(node)
#             stack.extend(graph[node])

#     return visited


n, m, r = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
graph_cnt = [0 for _ in range(n+1)]

# 그래프 만들어주기
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

for i in range(n+1):
    graph[i].sort()


cnt = 1
stack = deque()
stack.append(r)

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
