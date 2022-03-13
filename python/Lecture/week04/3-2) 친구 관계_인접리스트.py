import sys

n, m = map(int, sys.stdin.readline().split())

adjMatrix = [[] for _ in range(n)]

for _ in range(m):
    src, dest = map(int, sys.stdin.readline().split())
    # 연결 리스트 생성
    adjMatrix[src].append(dest)
    adjMatrix[dest].append(src)

def dfs(v, visited):
    friend = 0
    stack = [v]
    while stack:
        v = stack.pop()

        if v not in visited:
            visited.append(v)
            friend += 1

            for w in adjMatrix[v]:
                stack.append(w)

    return visited, friend

visited = []
relationship = 0
result = []

for i in range(n):
    visited, people = dfs(i, visited)
    if people != 0:
        relationship += 1
        result.append(people)


print(relationship)
print(max(result), min(result))