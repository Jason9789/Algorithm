from collections import deque
import sys

input = sys.stdin.readline


dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(sx, sy, ex, ey):
    q = deque()
    q.append([sx, sy])

    while q:
        a, b = q.popleft()

        if a == ex and b == ey:
            print(dist[ex][ey])
            break

        for i in range(8):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0 <= nx < I and 0 <= ny < I and not dist[nx][ny]:
                dist[nx][ny] = dist[a][b] + 1
                q.append([nx, ny])


t = int(input())  # 테스트 케이스 개수
for _ in range(t):
    I = int(input())  # 체스판 한 변의 길이

    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    dist = [[0] * I for i in range(I)]

    bfs(sx, sy, ex, ey)
