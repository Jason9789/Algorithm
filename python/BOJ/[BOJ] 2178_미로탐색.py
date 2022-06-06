from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        # 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위에 맞지 않을 때
            if nx < 0 or nx >= n or \
                    ny < 0 or ny >= m:
                continue

            # 이동할 수 없을 때
            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    return maze[n-1][m-1]


n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, input())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(maze)
print(bfs(0, 0))
print(maze)
