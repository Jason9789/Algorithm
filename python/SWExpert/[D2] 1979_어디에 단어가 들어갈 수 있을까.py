T = int(input())


for tc in range(1, T+1):
    N, K = map(int, input().split())

    grid = [[x for x in input().split()] for _ in range(N)]

    result = 0

    # 행 탐색
    for i in range(N):
        count = 0
        for j in range(N):
            if grid[i][j] == '1':
                count += 1
            else:
                if count == K:
                    result += 1

                count = 0

        if count == K:
            result += 1

    # 열 탐색
    for i in range(N):
        count = 0
        for j in range(N):
            if grid[j][i] == '1':
                count += 1
            else:
                if count == K:
                    result += 1

                count = 0

        if count == K:
            result += 1

    print(f'#{tc} {result}')
