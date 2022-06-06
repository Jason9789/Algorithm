
from collections import deque

m, n = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

# 처음 받은 토마토 위치 찾기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append((i, j))


def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))


bfs()

for i in grid:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)

    # 다 익혔다면 최댓값을 저장
    result = max(result, max(i))

print(result-1)
