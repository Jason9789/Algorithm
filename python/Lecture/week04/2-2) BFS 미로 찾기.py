from collections import deque

m, n = map(int, input().split())
maze = [[0 for _ in range(n)] for _ in range(m)]
dis = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    temp = input()
    maze[i] = list(map(int, list(str(temp))))

queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(map, s_x, s_y):
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue.append([s_x, s_y])
    dis[s_y][s_x] = 1

    while queue:
        x, y = queue.popleft()

        # 0은 서쪽, 1은 북쪽, 2는 동쪽, 3은 남쪽
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y and not visited[new_y][new_x]:
                if map[new_y][new_x] == 1:
                    visited[new_y][new_x] = True
                    queue.append((new_x, new_y))
                    dis[new_y][new_x] = dis[y][x] + 1
                    if new_y == m-1:
                        temp = dis[new_y][new_x]
                        queue.clear()
                        return temp

new_maze = []
for i in range(n):
    if maze[0][i] == 1:
        new_maze.append(bfs(maze, i, 0))

print(new_maze)

answer = list(new_maze)
if len(answer) == 0:
    print(-1)
else:
    print(min(answer))

