import sys
sys.setrecursionlimit(10000)


def dfs(i, j):
    if i < 0 or i >= len(grid) or \
        j < 0 or j >= len(grid[0]) or \
            grid[i][j] != 1:
        return

    grid[i][j] = 0

    # 동서남북 탐색
    dfs(i + 1, j)
    dfs(i - 1, j)
    dfs(i, j + 1)
    dfs(i, j - 1)


T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    grid = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        m, n = map(int, input().split())
        grid[n][m] = 1

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                dfs(i, j)

                count += 1

    print(count)

    # 출력
    # for i in grid:
    #     print(i)
