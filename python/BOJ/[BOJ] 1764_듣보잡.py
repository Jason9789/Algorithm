import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_listen = set()
no_see = set()

result = []

for _ in range(n):
    no_listen.add(input().strip())

for _ in range(m):
    no_see.add(input().strip())

result = no_listen & no_see


result = list(result)
result.sort()
print(len(result))

for i in result:
    print(i)
