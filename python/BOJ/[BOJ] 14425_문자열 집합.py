import sys
input = sys.stdin.readline

n, m = map(int, input().split())

words = set([input() for _ in range(n)])

cnt = 0

for _ in range(m):
    word = input()
    if word in words:
        cnt += 1

print(cnt)
