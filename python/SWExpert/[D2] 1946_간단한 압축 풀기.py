from collections import deque
from typing import Deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    doc = Deque()

    for _ in range(N):
        tmp = list(map(str, input().split()))
        alpha = tmp[0]
        count = int(tmp[1])

        for _ in range(count):
            doc.append(alpha)

    print(f'#{tc}')
    while doc:
        result = ""
        if len(doc) >= 10:
            for i in range(10):
                result += doc.popleft()

        else:
            for i in range(len(doc)):
                result += doc.popleft()
        print(result)

    # print("".join(doc))
