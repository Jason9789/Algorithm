# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

import sys
from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())

    # 큐 입력받기
    tmp = list(map(int, sys.stdin.readline().split()))
    queue = deque((v, i) for i, v in enumerate(tmp))
    answer = 0

    while queue:
        item = queue.popleft()

        if queue and item[0] < max(queue)[0]:
            queue.append(item)

        else:
            answer += 1
            if item[1] == m:
                break
            if item[1] == m:
                break

    print(answer)
