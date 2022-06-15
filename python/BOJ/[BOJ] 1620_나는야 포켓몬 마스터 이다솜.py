import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n+1):
    a = input().strip()

    dict[i] = a
    dict[a] = i

for _ in range(m):
    q = input().strip()

    if q.isdigit():
        print(dict[int(q)])

    else:
        print(dict[q])
