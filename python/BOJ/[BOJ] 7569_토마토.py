import sys
from collections import deque


m, n, h = map(int, input().split())

grid = [[list(map(int, sys.stdin.readline().split()))
         for _ in range(n)] for _ in range(h)]
queue = deque()

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if grid[i][j][k] == 1:
                queue.append((i, j, k))


def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and grid[nx][ny][nz] == 0:
                queue.append((nx, ny, nz))
                grid[nx][ny][nz] = grid[x][y][z] + 1


bfs()

result = 0

for i in grid:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)

        result = max(result, max(j))

print(result-1)
