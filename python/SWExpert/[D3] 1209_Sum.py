for tc in range(1, 11):

    T = int(input())

    grid = [list(map(int, input().split())) for _ in range(100)]

    result = 0

    grid2 = list(zip(*grid))

    for i in range(len(grid)):
        result = max(result, sum(grid[i]), sum(grid2[i]))

    tmp = []
    tmp2 = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if i == j:
                tmp.append(grid[i][j])
                tmp2.append(grid[i][j])

    result = max(result, sum(tmp), sum(tmp2))

    print(f'#{tc} {result}')
