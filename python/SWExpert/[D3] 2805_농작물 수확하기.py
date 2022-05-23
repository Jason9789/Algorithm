T = int(input())

for tc in range(1, T+1):
    N = int(input())

    farm = [list(map(int, input())) for _ in range(N)]

    mid = N // 2
    start = end = mid
    result = 0

    for i in range(N):
        for j in range(start, end+1):
            result += farm[i][j]

        if i < mid:
            start, end = start - 1, end + 1

        else:
            start, end = start + 1, end - 1

    print(f'#{tc} {result}')
