from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
position = list(map(int, input().split()))
de = deque([i for i in range(1, n+1)])

cnt = 0

for i in position:
    while True:
        if de[0] == i:
            de.popleft()
            break

        else:
            if de.index(i) < len(de) / 2:
                while de[0] != i:
                    de.append(de.popleft())
                    cnt += 1

            else:
                while de[0] != i:
                    de.appendleft(de.pop())
                    cnt += 1


print(cnt)
