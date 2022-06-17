import sys
from collections import deque
input = sys.stdin.readline


def bfs(n):
    q = deque([n])

    while q:
        node = q.popleft()

        if node == k:
            return dis[node]

        for i in (node-1, node+1, node*2):
            if 0 <= i <= MAX and not dis[i]:
                dis[i] = dis[node] + 1
                q.append(i)


n, k = map(int, input().split())

MAX = 10 ** 5
dis = [0] * (MAX + 1)

print(bfs(n))
