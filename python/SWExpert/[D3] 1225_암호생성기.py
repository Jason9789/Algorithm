from collections import deque

for tc in range(10):

    T = int(input())

    q = deque(list(map(int, input().split())))

    while True:
        if q[-1] <= 0:
            q[-1] = 0
            break

        for i in range(1, 6):
            tmp = q.popleft() - i
            if tmp <= 0:
                tmp = 0
                q.append(tmp)
                break

            q.append(tmp)

    result = list(q)
    print(f"#{T} {' '.join(map(str, result))}")
