import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, z):
    q = deque()
    q.append(([x, y, z]))
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1

    while q:
        a, b, c = q.popleft()

        if a == n-1 and b == m-1:
            return visited[a][b][c]

        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and c == 1:
                    visited[nx][ny][0] = visited[a][b][1] + 1
                    q.append([nx, ny, 0])

                elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                    visited[nx][ny][c] = visited[a][b][c] + 1
                    q.append([nx, ny, c])

    return -1


n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, list(input().strip()))))

print(bfs(0, 0, 1))
