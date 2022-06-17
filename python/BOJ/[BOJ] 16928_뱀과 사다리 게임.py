from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    q = deque([1])

    while q:
        node = q.popleft()

        for move in range(1, 7):
            dice = node + move
            if 0 < dice <= 100 and not visited[dice]:
                if dice in ladders.keys():
                    dice = ladders[dice]

                if dice in snakes.keys():
                    dice = snakes[dice]

                if not visited[dice]:
                    q.append(dice)
                    visited[dice] = visited[node] + 1


n, m = map(int, input().split())

ladders = dict()
snakes = dict()

for _ in range(n):
    a, b = map(int, input().split())
    ladders[a] = b

for _ in range(m):
    a, b = map(int, input().split())
    snakes[a] = b

visited = [0] * 101

bfs()

print(visited[100])
